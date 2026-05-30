#!/usr/bin/env python3
"""
Add confetti celebration to all module index.html files
"""

import os
import re
from pathlib import Path

COURSE_DIR = Path("/Users/dglickman@bgrove.com/AI course")

# Confetti library CDN
CONFETTI_SCRIPT = '    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>'

# Confetti celebration code to add after resultsDiv.scrollIntoView
CONFETTI_CODE = '''
            // Celebration confetti for passing
            if (passed && typeof confetti === 'function') {
                // Initial burst
                confetti({
                    particleCount: 100,
                    spread: 70,
                    origin: { y: 0.6 },
                    colors: ['#2ED4B5', '#1657A0', '#FFC83B', '#19316A']
                });

                // Follow-up burst after slight delay
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

            // Close popup window after completion (if opened in popup)
            if (window.opener !== null) {
                setTimeout(() => {
                    const shouldClose = confirm('Module completed! Close this window?');
                    if (shouldClose) {
                        window.close();
                    }
                }, 3000); // Wait 3 seconds to let them see the results
            }'''

def process_module(module_path):
    """Process a single module's index.html"""
    index_file = module_path / "index.html"

    if not index_file.exists():
        return False, "No index.html found"

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modified = False

    # Check if confetti script already exists
    if 'canvas-confetti' not in content:
        # Add confetti script after scorm_api.js
        pattern = r'(<script src="scorm_api\.js"></script>)'
        replacement = r'\1\n' + CONFETTI_SCRIPT
        content = re.sub(pattern, replacement, content)
        modified = True
        print(f"  ✓ Added confetti library script")
    else:
        print(f"  → Confetti library already present")

    # Check if confetti celebration code already exists
    if 'Celebration confetti for passing' not in content:
        # Find showResults function and add confetti after scrollIntoView
        # Look for pattern: resultsDiv.scrollIntoView({ behavior: 'smooth' });
        #                   [potential whitespace]
        #                   }
        pattern = r"(resultsDiv\.scrollIntoView\(\{ behavior: ['\"]smooth['\"] \}\);)\s*(\n\s*}\s*\n)"

        if re.search(pattern, content):
            replacement = r'\1' + CONFETTI_CODE + r'\2'
            content = re.sub(pattern, replacement, content, count=1)
            modified = True
            print(f"  ✓ Added confetti celebration code")
        else:
            print(f"  ⚠ Could not find scrollIntoView pattern to insert confetti")
    else:
        print(f"  → Confetti celebration already present")

    if modified and content != original_content:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Updated successfully"
    else:
        return False, "No changes needed"

def main():
    print("Adding confetti to all modules...")
    print("=" * 60)

    modules_found = 0
    modules_updated = 0
    modules_skipped = 0

    # Process each module 0-13
    for i in range(14):
        module_dirs = list(COURSE_DIR.glob(f"Module {i} - *"))

        if not module_dirs:
            continue

        module_dir = module_dirs[0]
        modules_found += 1

        print(f"\nModule {i}: {module_dir.name}")

        updated, message = process_module(module_dir)

        if updated:
            modules_updated += 1
        else:
            modules_skipped += 1

    print("\n" + "=" * 60)
    print(f"Summary:")
    print(f"  Modules found: {modules_found}")
    print(f"  Modules updated: {modules_updated}")
    print(f"  Modules skipped: {modules_skipped}")
    print("=" * 60)

if __name__ == "__main__":
    main()
