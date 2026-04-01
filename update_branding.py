#!/usr/bin/env python3
"""
Update all module index.html files with official ActivTrak branding
Colors from slide_layouts.md:
- Dark Navy: #14203F (body text, closing backgrounds)
- Medium Navy: #19316A (header bars, accents)
- Blue: #1657A0 (section dividers, accent elements)
- White: #FFFFFF (backgrounds, text on dark)
- Teal: #2ED4B5 (CTAs, accent lines, highlights)
- Yellow: #FFC83B (secondary accents - use sparingly)
"""

import os
import re
import glob

# Old CSS variables to replace
OLD_CSS = """:root {
            --primary-blue: #0042F3;
            --pelorous: #33A7B5;
            --teal: #2FD3B4;
            --violet-red: #EE2C82;
            --dark-base: #252D38;
            --light-gray: #D9D9D9;
            --bg-light: #F8F9FA;
            --white: #FFFFFF;
            --success: #2FD3B4;
            --error: #EE2C82;
            --warning: #F5A623;
        }"""

# New ActivTrak branded CSS variables
NEW_CSS = """:root {
            /* ActivTrak Official Brand Colors */
            --dark-navy: #14203F;
            --medium-navy: #19316A;
            --blue: #1657A0;
            --teal: #2ED4B5;
            --yellow: #FFC83B;
            --white: #FFFFFF;
            --light-gray: #E5E7EB;
            --bg-light: #F8FAFC;

            /* Semantic mappings */
            --primary-blue: #19316A;
            --pelorous: #1657A0;
            --dark-base: #14203F;
            --success: #2ED4B5;
            --error: #DC2626;
            --warning: #F59E0B;
        }"""

# Old header gradient
OLD_HEADER = """background: linear-gradient(135deg, var(--primary-blue) 0%, #384B76 100%);"""
NEW_HEADER = """background: linear-gradient(135deg, var(--dark-navy) 0%, var(--medium-navy) 100%);"""

# Module source directories
SOURCE_MODULES = [
    "/Users/dglickman@bgrove.com/AI course/Module 0 - Pre-Flight Check/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 1 - The Cognitive Shift/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 2 - Model Selection/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 3 - Prompt Architecture/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 4 - Personal Projects & Folders/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 5 - The Sensory System/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 6 - Decision Hygiene/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 7 - The Hybrid Agent/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 8 - Introduction to Skills/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 9 - Systemizing Intelligence/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 10 - Agentic Data Analysis/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 11 - Code Execution/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 12 - Future Frontiers/index.html",
    "/Users/dglickman@bgrove.com/AI course/Module 13 - Capstone & Governance/index.html",
]

# SCORM module directories
SCORM_MODULES = [
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_0/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_1/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_2/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_3/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_4/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_5/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_6/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_7/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_8/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_9/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_10/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_11/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_12/index.html",
    "/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course/module_13/index.html",
]

def update_file(filepath):
    """Update a single file with new branding"""
    if not os.path.exists(filepath):
        print(f"  SKIP: {filepath} (not found)")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace CSS variables
    content = content.replace(OLD_CSS, NEW_CSS)

    # Replace header gradient
    content = content.replace(OLD_HEADER, NEW_HEADER)

    # Additional color replacements for hardcoded values
    replacements = [
        ('#0042F3', '#19316A'),  # primary-blue -> medium-navy
        ('#33A7B5', '#1657A0'),  # pelorous -> blue
        ('#2FD3B4', '#2ED4B5'),  # teal adjustment
        ('#252D38', '#14203F'),  # dark-base -> dark-navy
        ('#384B76', '#19316A'),  # header gradient end -> medium-navy
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  UPDATED: {os.path.basename(os.path.dirname(filepath))}")
        return True
    else:
        print(f"  NO CHANGE: {os.path.basename(os.path.dirname(filepath))}")
        return False

def main():
    print("Updating Source Module Files...")
    print("-" * 40)
    source_updated = 0
    for filepath in SOURCE_MODULES:
        if update_file(filepath):
            source_updated += 1

    print(f"\nSource modules updated: {source_updated}/{len(SOURCE_MODULES)}")

    print("\nUpdating SCORM Module Files...")
    print("-" * 40)
    scorm_updated = 0
    for filepath in SCORM_MODULES:
        if update_file(filepath):
            scorm_updated += 1

    print(f"\nSCORM modules updated: {scorm_updated}/{len(SCORM_MODULES)}")
    print(f"\nTotal files updated: {source_updated + scorm_updated}")

if __name__ == "__main__":
    main()
