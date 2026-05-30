#!/usr/bin/env python3
"""
Add confetti celebration to all module quiz completions
Finds the SCORM status call and adds confetti right after
"""

import os
import re
from pathlib import Path

COURSE_DIR = Path("/Users/dglickman@bgrove.com/AI course")

# Confetti celebration code
CONFETTI_CODE = '''
            // Celebration confetti for passing
            const passed = scorePercent >= 70;
            if (passed && typeof confetti === 'function') {
                // Initial burst
                confetti({
                    particleCount: 100,
                    spread: 70,
                    origin: { y: 0.6 },
                    colors: ['#2ED4B5', '#1657A0', '#FFC83B', '#19316A']
                });

                // Follow-up bursts
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
    """Process a single module's index.html"""
    index_file = module_path / "index.html"

    if not index_file.exists():
        return False, "No index.html found"

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Check if confetti celebration already exists
    if 'Celebration confetti for passing' in content:
        return False, "Confetti already present"

    # Find the SCORM status call pattern and add confetti after it
    # Pattern: setSCORMStatus(...);
    #          [whitespace]
    #          }
    pattern = r"(setSCORMStatus\([^)]+\);)\s*\n(\s*)\}"

    matches = list(re.finditer(pattern, content))

    if not matches:
        return False, "Could not find SCORM status call pattern"

    # Use the first match (should be the quiz completion function)
    match = matches[0]
    indentation = match.group(2)

    # Insert confetti code after the SCORM call, before the closing brace
    before = content[:match.end(1)]
    after = content[match.end(1):]

    # Add confetti code with proper indentation
    new_content = before + CONFETTI_CODE + after

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "Confetti added successfully"

def main():
    print("Adding confetti to all module quiz completions...")
    print("=" * 60)

    modules_found = 0
    modules_updated = 0
    modules_skipped = 0
    errors = []

    # Process each module 0-13
    for i in range(14):
        module_dirs = list(COURSE_DIR.glob(f"Module {i} - *"))

        if not module_dirs:
            continue

        module_dir = module_dirs[0]
        modules_found += 1

        print(f"\nModule {i}: {module_dir.name}")

        updated, message = process_module(module_dir)

        print(f"  {message}")

        if updated:
            modules_updated += 1
        else:
            modules_skipped += 1
            if "Could not find" in message and "already present" not in message:
                errors.append(f"Module {i}: {message}")

    print("\n" + "=" * 60)
    print(f"Summary:")
    print(f"  Modules found: {modules_found}")
    print(f"  Modules updated: {modules_updated}")
    print(f"  Modules skipped: {modules_skipped}")

    if errors:
        print(f"\nErrors:")
        for error in errors:
            print(f"  - {error}")

    print("=" * 60)

if __name__ == "__main__":
    main()
