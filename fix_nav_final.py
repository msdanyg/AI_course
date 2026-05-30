#!/usr/bin/env python3
"""
fix_nav_final.py

Final nav fix — uses string-based approach instead of regex for nested divs.
Strips ALL study-guide and complete fragments from the nav, then cleanly
appends them at section boundaries.
"""

import os
import re

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


def extract_nav(content):
    """Extract the nav block boundaries."""
    start = content.find('<nav class="sidebar">')
    end = content.find('</nav>', start)
    if start == -1 or end == -1:
        return None, None
    return start, end + len('</nav>')


def clean_nav_block(nav_block, attr):
    """
    Remove all study-guide items, complete items, orphaned fragments,
    and empty sections from the nav. Line-by-line approach.
    """
    lines = nav_block.split('\n')
    clean_lines = []
    skip_until_close = 0  # depth counter for skipping

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip any line that's part of a study-guide or complete nav-item
        if f'{attr}="study-guide"' in line or f'{attr}="complete"' in line:
            # Start skipping: count opening divs, skip until we balance
            skip_until_close = 1  # we opened one div
            i += 1
            while i < len(lines) and skip_until_close > 0:
                inner = lines[i].strip()
                skip_until_close += inner.count('<div') - inner.count('</div>')
                i += 1
            continue

        # Skip orphaned study-guide/complete fragments
        if '&#128203;' in stripped and 'nav-icon' in stripped:
            i += 1
            continue
        if '&#127942;' in stripped and 'nav-icon' in stripped:
            i += 1
            continue
        if 'Study Guide' in stripped and 'nav-label' in stripped:
            i += 1
            continue
        if '>Complete<' in stripped and 'nav-label' in stripped:
            i += 1
            continue

        # Skip orphaned study-guide related spans
        if stripped == '<span class="nav-label">Study Guide</span>':
            i += 1
            continue
        if stripped == '<span class="nav-duration">5 min</span>' and i > 0:
            # Only skip if preceded by a Study Guide label removal
            prev_clean = clean_lines[-1].strip() if clean_lines else ''
            if 'quiz' in prev_clean or '</div>' == prev_clean or prev_clean == '':
                i += 1
                continue

        clean_lines.append(line)
        i += 1

    return '\n'.join(clean_lines)


def remove_empty_sections(nav_block):
    """Remove nav-sections that have a title but no nav-items."""
    # Pattern: section with only a title, no nav-items
    nav_block = re.sub(
        r'\s*<div class="nav-section">\s*'
        r'<div class="nav-section-title">[^<]+</div>\s*'
        r'</div>',
        '',
        nav_block
    )
    return nav_block


def find_section_close(nav_block, section_title):
    """Find the closing </div> of a named nav-section."""
    title_pos = nav_block.find(f'>{section_title}<')
    if title_pos == -1:
        return -1

    # Find the start of the next section or </nav>
    next_section = nav_block.find('<div class="nav-section">', title_pos + len(section_title) + 5)
    boundary = next_section if next_section != -1 else nav_block.find('</nav>')

    if boundary == -1:
        return -1

    # The closing </div> of this section is the last one before the boundary
    close_pos = nav_block.rfind('</div>', title_pos, boundary)
    return close_pos


def add_study_guide_to_section(nav_block, section_title, attr):
    """Insert a study guide nav-item before the closing </div> of the named section."""
    close_pos = find_section_close(nav_block, section_title)
    if close_pos == -1:
        return nav_block, False

    study_guide = f"""
                <div class="nav-item" {attr}="study-guide">
                    <div class="nav-icon">&#128203;</div>
                    <span class="nav-label">Study Guide</span>
                </div>
            """

    nav_block = nav_block[:close_pos] + study_guide + nav_block[close_pos:]
    return nav_block, True


def add_finish_section(nav_block, attr):
    """Add a Finish section with Complete just before </nav>."""
    nav_close = nav_block.rfind('</nav>')
    if nav_close == -1:
        return nav_block

    finish = f"""
            <div class="nav-section">
                <div class="nav-section-title">Finish</div>
                <div class="nav-item" {attr}="complete">
                    <div class="nav-icon">&#127942;</div>
                    <span class="nav-label">Complete</span>
                </div>
            </div>
        """

    nav_block = nav_block[:nav_close] + finish + nav_block[nav_close:]
    return nav_block


def process_file(folder, filepath):
    if not os.path.exists(filepath):
        print(f"  SKIP: not found")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    attr = "data-section" if "data-section=" in content else "data-screen"

    nav_start, nav_end = extract_nav(content)
    if nav_start is None:
        print("    WARNING: no nav block found")
        return False

    nav_block = content[nav_start:nav_end]

    # Step 1: Clean all study-guide and complete items/fragments
    nav_block = clean_nav_block(nav_block, attr)

    # Step 2: Remove empty sections
    nav_block = remove_empty_sections(nav_block)

    # Step 3: Clean up excessive blank lines
    nav_block = re.sub(r'\n\s*\n\s*\n', '\n\n', nav_block)

    # Step 4: Add study guide to the first content section
    content_sections = ['Learn', 'Lesson Content', 'Module Content']
    added = False
    for sec_name in content_sections:
        nav_block, added = add_study_guide_to_section(nav_block, sec_name, attr)
        if added:
            print(f"    nav: added Study Guide to '{sec_name}'")
            break

    if not added:
        # Fallback: add to first section found
        title_match = re.search(r'>([^<]+)<', nav_block[nav_block.find('nav-section-title'):])
        if title_match:
            fallback_name = title_match.group(1)
            nav_block, added = add_study_guide_to_section(nav_block, fallback_name, attr)
            if added:
                print(f"    nav: added Study Guide to '{fallback_name}' (fallback)")

    # Step 5: Add Finish section with Complete
    nav_block = add_finish_section(nav_block, attr)
    print("    nav: added Finish section")

    # Replace nav in content
    content = content[:nav_start] + nav_block + content[nav_end:]

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    print("=" * 55)
    print("  Final nav rebuild (line-by-line clean)")
    print("=" * 55)

    fixed = 0
    for folder in MODULE_DIRS:
        filepath = os.path.join(BASE_DIR, folder, "index.html")
        print(f"\n[{folder}]")
        if process_file(folder, filepath):
            fixed += 1
            print(f"  FIXED")
        else:
            print(f"  no changes")

    print(f"\n{'=' * 55}")
    print(f"  Fixed: {fixed}/{len(MODULE_DIRS)} modules")
    print(f"{'=' * 55}")


if __name__ == "__main__":
    main()
