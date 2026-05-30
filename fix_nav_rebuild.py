#!/usr/bin/env python3
"""
fix_nav_rebuild.py

Rebuilds the nav sidebar to fix broken HTML from prior injection.
Strategy: find the <nav> block, strip all study-guide and complete nav items,
then re-add them cleanly — study-guide in the first content section,
complete in its own "Finish" section at the bottom.

Also fixes modules 5, 6, and Bonus SARA completion screens that
were missing the Close Course button.
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


def rebuild_nav(content):
    """Strip broken nav items and rebuild cleanly."""
    # Detect attribute type
    attr = "data-section" if "data-section=" in content else "data-screen"

    # Find the nav block
    nav_start = content.find('<nav class="sidebar">')
    nav_end = content.find('</nav>', nav_start)
    if nav_start == -1 or nav_end == -1:
        print("    nav: WARNING - could not find <nav> block")
        return content

    nav_block = content[nav_start:nav_end + len('</nav>')]

    # --- Step 1: Remove ALL study-guide nav items (clean or broken) ---
    # Pattern for clean study-guide nav item
    nav_block = re.sub(
        r'\s*<div class="nav-item"[^>]*' + attr + r'="study-guide"[^>]*>\s*'
        r'<div class="nav-icon">[^<]*</div>\s*'
        r'<span class="nav-label">[^<]*</span>\s*'
        r'(?:<span class="nav-duration">[^<]*</span>\s*)?'
        r'</div>',
        '',
        nav_block,
        flags=re.DOTALL
    )

    # Pattern for broken study-guide (with Complete injected inside it)
    # This catches: opening study-guide div, icon, then Complete div, then label, close
    nav_block = re.sub(
        r'\s*<div class="nav-item"[^>]*' + attr + r'="study-guide"[^>]*>\s*'
        r'<div class="nav-icon">[^<]*</div>\s*'
        r'<div class="nav-item"[^>]*' + attr + r'="complete"[^>]*>.*?</div>\s*'
        r'<span class="nav-label">[^<]*</span>\s*'
        r'(?:<span class="nav-duration">[^<]*</span>\s*)?'
        r'</div>',
        '',
        nav_block,
        flags=re.DOTALL
    )

    # Pattern for orphaned study-guide fragments (just the opening part)
    nav_block = re.sub(
        r'\s*<div class="nav-item"[^>]*' + attr + r'="study-guide"[^>]*>\s*'
        r'(?:<div class="nav-icon">[^<]*</div>\s*)?'
        r'(?:<span class="nav-label">[^<]*</span>\s*)?'
        r'(?:<span class="nav-duration">[^<]*</span>\s*)?',
        '',
        nav_block,
        flags=re.DOTALL
    )

    # --- Step 2: Remove ALL complete nav items ---
    nav_block = re.sub(
        r'\s*<div class="nav-item"[^>]*' + attr + r'="complete"[^>]*>\s*'
        r'<div class="nav-icon">[^<]*</div>\s*'
        r'<span class="nav-label">[^<]*</span>\s*'
        r'</div>',
        '',
        nav_block,
        flags=re.DOTALL
    )

    # --- Step 3: Remove empty "Reference" or "Finish" sections ---
    nav_block = re.sub(
        r'\s*<div class="nav-section">\s*'
        r'<div class="nav-section-title">(?:Reference|Finish)</div>\s*'
        r'</div>',
        '',
        nav_block,
        flags=re.DOTALL
    )

    # --- Step 4: Clean up any leftover empty closing divs or whitespace ---
    # Remove double blank lines
    nav_block = re.sub(r'\n\s*\n\s*\n', '\n\n', nav_block)

    # --- Step 5: Add study-guide to the first content section ---
    # Find the first nav-section that has content items (not "Getting Started" with just welcome/video)
    # Strategy: find the section that contains a "lesson" nav item, or the first section if none

    # Find all nav-sections in the block
    sections = list(re.finditer(r'<div class="nav-section-title">([^<]+)</div>', nav_block))

    target_section_name = None
    for sec in sections:
        name = sec.group(1)
        # Find the end of this section
        sec_start = sec.start()
        next_sec = nav_block.find('<div class="nav-section">', sec.end())
        sec_end = next_sec if next_sec != -1 else nav_block.find('</nav>')
        sec_content = nav_block[sec_start:sec_end]

        # Is this a content section? (has lesson or multiple items)
        if ('lesson' in sec_content.lower() or
            'content' in name.lower() or
            'learn' in name.lower()):
            target_section_name = name
            # Find the last </div> that closes a nav-item in this section
            # We want to insert study-guide after the last nav-item
            last_nav_item = None
            for m in re.finditer(r'<div class="nav-item"[^>]*>.*?</div>', sec_content, re.DOTALL):
                last_nav_item = m

            if last_nav_item:
                insert_pos = sec_start + last_nav_item.end()
                study_guide_item = f"""
                <div class="nav-item" {attr}="study-guide">
                    <div class="nav-icon">&#128203;</div>
                    <span class="nav-label">Study Guide</span>
                </div>"""
                nav_block = nav_block[:insert_pos] + study_guide_item + nav_block[insert_pos:]
                print(f"    nav: added Study Guide to '{name}' section")
            break

    if not target_section_name:
        # Fallback: add to the first section
        if sections:
            name = sections[0].group(1)
            sec_start = sections[0].start()
            next_sec = nav_block.find('<div class="nav-section">', sections[0].end())
            sec_end = next_sec if next_sec != -1 else nav_block.find('</nav>')
            sec_content = nav_block[sec_start:sec_end]
            last_nav_item = None
            for m in re.finditer(r'<div class="nav-item"[^>]*>.*?</div>', sec_content, re.DOTALL):
                last_nav_item = m
            if last_nav_item:
                insert_pos = sec_start + last_nav_item.end()
                study_guide_item = f"""
                <div class="nav-item" {attr}="study-guide">
                    <div class="nav-icon">&#128203;</div>
                    <span class="nav-label">Study Guide</span>
                </div>"""
                nav_block = nav_block[:insert_pos] + study_guide_item + nav_block[insert_pos:]
                print(f"    nav: added Study Guide to '{name}' section (fallback)")

    # --- Step 6: Add "Finish" section with Complete at the bottom ---
    # Insert just before </nav>
    nav_close = nav_block.rfind('</nav>')
    finish_section = f"""
            <div class="nav-section">
                <div class="nav-section-title">Finish</div>
                <div class="nav-item" {attr}="complete">
                    <div class="nav-icon">&#127942;</div>
                    <span class="nav-label">Complete</span>
                </div>
            </div>
        """
    nav_block = nav_block[:nav_close] + finish_section + nav_block[nav_close:]
    print("    nav: added Finish section with Complete")

    # Replace the nav block in the original content
    content = content[:nav_start] + nav_block + content[nav_end + len('</nav>'):]
    return content


def fix_completion_close(content):
    """Add Close Course button to completion screens that are missing it."""
    if "Close Course" in content:
        print("    complete: Close Course already present")
        return content

    # Find the completion screen
    complete_start = content.find('id="complete"')
    if complete_start == -1:
        print("    complete: no completion screen found")
        return content

    # Find the closing </section> of the complete screen
    # Look for various patterns to insert the close button

    # Strategy: find "Close this window" or "revisit any section" text in the completion area
    close_text_patterns = [
        "Close this window",
        "revisit any section",
        "You've completed all",
        "close this window",
    ]

    insert_after = -1
    for pattern in close_text_patterns:
        pos = content.find(pattern, complete_start)
        if pos != -1:
            # Find the end of the enclosing tag (</p> or </div>)
            tag_end = content.find('</p>', pos)
            if tag_end != -1 and tag_end < complete_start + 2000:
                insert_after = tag_end + len('</p>')
                break

    if insert_after == -1:
        # Fallback: find the closing </section> or </div> of the completion hero
        hero_end = content.find('</div>', complete_start + 100)
        if hero_end != -1:
            # Find the section close
            section_close = content.find('</section>', complete_start)
            if section_close != -1:
                insert_after = section_close
        else:
            print("    complete: WARNING - could not find insertion point")
            return content

    close_button = """

                    <button onclick="if(typeof finishSCORM==='function')finishSCORM(); if(window.opener){window.close();}else{alert('Course complete! You may close this window.');}" style="display:inline-block; margin-top:1.5rem; padding:0.8rem 2rem; border-radius:10px; border:none; background:linear-gradient(135deg,#2ED4B5,#1657A0); color:#fff; font-size:1rem; font-weight:600; cursor:pointer; transition:transform 0.15s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">Close Course</button>"""

    content = content[:insert_after] + close_button + content[insert_after:]
    print("    complete: added Close Course button")
    return content


def process_file(folder, filepath):
    if not os.path.exists(filepath):
        print(f"  SKIP: not found")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    content = rebuild_nav(content)
    content = fix_completion_close(content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    print("=" * 55)
    print("  Rebuilding nav sidebars + fixing Close buttons")
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
