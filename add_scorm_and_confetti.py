#!/usr/bin/env python3
"""
Add SCORM integration and confetti to all modules
"""

import os
import re
from pathlib import Path

COURSE_DIR = Path("/Users/dglickman@bgrove.com/AI course")

# SCORM + Confetti code to insert before closing brace of showResults()
SCORM_AND_CONFETTI = '''
            // SCORM reporting
            const scorePercent = Math.round((correct / quizAnswers.length) * 100);
            const passed = scorePercent >= 70;

            if (typeof setSCORMScore === 'function') {
                setSCORMScore(scorePercent);
            }
            if (typeof setSCORMStatus === 'function') {
                setSCORMStatus(passed ? 'passed' : 'failed');
            }

            // Celebration confetti for passing
            if (passed && typeof confetti === 'function') {
                confetti({
                    particleCount: 100,
                    spread: 70,
                    origin: { y: 0.6 },
                    colors: ['#2ED4B5', '#1657A0', '#FFC83B', '#19316A']
                });

                setTimeout(() => {
                    confetti({
                        particleCount: 50,
                        angle: 60,
                        spread: 55,
                        origin: { x: 0 },
                        colors: ['#2ED4B5', '#1657A0', '#FFC83B']
                    });
                }, 250);

                setTimeout(() => {
                    confetti({
                        particleCount: 50,
                        angle: 120,
                        spread: 55,
                        origin: { x: 1 },
                        colors: ['#2ED4B5', '#1657A0', '#FFC83B']
                    });
                }, 400);
            }

            // Close popup window after completion
            if (window.opener !== null) {
                setTimeout(() => {
                    const shouldClose = confirm('Module completed! Close this window?');
                    if (shouldClose) {
                        window.close();
                    }
                }, 3000);
            }'''

def process_module(module_path):
    """Add SCORM and confetti to a module"""
    index_file = module_path / "index.html"

    if not index_file.exists():
        return False, "No index.html"

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has SCORM + confetti
    if 'Celebration confetti for passing' in content:
        return False, "Already has confetti"

    # Find showResults() function ending
    # Pattern: function showResults() { ... }
    # We want to add code right before the final closing brace

    pattern = r'(function showResults\(\)\s*\{[^}]*)(}\s*\n)'

    # Use a more sophisticated approach: find the function and its closing brace
    func_start = content.find('function showResults()')

    if func_start == -1:
        return False, "No showResults function"

    # Find the matching closing brace
    # Start after the opening brace of the function
    open_brace = content.find('{', func_start)
    if open_brace == -1:
        return False, "Cannot find opening brace"

    brace_count = 1
    pos = open_brace + 1

    while pos < len(content) and brace_count > 0:
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
        pos += 1

    if brace_count != 0:
        return False, "Cannot find matching closing brace"

    # pos is now right after the closing brace
    closing_brace_pos = pos - 1

    # Get the indentation of the closing brace
    line_start = content.rfind('\n', 0, closing_brace_pos) + 1
    indentation = content[line_start:closing_brace_pos]

    # Insert SCORM + confetti before the closing brace
    new_content = (
        content[:closing_brace_pos] +
        SCORM_AND_CONFETTI +
        '\n' + indentation +
        content[closing_brace_pos:]
    )

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "Added SCORM + confetti"

def main():
    print("Adding SCORM integration and confetti to all modules...")
    print("=" * 60)

    modules_updated = 0
    modules_skipped = 0

    # Process modules 5-7 and 9-13 (the ones that failed before)
    target_modules = [5, 6, 7, 9, 10, 11, 12, 13]

    for i in target_modules:
        module_dirs = list(COURSE_DIR.glob(f"Module {i} - *"))

        if not module_dirs:
            continue

        module_dir = module_dirs[0]
        print(f"\nModule {i}: {module_dir.name}")

        updated, message = process_module(module_dir)
        print(f"  {message}")

        if updated:
            modules_updated += 1
        else:
            modules_skipped += 1

    print("\n" + "=" * 60)
    print(f"Summary:")
    print(f"  Modules updated: {modules_updated}")
    print(f"  Modules skipped: {modules_skipped}")
    print("=" * 60)

if __name__ == "__main__":
    main()
