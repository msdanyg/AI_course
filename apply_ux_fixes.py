#!/usr/bin/env python3
"""
apply_ux_fixes.py

Applies all UX review recommendations across all modules:

CRITICAL:
  1. Fix lab modal emoji (laughing face → rocket)
  2. Add onclick handlers to Study Guide nav items
  3. Add missing CSS variables (--dark-navy, --medium-navy)
  4. Hide static "Module Complete" button until quiz is passed

HIGH:
  5. Replace alert() copy feedback with toast notification
  6. Move hardcoded completion colors to CSS variables
  7. Fix Close Course button fallback for iframe/LMS context

MEDIUM:
  8. Add keyboard accessibility to flashcards
  9. Add checklist toggle animation
 10. Add encouragement message for near-pass quiz scores
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

FIXES_APPLIED = {}


def count(key):
    FIXES_APPLIED[key] = FIXES_APPLIED.get(key, 0) + 1


# ─── FIX 1: Lab modal emoji ──────────────────────────────────────────────────

def fix_modal_emoji(content):
    """Replace laughing/crying emoji with rocket emoji in lab modal."""
    old = '<div style="font-size: 2.5rem; margin-bottom: 1rem;">&#129514;</div>'
    new = '<div style="font-size: 2.5rem; margin-bottom: 1rem;">&#128640;</div>'
    if old in content:
        content = content.replace(old, new)
        count("modal_emoji")
    return content


# ─── FIX 2: Study Guide onclick handler ──────────────────────────────────────

def fix_study_guide_onclick(content):
    """Add onclick handler to Study Guide nav items that are missing one."""
    attr = "data-section" if "data-section=" in content else "data-screen"

    # Pattern: study-guide nav item without onclick
    old_pattern = f'{attr}="study-guide">'
    has_onclick = f'{attr}="study-guide" onclick='

    if has_onclick not in content and old_pattern in content:
        content = content.replace(
            f'{attr}="study-guide">',
            f'{attr}="study-guide" onclick="navigateTo(\'study-guide\')">'
        )
        count("sg_onclick")
    return content


# ─── FIX 3: Missing CSS variables ────────────────────────────────────────────

def fix_missing_css_vars(content):
    """Add --dark-navy and --medium-navy if referenced but not defined."""
    if "var(--dark-navy)" in content and "--dark-navy:" not in content:
        # Find :root { and add the missing variables
        root_match = re.search(r'(:root\s*\{[^}]*?)(})', content, re.DOTALL)
        if root_match:
            existing_vars = root_match.group(1)
            # Add navy variables before the closing brace
            navy_vars = """
            /* ActivTrak Navy Colors */
            --dark-navy: #14203F;
            --medium-navy: #19316A;
        """
            content = content[:root_match.end(1)] + navy_vars + content[root_match.start(2):]
            count("css_vars")
    return content


# ─── FIX 4: Block completion on quiz failure ──────────────────────────────────

def fix_completion_gate(content):
    """
    Hide the static "Module Complete" button and only show it after quiz pass.
    Strategy: add id and hide by default, then show it in the quiz pass logic.
    """
    # Find the static "Module Complete →" button in the quiz section nav
    # Pattern: onclick="navigateTo('complete')">Module Complete →</button>
    static_btn = re.search(
        r'(<button[^>]*onclick="navigateTo\(\'complete\'\)"[^>]*>)\s*Module Complete\s*→\s*</button>',
        content
    )

    if static_btn:
        # Add id and hidden style to the static button
        old_tag = static_btn.group(1)
        if 'id="staticCompleteBtn"' not in old_tag:
            new_tag = old_tag.replace('<button', '<button id="staticCompleteBtn" style="display:none"', 1)
            content = content.replace(old_tag, new_tag, 1)

            # Now make the dynamic quiz code also unhide this button on pass
            # Find the dynamic button injection code
            if "staticCompleteBtn" not in content[content.find("setSCORMScore"):]:
                # Add unhide logic after the dynamic button injection
                show_static = """
            // Also show the static complete button in section nav
            var staticBtn = document.getElementById('staticCompleteBtn');
            if (staticBtn) { staticBtn.style.display = ''; }
"""
                # Insert after the dynamic button block
                dynamic_marker = "if (resultsEl) resultsEl.appendChild(completeBtn);"
                if dynamic_marker in content:
                    content = content.replace(
                        dynamic_marker,
                        dynamic_marker + "\n" + show_static
                    )
                else:
                    # Alternative: insert after the confetti block's pass check
                    # Find "if (passed)" in the quiz function and add there
                    pass

            count("completion_gate")
    return content


# ─── FIX 5: Toast notification instead of alert ──────────────────────────────

TOAST_CSS = """
        /* Toast notification */
        .toast-notification {
            position: fixed;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: #14203F;
            color: #fff;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: 500;
            z-index: 20000;
            opacity: 0;
            transition: transform 0.3s ease, opacity 0.3s ease;
            pointer-events: none;
        }
        .toast-notification.visible {
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }
"""

TOAST_JS = """
        function showToast(message) {
            var existing = document.getElementById('toastNotification');
            if (existing) existing.remove();
            var toast = document.createElement('div');
            toast.id = 'toastNotification';
            toast.className = 'toast-notification';
            toast.textContent = message;
            document.body.appendChild(toast);
            requestAnimationFrame(function() {
                toast.classList.add('visible');
            });
            setTimeout(function() {
                toast.classList.remove('visible');
                setTimeout(function() { toast.remove(); }, 300);
            }, 2000);
        }
"""


def fix_copy_toast(content):
    """Replace alert('Copied to clipboard!') with toast notification."""
    if "alert('Copied to clipboard!')" not in content:
        return content

    # Add toast CSS before </style>
    if ".toast-notification" not in content:
        last_style = content.rfind("</style>")
        if last_style != -1:
            content = content[:last_style] + TOAST_CSS + "\n    " + content[last_style:]

    # Add toast JS function before copyToClipboard
    if "showToast" not in content:
        copy_func = content.find("function copyToClipboard")
        if copy_func != -1:
            content = content[:copy_func] + TOAST_JS + "\n" + content[copy_func:]

    # Replace alert with showToast
    content = content.replace(
        "alert('Copied to clipboard!');",
        "showToast('Copied to clipboard!');"
    )
    count("toast")
    return content


# ─── FIX 6: Completion colors to CSS variables ───────────────────────────────

def fix_completion_colors(content):
    """Replace hardcoded colors in completion screen with CSS variables."""
    changes = 0

    # Completion icon gradient — use variables if defined
    old_gradient = "background: linear-gradient(135deg, #2ED4B5 0%, #1657A0 100%);"
    new_gradient = "background: linear-gradient(135deg, var(--teal, #2ED4B5) 0%, var(--blue, #1657A0) 100%);"
    if old_gradient in content:
        content = content.replace(old_gradient, new_gradient)
        changes += 1

    # Stat value color
    old_stat = "color: #2ED4B5;"
    new_stat = "color: var(--teal, #2ED4B5);"
    if ".completion-stat-value" in content and old_stat in content:
        # Only replace within the CSS block (not inline styles)
        content = content.replace(old_stat, new_stat, 1)
        changes += 1

    if changes:
        count("completion_colors")
    return content


# ─── FIX 7: Close Course button for iframe/LMS ───────────────────────────────

def fix_close_button(content):
    """Replace alert fallback with graceful in-page message."""
    old_close = (
        """onclick="if(typeof finishSCORM==='function')finishSCORM(); """
        """if(window.opener){window.close();}else{alert('Course complete! You may close this window.');}" """
    )
    new_close = (
        """onclick="if(typeof finishSCORM==='function')finishSCORM(); """
        """if(window.opener||window!==window.top){try{window.close();}catch(e){}}"""
        """this.textContent='Course Complete \\u2713';this.disabled=true;this.style.background='#14203F';" """
    )
    if old_close in content:
        content = content.replace(old_close, new_close)
        count("close_button")
    return content


# ─── FIX 8: Flashcard keyboard accessibility ─────────────────────────────────

def fix_flashcard_a11y(content):
    """Add tabindex, role, aria-label, and keydown handler to flashcards."""
    # Pattern: <div class="flashcard" id="flashcard" onclick="flipCard()">
    old = 'class="flashcard" id="flashcard" onclick="flipCard()"'
    new = ('class="flashcard" id="flashcard" onclick="flipCard()" '
           'tabindex="0" role="button" aria-label="Flashcard - click or press Enter to flip" '
           'onkeydown="if(event.key===\'Enter\'||event.key===\' \'){event.preventDefault();flipCard();}"')

    if old in content and 'tabindex="0"' not in content[content.find('id="flashcard"'):content.find('id="flashcard"') + 200]:
        content = content.replace(old, new, 1)
        count("flashcard_a11y")
    return content


# ─── FIX 9: Checklist toggle animation ───────────────────────────────────────

CHECKLIST_TRANSITION_CSS = """
        .checklist-item, .lab-checkbox {
            transition: background-color 0.2s ease, border-color 0.2s ease;
        }
"""


def fix_checklist_animation(content):
    """Add smooth transition to checklist items."""
    if "checklist-item" not in content:
        return content
    if "transition: background-color 0.2s" in content:
        return content

    # Inject transition CSS
    last_style = content.rfind("</style>")
    if last_style != -1:
        content = content[:last_style] + CHECKLIST_TRANSITION_CSS + "\n    " + content[last_style:]
        count("checklist_anim")
    return content


# ─── FIX 10: Near-pass encouragement ─────────────────────────────────────────

def fix_near_pass_message(content):
    """
    Add encouragement message for scores between 50-69%.
    Find the quiz results display and add a near-pass case.
    """
    # Look for the pattern where we check if passed
    # Most modules have: if (passed) { ... } else { statusDiv.innerHTML = '...' }
    # or a 3-tier message system

    # Strategy: find the "not yet passing" or "failed" message and add a near-pass tier
    # Only add if not already present
    if "almost there" in content.lower() or "close!" in content.lower():
        return content

    # Pattern varies by module. Let's target the common patterns:

    # Pattern A: Module 6 style - checkQuiz with inline results
    # if (scorePercent === 100) { ... } else if (passed) { ... } else { ... }
    not_passing = re.search(
        r"(statusDiv\.innerHTML\s*=\s*['\"]<span[^>]*>)Not yet passing",
        content
    )
    if not_passing:
        # Add a near-pass check before the fail case
        # Find the else { that contains this
        else_pos = content.rfind("} else {", 0, not_passing.start())
        if else_pos != -1:
            near_pass = """} else if (scorePercent >= 50) {
                statusDiv.innerHTML = '<span style="color: #F59E0B;">So close! You\\'re almost there. Review the sections you missed and try again — you\\'ve got this.</span>';
            """
            content = content[:else_pos] + near_pass + content[else_pos:]
            count("near_pass")
            return content

    # Pattern B: Module 0 style - showQuizResults with message variable
    review_needed = re.search(
        r'(message\s*=\s*["\']).*?[Rr]eview.*?retake',
        content
    )
    if review_needed:
        # Find the if/else structure
        else_pos = content.rfind("} else {", 0, review_needed.start())
        if else_pos != -1 and "almost there" not in content[else_pos:else_pos+300]:
            near_pass = """} else if (scorePercent >= 50) {
                message = "So close! You're almost there. Review the sections you missed and try again.";
            """
            content = content[:else_pos] + near_pass + content[else_pos:]
            count("near_pass")
            return content

    # Pattern C: Modules using direct innerHTML with "Review" or "not passing"
    review_pattern = re.search(
        r"(resultsMessage\.innerHTML|statusEl\.innerHTML|messageEl\.innerHTML)\s*=\s*['\"].*?[Rr]eview",
        content
    )
    if review_pattern:
        else_pos = content.rfind("} else {", 0, review_pattern.start())
        if else_pos != -1 and "almost there" not in content[else_pos:else_pos+300]:
            var_name = review_pattern.group(1)
            near_pass = f"""}} else if (scorePercent >= 50) {{
                {var_name} = "So close! You\\'re almost there. Review the sections you missed and try again.";
            """
            content = content[:else_pos] + near_pass + content[else_pos:]
            count("near_pass")
            return content

    return content


# ─── Main processing ─────────────────────────────────────────────────────────

def process_file(folder, filepath):
    if not os.path.exists(filepath):
        print(f"  SKIP: not found")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Apply all fixes
    content = fix_modal_emoji(content)            # 1
    content = fix_study_guide_onclick(content)     # 2
    content = fix_missing_css_vars(content)        # 3
    content = fix_completion_gate(content)         # 4
    content = fix_copy_toast(content)              # 5
    content = fix_completion_colors(content)       # 6
    content = fix_close_button(content)            # 7
    content = fix_flashcard_a11y(content)          # 8
    content = fix_checklist_animation(content)     # 9
    content = fix_near_pass_message(content)       # 10

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    print("=" * 60)
    print("  Applying UX Review Fixes (10 recommendations)")
    print("=" * 60)

    fixed = 0
    for folder in MODULE_DIRS:
        filepath = os.path.join(BASE_DIR, folder, "index.html")
        print(f"\n[{folder}]")
        if process_file(folder, filepath):
            fixed += 1
            print(f"  UPDATED")
        else:
            print(f"  no changes")

    print(f"\n{'=' * 60}")
    print(f"  Modules updated: {fixed}/{len(MODULE_DIRS)}")
    print(f"\n  Fix summary:")
    for key, val in sorted(FIXES_APPLIED.items()):
        print(f"    {key}: {val} modules")
    print(f"\n  Next: Re-run create_packages.sh")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
