#!/usr/bin/env python3
"""
fix_navigate_wrapper.py

Fixes the missing navigateTo → doNavigate rename that the main script failed to apply.
Also adds the updateProgress guard for study-guide (not in screens array).

Run after update_completion_flow.py.
"""

import os
import re
import glob

BASE_DIR = "/Users/dglickman@bgrove.com/AI course"

MODULE_DIRS = [
    "Module 0 - Pre-Flight Check",
    "Module 1 - The Cognitive Shift",
    "Module 2 - Model Selection",
    "Module 3 - Prompt Architecture",
    "Module 4 - Personal Projects & Folders",
    "Module 5 - The Sensory System",
    "Module 6 - Decision Hygiene",
    "Module 7 - The Hybrid Agent",
    "Module 9 - Systemizing Intelligence",
    "Module 10 - Agentic Data Analysis",
    "Module 11 - Code Execution",
    "Module 12 - Future Frontiers",
    "Module 13 - Capstone & Governance",
    "Bonus - SARA",
]


def fix_navigate_wrapper(content):
    """Rename navigateTo → doNavigate and create the wrapper."""

    # Already fixed?
    if "function doNavigate(" in content:
        print("    navigate wrapper: already present")
        return content

    # Find the navigateTo function definition
    nav_match = re.search(r"function navigateTo\((\w+)\)", content)
    if not nav_match:
        print("    WARNING: no navigateTo function found")
        return content

    param_name = nav_match.group(1)
    func_start = nav_match.start()

    # Rename: function navigateTo → function doNavigate (first occurrence only)
    content = content[:func_start] + content[func_start:].replace(
        f"function navigateTo({param_name})",
        f"function doNavigate({param_name})",
        1
    )

    # Find the end of the doNavigate function body (matching braces)
    do_nav_pos = content.find(f"function doNavigate({param_name})")
    brace_start = content.find("{", do_nav_pos)
    if brace_start == -1:
        print("    WARNING: no opening brace for doNavigate")
        return content

    depth = 0
    i = brace_start
    while i < len(content):
        if content[i] == "{":
            depth += 1
        elif content[i] == "}":
            depth -= 1
            if depth == 0:
                break
        i += 1

    if depth != 0:
        print("    WARNING: could not find closing brace for doNavigate")
        return content

    insert_pos = i + 1

    # Create the wrapper
    wrapper = """

        function navigateTo(target) {
            if (target === 'quiz' && !labCertified && !quizAccessConfirmed) {
                showLabModal();
                return;
            }
            doNavigate(target);
        }
"""

    content = content[:insert_pos] + wrapper + content[insert_pos:]
    print("    navigate wrapper: APPLIED")
    return content


def fix_progress_guard(content):
    """Add -1 guard to updateProgress so study-guide doesn't reset progress."""

    if "function updateProgress" not in content:
        print("    progress guard: no updateProgress function")
        return content

    # Already guarded?
    if "=== -1" in content[content.find("function updateProgress"):content.find("function updateProgress") + 500]:
        print("    progress guard: already present")
        return content

    # Find the index variable in updateProgress
    up_start = content.find("function updateProgress")
    up_end = content.find("}", up_start)
    # Find the closing brace properly
    brace_start = content.find("{", up_start)
    depth = 0
    i = brace_start
    while i < len(content):
        if content[i] == "{":
            depth += 1
        elif content[i] == "}":
            depth -= 1
            if depth == 0:
                up_end = i
                break
        i += 1

    up_body = content[up_start:up_end]

    # Find the index variable (indexOf, findIndex, or direct index calc)
    idx_match = re.search(
        r"(?:const|var|let)\s+(\w+)\s*=\s*\w+\.(indexOf|findIndex)\(",
        up_body
    )

    if idx_match:
        var_name = idx_match.group(1)
        # Find the semicolon ending this statement in the original content
        abs_pos = up_start + idx_match.end()

        # For findIndex with multi-line arrow functions, find the closing paren + semicolon
        paren_depth = 1  # we're inside the opening (
        j = abs_pos
        while j < len(content) and paren_depth > 0:
            if content[j] == "(":
                paren_depth += 1
            elif content[j] == ")":
                paren_depth -= 1
            j += 1

        # Find the semicolon after the closing paren
        semi_pos = content.find(";", j - 1)
        if semi_pos != -1 and semi_pos < up_start + len(up_body) + 100:
            guard = f"\n            if ({var_name} === -1) return;"
            content = content[:semi_pos + 1] + guard + content[semi_pos + 1:]
            print(f"    progress guard: APPLIED (guarding {var_name})")
            return content

    # Alternative: some modules use completedScreens.size / screens.length
    # These don't need a guard since they don't use indexOf
    if "completedScreens" in up_body:
        print("    progress guard: not needed (uses completedScreens set)")
        return content

    print("    progress guard: could not find index variable to guard")
    return content


def process_file(filepath):
    """Apply fixes to a single module file."""
    if not os.path.exists(filepath):
        print(f"  SKIP: not found")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    content = fix_navigate_wrapper(content)
    content = fix_progress_guard(content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    print("=" * 50)
    print("  Fixing navigateTo wrapper + progress guard")
    print("=" * 50)

    fixed = 0
    for folder in MODULE_DIRS:
        filepath = os.path.join(BASE_DIR, folder, "index.html")
        print(f"\n[{folder}]")
        if process_file(filepath):
            fixed += 1
            print(f"  FIXED")
        else:
            print(f"  no changes needed")

    print(f"\n{'=' * 50}")
    print(f"  Fixed: {fixed}/{len(MODULE_DIRS)} modules")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
