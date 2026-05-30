#!/usr/bin/env python3
"""
fix_study_guide_and_lab.py

Fixes three issues across all modules:

1. STUDY GUIDE NAV: Move from "Reference" section into "Learn" section (alongside lessons).
   Fix broken HTML where "Complete" nav item was injected inside study-guide div.
   Rename "Reference" section to just hold "Complete".

2. LAB CERTIFICATION: Remove the checkbox from the lab page.
   Move the certification into the modal popup — the "Continue to Quiz" button
   becomes "I've completed the lab, continue to Quiz" (the modal IS the cert).

3. COMPLETION SCREEN: Add a "Close Course" button.
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


def fix_nav_sidebar(content):
    """
    Fix the broken nav: remove the injected Complete nav from inside study-guide,
    move study-guide to the Learn section, and put Complete in its own section.
    """
    # Detect which attribute is used
    if "data-section=" in content:
        attr = "data-section"
    else:
        attr = "data-screen"

    # --- Step 1: Fix the broken "Reference" section ---
    # The broken pattern looks like:
    #   <div class="nav-section">
    #       <div class="nav-section-title">Reference</div>
    #       <div class="nav-item" data-X="study-guide">
    #           <div class="nav-icon">📋</div>
    #       <div class="nav-item" data-X="complete">        <-- injected inside study-guide
    #           <div class="nav-icon">&#127942;</div>
    #           <span class="nav-label">Complete</span>
    #       </div>
    #           <span class="nav-label">Study Guide</span>
    #       </div>
    #   </div>

    # Replace the entire broken Reference section with a clean one
    broken_ref_pattern = re.compile(
        r'<div class="nav-section">\s*'
        r'<div class="nav-section-title">Reference</div>\s*'
        r'<div class="nav-item"[^>]*' + attr + r'="study-guide"[^>]*>.*?'
        r'</div>\s*</div>',
        re.DOTALL
    )

    clean_ref_section = f"""<div class="nav-section">
                <div class="nav-section-title">Finish</div>
                <div class="nav-item" {attr}="complete">
                    <div class="nav-icon">&#127942;</div>
                    <span class="nav-label">Complete</span>
                </div>
            </div>"""

    match = broken_ref_pattern.search(content)
    if match:
        content = content[:match.start()] + clean_ref_section + content[match.end():]
        print("    nav: fixed broken Reference section")
    else:
        # Try to find a clean Reference section (may already be fixed)
        clean_ref_pattern = re.compile(
            r'<div class="nav-section">\s*'
            r'<div class="nav-section-title">Reference</div>.*?'
            r'</div>\s*</div>',
            re.DOTALL
        )
        match = clean_ref_pattern.search(content)
        if match:
            content = content[:match.start()] + clean_ref_section + content[match.end():]
            print("    nav: replaced Reference section with Finish")
        else:
            print("    nav: WARNING - could not find Reference section")

    # --- Step 2: Add study-guide to the Learn section ---
    # Find the end of the Learn section (the last nav-item before </div> of that section)
    # The Learn section contains video, lesson(s), flashcards

    # Patterns to find the Learn section's closing:
    # Look for the section that has "Learn" or "Module Content" as title
    learn_section = re.search(
        r'<div class="nav-section-title">(Learn|Module Content)</div>',
        content
    )

    if learn_section:
        # Find the closing </div> of this nav-section
        # It's the </div> before the next <div class="nav-section">
        next_section = content.find('<div class="nav-section">', learn_section.end())
        if next_section != -1:
            # Find the </div> just before the next section
            close_div = content.rfind('</div>', learn_section.end(), next_section)
            if close_div != -1:
                # Check if study guide nav item already exists in Learn section
                learn_block = content[learn_section.start():next_section]
                if 'study-guide' not in learn_block:
                    study_guide_nav = f"""
                <div class="nav-item" {attr}="study-guide">
                    <div class="nav-icon">&#128203;</div>
                    <span class="nav-label">Study Guide</span>
                </div>
            """
                    # Insert before the closing </div> of the Learn section
                    content = content[:close_div] + study_guide_nav + content[close_div:]
                    print("    nav: added Study Guide to Learn section")
                else:
                    print("    nav: Study Guide already in Learn section")
    else:
        print("    nav: WARNING - could not find Learn/Module Content section")

    return content


def fix_lab_certification(content):
    """
    Remove the lab-certification checkbox from the lab page.
    The modal popup handles certification instead.
    """
    # Remove the lab-certification div
    cert_pattern = re.compile(
        r'\n\s*<div class="lab-certification">.*?</div>\s*\n',
        re.DOTALL
    )
    new_content = cert_pattern.sub('\n', content)
    if new_content != content:
        print("    lab: removed certification checkbox from page")
        content = new_content
    else:
        print("    lab: no checkbox to remove (already clean)")

    return content


def fix_lab_modal(content):
    """
    Update the modal text: the "Continue to Quiz" button becomes
    "I've completed the lab, continue to Quiz" — making the modal the cert.
    """
    old_btn = '>Continue to Quiz</button>'
    new_btn = ">I've completed the lab, take me to the Quiz</button>"

    if old_btn in content:
        content = content.replace(old_btn, new_btn)
        print("    modal: updated button text")
    else:
        print("    modal: button text already updated or not found")

    return content


def fix_completion_close_button(content):
    """Add a 'Close Course' button to the completion screen."""
    if "Close Course" in content or "close-course" in content:
        print("    complete: Close button already present")
        return content

    # Find the completion-footer paragraph and add a close button after it
    footer_pattern = re.compile(
        r'(<p class="completion-footer">.*?</p>)',
        re.DOTALL
    )
    match = footer_pattern.search(content)
    if match:
        close_button = """

                    <button onclick="if(typeof finishSCORM==='function')finishSCORM(); if(window.opener){window.close();}else{alert('Course complete! You may close this window.');}" style="display:inline-block; margin-top:1.5rem; padding:0.8rem 2rem; border-radius:10px; border:none; background:linear-gradient(135deg,#2ED4B5,#1657A0); color:#fff; font-size:1rem; font-weight:600; cursor:pointer; transition:transform 0.15s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">Close Course</button>"""
        content = content[:match.end()] + close_button + content[match.end():]
        print("    complete: added Close Course button")
    else:
        print("    complete: WARNING - could not find completion-footer")

    return content


def process_file(folder, filepath):
    """Apply all fixes to a single module."""
    if not os.path.exists(filepath):
        print(f"  SKIP: not found")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    content = fix_nav_sidebar(content)
    content = fix_lab_certification(content)
    content = fix_lab_modal(content)
    content = fix_completion_close_button(content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    print("=" * 55)
    print("  Fixing: Study Guide nav + Lab modal + Close button")
    print("=" * 55)

    fixed = 0
    for folder in MODULE_DIRS:
        filepath = os.path.join(BASE_DIR, folder, "index.html")
        print(f"\n[{folder}]")
        if process_file(folder, filepath):
            fixed += 1
            print(f"  FIXED")
        else:
            print(f"  no changes needed")

    print(f"\n{'=' * 55}")
    print(f"  Fixed: {fixed}/{len(MODULE_DIRS)} modules")
    print(f"  Next: Re-run create_packages.sh")
    print(f"{'=' * 55}")


if __name__ == "__main__":
    main()
