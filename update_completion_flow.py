#!/usr/bin/env python3
"""
update_completion_flow.py

Applies three UX improvements to all module index.html files:
1. Lab certification checkbox with gentle quiz gate modal
2. Completion celebration screen (post-quiz, replaces study guide as "the end")
3. Study guide repositioned as sidebar-only reference (not a linear step)

Only modifies source files (Module X - Title/index.html).
SCORM copies are derived artifacts — re-run create_packages.sh after this.
"""

import os
import re
import sys

BASE_DIR = "/Users/dglickman@bgrove.com/AI course"

# Module metadata for completion screens
MODULE_INFO = {
    "Module 0 - Pre-Flight Check": {
        "number": 0,
        "title": "Pre-Flight Check",
        "completion_msg": "Your AI tools are configured and you understand the boundaries of responsible use. You're cleared for takeoff.",
        "stats": [("Tools", "Configured"), ("Policies", "Understood"), ("Status", "Ready for Takeoff")],
    },
    "Module 1 - The Cognitive Shift": {
        "number": 1,
        "title": "The Cognitive Shift",
        "completion_msg": "You now understand how to work WITH the reasoning engine, not just talk AT it. The shift from search to collaboration starts here.",
        "stats": [("Mindset", "Shifted"), ("Engine", "Understood"), ("Collaboration", "Unlocked")],
    },
    "Module 2 - Model Selection": {
        "number": 2,
        "title": "Model Selection",
        "completion_msg": "You know when to deploy each AI model for maximum impact. The right tool for the right mission, every time.",
        "stats": [("Models", "Mastered"), ("Selection", "Strategic"), ("Efficiency", "Maximized")],
    },
    "Module 3 - Prompt Architecture": {
        "number": 3,
        "title": "Prompt Architecture",
        "completion_msg": "You can structure complex prompts that prevent context bleeding and produce consistent results. Architecture before improvisation.",
        "stats": [("Formats", "3 Mastered"), ("Components", "6 Standard"), ("Context Bleeding", "Eliminated")],
    },
    "Module 4 - Personal Projects & Folders": {
        "number": 4,
        "title": "Personal Projects & Folders",
        "completion_msg": "Your AI tools are now organized for mission efficiency. Projects and folders give your Squadron persistent memory.",
        "stats": [("Projects", "Organized"), ("Context", "Persistent"), ("Efficiency", "Elevated")],
    },
    "Module 5 - The Sensory System": {
        "number": 5,
        "title": "The Sensory System",
        "completion_msg": "You've connected Gemini as your Recon & Radar and Granola as your Flight Recorder. Your Squadron now has eyes and ears everywhere.",
        "stats": [("Recon", "Online"), ("Flight Recorder", "Active"), ("Intel", "Flowing")],
    },
    "Module 6 - Decision Hygiene": {
        "number": 6,
        "title": "Decision Hygiene",
        "completion_msg": "You've mastered Decision Hygiene. You now know how to extract honest analysis from AI systems designed to please you.",
        "stats": [("Techniques", "4 Learned"), ("Workflow", "1 Mastered"), ("Sycophancy", "Defeated")],
    },
    "Module 7 - The Hybrid Agent": {
        "number": 7,
        "title": "The Hybrid Agent",
        "completion_msg": "You can command your Squadron from anywhere — Mac, mobile or Google Docs. Platform boundaries no longer limit your workflows.",
        "stats": [("Platforms", "Connected"), ("Workflows", "Cross-Device"), ("Access", "Anywhere")],
    },
    "Module 9 - Systemizing Intelligence": {
        "number": 9,
        "title": "Systemizing Intelligence",
        "completion_msg": "Your Squadron can now operate as a coordinated unit. Shared projects and team collaboration multiply your AI impact.",
        "stats": [("Collaboration", "Enabled"), ("Knowledge", "Shared"), ("Impact", "Multiplied")],
    },
    "Module 10 - Agentic Data Analysis": {
        "number": 10,
        "title": "Agentic Data Analysis",
        "completion_msg": 'You\'ve mastered the "No Math" Rule. Let AI handle the calculations while you focus on the insights that drive decisions.',
        "stats": [("Analysis", "Automated"), ("Math", "Delegated"), ("Insights", "Amplified")],
    },
    "Module 11 - Code Execution": {
        "number": 11,
        "title": "Code Execution",
        "completion_msg": "Excel, PowerPoint and PDF creation are now on autopilot. You've unlocked AI-powered file generation without writing a single line of code.",
        "stats": [("File Types", "Mastered"), ("Code", "Zero Required"), ("Output", "Professional")],
    },
    "Module 12 - Future Frontiers": {
        "number": 12,
        "title": "Future Frontiers",
        "completion_msg": "You've explored what's coming next — agents, MCP and the evolving AI landscape. You're prepared for the frontier.",
        "stats": [("Agents", "Understood"), ("MCP", "Explored"), ("Future", "Ready")],
    },
    "Module 13 - Capstone & Governance": {
        "number": 13,
        "title": "Capstone & Governance",
        "completion_msg": "You've completed the capstone mission and established your governance framework. You are now a certified Squadron Leader.",
        "stats": [("Capstone", "Complete"), ("Governance", "Established"), ("Rank", "Squadron Leader")],
    },
    "Bonus - SARA": {
        "number": "B",
        "title": "SARA",
        "completion_msg": "Your mission-specific command center is built and operational. SARA is ready to support your strategic initiatives.",
        "stats": [("Command Center", "Built"), ("SARA", "Operational"), ("Missions", "Ready")],
    },
}


# ─── CSS to inject ────────────────────────────────────────────────────────────

LAB_CERT_CSS = """
        /* Lab Certification */
        .lab-certification {
            margin: 2rem 0;
            padding: 1.25rem 1.5rem;
            background: rgba(46, 212, 181, 0.08);
            border-radius: 12px;
            border: 1px solid rgba(46, 212, 181, 0.25);
        }
        .lab-certification label {
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            font-size: 1rem;
            line-height: 1.5;
        }
        .lab-certification input[type="checkbox"] {
            width: 20px;
            height: 20px;
            flex-shrink: 0;
            accent-color: #2ED4B5;
            cursor: pointer;
        }

        /* Lab Gate Modal */
        .lab-modal-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.55);
            z-index: 10000;
            align-items: center;
            justify-content: center;
        }
        .lab-modal-overlay.visible {
            display: flex;
        }
        .lab-modal {
            background: #fff;
            border-radius: 16px;
            padding: 2.5rem;
            max-width: 460px;
            margin: 1rem;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        .lab-modal h3 {
            margin: 0 0 0.75rem;
            color: #14203F;
            font-size: 1.25rem;
        }
        .lab-modal p {
            color: #4B5563;
            line-height: 1.6;
            margin: 0 0 1.5rem;
        }
        .lab-modal-buttons {
            display: flex;
            gap: 0.75rem;
            justify-content: center;
            flex-wrap: wrap;
        }
        .lab-modal-buttons button {
            padding: 0.7rem 1.5rem;
            border-radius: 8px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            border: none;
            transition: transform 0.15s, box-shadow 0.15s;
        }
        .lab-modal-buttons button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .lab-modal-btn-primary {
            background: #2ED4B5;
            color: #14203F;
        }
        .lab-modal-btn-secondary {
            background: #E5E7EB;
            color: #374151;
        }
"""

COMPLETION_CSS = """
        /* Completion Celebration Screen */
        .completion-hero {
            text-align: center;
            padding: 3rem 2rem;
        }
        .completion-icon {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: linear-gradient(135deg, #2ED4B5 0%, #1657A0 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 2rem;
            font-size: 3rem;
            color: #fff;
        }
        .completion-hero h1 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        .completion-hero > p {
            max-width: 540px;
            margin: 0 auto 1.5rem;
            line-height: 1.6;
            opacity: 0.9;
        }
        .completion-stats {
            display: flex;
            justify-content: center;
            gap: 3rem;
            margin: 2.5rem 0;
            flex-wrap: wrap;
        }
        .completion-stat {
            text-align: center;
        }
        .completion-stat-value {
            font-size: 1.6rem;
            font-weight: 700;
            color: #2ED4B5;
        }
        .completion-stat-label {
            font-size: 0.85rem;
            color: #6B7280;
            margin-top: 0.25rem;
        }
        .completion-footer {
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            opacity: 0.7;
            font-size: 0.9rem;
        }
        .completion-study-link {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.6rem 1.5rem;
            border-radius: 8px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            cursor: pointer;
            font-size: 0.9rem;
            transition: background 0.2s;
        }
        .completion-study-link:hover {
            background: rgba(255,255,255,0.15);
        }
"""


# ─── HTML Templates ───────────────────────────────────────────────────────────

LAB_CERT_HTML = """
                <div class="lab-certification">
                    <label>
                        <input type="checkbox" id="labCertifyCheckbox" onchange="labCertified = this.checked">
                        <span>I've completed the lab exercise</span>
                    </label>
                </div>
"""

LAB_MODAL_HTML = """
    <!-- Lab Certification Gate Modal -->
    <div class="lab-modal-overlay" id="labModal">
        <div class="lab-modal">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">&#129514;</div>
            <h3>Lab Exercise Recommended</h3>
            <p>The lab contains important hands-on practice and reinforcements that will help you succeed on the quiz. It's optional but highly recommended.</p>
            <div class="lab-modal-buttons">
                <button class="lab-modal-btn-primary" onclick="closeLabModal(); doNavigate('lab')">Take Me to the Lab</button>
                <button class="lab-modal-btn-secondary" onclick="closeLabModal(); quizAccessConfirmed = true; doNavigate('quiz')">Continue to Quiz</button>
            </div>
        </div>
    </div>
"""


def make_completion_html(info, screen_class):
    """Generate the completion screen HTML for a module."""
    tag = "section"
    cls = f'class="{screen_class}"' if screen_class else ""
    stats_html = ""
    for label, value in info["stats"]:
        stats_html += f"""
                        <div class="completion-stat">
                            <div class="completion-stat-value">{value}</div>
                            <div class="completion-stat-label">{label}</div>
                        </div>"""

    return f"""
            <!-- Completion Celebration Screen -->
            <{tag} {cls} id="complete">
                <div class="completion-hero">
                    <div class="completion-icon">&#10003;</div>
                    <h1>Module {info['number']} Complete!</h1>
                    <p>{info['completion_msg']}</p>

                    <div class="completion-stats">{stats_html}
                    </div>

                    <button class="completion-study-link" onclick="doNavigate('study-guide')">
                        &#128203; View Study Guide (Reference)
                    </button>

                    <p class="completion-footer">You've completed all required sections. Close this window or revisit any section from the sidebar.</p>
                </div>
            </{tag}>
"""


# ─── JS Templates ─────────────────────────────────────────────────────────────

LAB_GATE_JS = """
        // Lab certification gate
        var labCertified = false;
        var quizAccessConfirmed = false;

        function showLabModal() {
            document.getElementById('labModal').classList.add('visible');
        }
        function closeLabModal() {
            document.getElementById('labModal').classList.remove('visible');
        }
"""

COMPLETION_NAV_JS = """
            // Show completion button on pass
            if (passed) {
                var completeBtn = document.createElement('button');
                completeBtn.style.cssText = 'display:block; margin:1.5rem auto 0; padding:1rem 2.5rem; font-size:1.1rem; font-weight:700; border:none; border-radius:12px; cursor:pointer; background:linear-gradient(135deg,#2ED4B5,#1657A0); color:#fff; transition:transform 0.15s;';
                completeBtn.textContent = 'Module Complete \\u2192';
                completeBtn.onmouseover = function() { this.style.transform = 'translateY(-2px)'; };
                completeBtn.onmouseout = function() { this.style.transform = 'translateY(0)'; };
                completeBtn.onclick = function() { navigateTo('complete'); };
                var resultsEl = document.getElementById('quiz-results');
                if (resultsEl) resultsEl.appendChild(completeBtn);
            }
"""


# ─── Processing Functions ─────────────────────────────────────────────────────

def detect_conventions(content):
    """Detect the nav/screen conventions used in this module."""
    info = {}

    # Nav attribute: data-screen vs data-section
    if "data-screen=" in content:
        info["nav_attr"] = "data-screen"
        info["screen_class"] = "screen"
    elif "data-section=" in content:
        info["nav_attr"] = "data-section"
        info["screen_class"] = "content-section"
    else:
        info["nav_attr"] = None
        info["screen_class"] = "screen"

    # Array variable name
    m = re.search(r"const (screens|sections)\s*=\s*\[", content)
    info["array_name"] = m.group(1) if m else None

    # Quiz function name — the function containing setSCORMScore
    # Search backwards from setSCORMScore to find the enclosing function
    scorm_pos = content.find("setSCORMScore")
    if scorm_pos != -1:
        # Look backwards for the nearest function declaration
        preceding = content[:scorm_pos]
        func_matches = list(re.finditer(r"function\s+(\w+)\s*\(", preceding))
        info["quiz_func"] = func_matches[-1].group(1) if func_matches else None
    else:
        info["quiz_func"] = None

    # Has completion screen already?
    info["has_complete"] = 'id="complete"' in content

    # Has lab certification already?
    info["has_lab_cert"] = "labCertified" in content or "labCertifyCheckbox" in content

    # Has lab modal already?
    info["has_lab_modal"] = "labModal" in content

    return info


def inject_css(content):
    """Inject lab certification and completion CSS before </style>."""
    # Check what's already present
    needs_lab_css = ".lab-certification" not in content
    needs_completion_css = ".completion-hero" not in content

    if not needs_lab_css and not needs_completion_css:
        return content

    css_to_add = ""
    if needs_lab_css:
        css_to_add += LAB_CERT_CSS
    if needs_completion_css:
        css_to_add += COMPLETION_CSS

    # Insert before last </style>
    last_style = content.rfind("</style>")
    if last_style == -1:
        print("    WARNING: No </style> tag found")
        return content

    content = content[:last_style] + css_to_add + "\n    " + content[last_style:]
    return content


def inject_lab_certification(content, conv):
    """Add lab certification checkbox at the end of the lab section."""
    if conv["has_lab_cert"]:
        return content

    # Strategy: find the nav buttons div at the end of the lab section
    # which contains a navigateTo('quiz') call — insert cert checkbox before it
    #
    # Pattern varies:
    # - <div class="section-nav"> or <div class="nav-buttons"> before </section> of lab
    # - The lab section is id="lab"

    # Find the lab section
    lab_start = content.find('id="lab"')
    if lab_start == -1:
        print("    WARNING: No lab section found")
        return content

    # Find the closing </section> for the lab (first one after lab_start)
    # But we need to handle nested elements. Find the nav buttons area.
    # Look for the nav buttons div that contains navigateTo('quiz') AFTER lab_start
    quiz_nav_pattern = re.compile(
        r'([ \t]*<div\s+class="(?:section-nav|nav-buttons)">\s*(?:.*?)navigateTo\([\'"]quiz[\'"]\).*?</div>)',
        re.DOTALL
    )

    match = quiz_nav_pattern.search(content, lab_start)
    if match:
        insert_pos = match.start()
        # Check this is still within the lab section (before the next </section>)
        next_section_end = content.find("</section>", lab_start)
        if next_section_end == -1 or insert_pos < next_section_end:
            content = content[:insert_pos] + LAB_CERT_HTML + "\n" + content[insert_pos:]
            return content

    # Fallback: insert before the first </section> after lab_start
    next_section_end = content.find("</section>", lab_start)
    if next_section_end != -1:
        # Go back to find the nav buttons or just insert before </section>
        insert_pos = next_section_end
        # Try to insert before the nav-buttons div
        nav_div = content.rfind('<div class="nav-buttons">', lab_start, next_section_end)
        if nav_div == -1:
            nav_div = content.rfind('<div class="section-nav">', lab_start, next_section_end)
        if nav_div != -1:
            insert_pos = nav_div
        content = content[:insert_pos] + LAB_CERT_HTML + "\n" + content[insert_pos:]
    else:
        print("    WARNING: Could not find lab section end")

    return content


def inject_lab_modal(content):
    """Add the lab gate modal HTML before </main> or before </body>."""
    if "labModal" in content and "lab-modal-overlay" in content:
        return content

    # Insert before </main>
    main_end = content.rfind("</main>")
    if main_end != -1:
        content = content[:main_end] + LAB_MODAL_HTML + "\n    " + content[main_end:]
    else:
        # Fallback: before </body>
        body_end = content.rfind("</body>")
        if body_end != -1:
            content = content[:body_end] + LAB_MODAL_HTML + "\n" + content[body_end:]
        else:
            print("    WARNING: No </main> or </body> found for modal injection")
    return content


def inject_completion_screen(content, module_info, conv):
    """Add completion celebration screen before </main>."""
    if conv["has_complete"]:
        return content

    screen_class = conv["screen_class"]
    completion_html = make_completion_html(module_info, screen_class)

    # Insert before </main>
    main_end = content.rfind("</main>")
    if main_end != -1:
        content = content[:main_end] + completion_html + "\n    " + content[main_end:]
    else:
        print("    WARNING: No </main> found for completion screen injection")
    return content


def inject_lab_gate_js(content):
    """Add lab gate variables and modal functions to the script section."""
    if "labCertified" in content and "showLabModal" in content:
        return content

    # Find the first <script> tag that contains the navigateTo function
    # Insert the lab gate variables right after the opening <script>
    script_match = re.search(r"(<script>)\s*\n", content)
    if script_match:
        insert_pos = script_match.end()
        content = content[:insert_pos] + LAB_GATE_JS + "\n" + content[insert_pos:]
    else:
        # Try after last <script> tag
        last_script = content.rfind("<script>")
        if last_script != -1:
            insert_pos = last_script + len("<script>")
            content = content[:insert_pos] + "\n" + LAB_GATE_JS + content[insert_pos:]
        else:
            print("    WARNING: No <script> tag found for JS injection")
    return content


def modify_navigate_function(content, conv):
    """Wrap the navigateTo function with lab gate logic."""
    # Already modified?
    if "doNavigate" in content:
        return content

    # Strategy: rename the existing navigateTo to doNavigate, then create
    # a new navigateTo that gates quiz access.
    #
    # Find: function navigateTo(paramName)
    nav_func = re.search(r"function navigateTo\((\w+)\)", content)
    if not nav_func:
        print("    WARNING: navigateTo function not found")
        return content

    param_name = nav_func.group(1)

    # Replace the function declaration
    content = content.replace(
        f"function navigateTo({param_name})",
        f"function doNavigate({param_name})",
        1  # Only first occurrence
    )

    # Also replace any event listener references that call navigateTo directly
    # BUT we want external onclick="navigateTo(...)" to still work via the wrapper
    # The wrapper function:
    wrapper = f"""
        function navigateTo(target) {{
            if (target === 'quiz' && !labCertified && !quizAccessConfirmed) {{
                showLabModal();
                return;
            }}
            doNavigate(target);
        }}
"""

    # Insert the wrapper right after the doNavigate function definition
    # Find the end of the doNavigate function — tricky with regex due to nesting
    # Instead, insert the wrapper right after the doNavigate declaration line
    do_nav_pos = content.find(f"function doNavigate({param_name})")
    if do_nav_pos != -1:
        # Find the closing brace of doNavigate — scan for matching braces
        brace_start = content.find("{", do_nav_pos)
        if brace_start != -1:
            depth = 0
            i = brace_start
            while i < len(content):
                if content[i] == "{":
                    depth += 1
                elif content[i] == "}":
                    depth -= 1
                    if depth == 0:
                        # Insert wrapper after the closing brace
                        insert_pos = i + 1
                        content = content[:insert_pos] + "\n" + wrapper + content[insert_pos:]
                        break
                i += 1
    else:
        print("    WARNING: Could not find doNavigate for wrapper insertion")

    return content


def update_screens_array(content, conv):
    """Update the screens/sections array: add 'complete' if not present."""
    arr_name = conv["array_name"]
    if not arr_name:
        return content

    # Find the array declaration
    pattern = re.compile(
        rf"(const {arr_name}\s*=\s*\[)([^\]]+)(\])",
    )
    match = pattern.search(content)
    if not match:
        return content

    items_str = match.group(2)

    # Already has 'complete'?
    if "'complete'" in items_str or '"complete"' in items_str:
        # Just remove study-guide from the array (keep it navigable, not in progress)
        new_items = items_str.replace(", 'study-guide'", "").replace("'study-guide', ", "").replace(", \"study-guide\"", "").replace("\"study-guide\", ", "")
        if new_items != items_str:
            content = content[:match.start(2)] + new_items + content[match.end(2):]
        return content

    # Remove study-guide and add complete
    new_items = items_str
    # Remove study-guide
    new_items = re.sub(r",?\s*['\"]study-guide['\"]", "", new_items)
    # Remove trailing comma if any
    new_items = new_items.rstrip().rstrip(",")
    # Add complete
    new_items = new_items + ", 'complete'"

    content = content[:match.start(2)] + new_items + content[match.end(2):]
    return content


def fix_progress_for_study_guide(content, conv):
    """Ensure updateProgress doesn't break when viewing the study guide."""
    arr_name = conv["array_name"]
    if not arr_name:
        return content

    # If updateProgress exists, add a guard for -1 index (study guide not in array)
    if "function updateProgress" not in content:
        return content

    # Check if already guarded
    if "currentIndex === -1" in content or "indexOf" not in content:
        return content

    # Find the indexOf line in updateProgress and add a guard
    # Pattern: const/var/let currentIndex = screens.indexOf(...); or
    #          const activeIndex = sections.findIndex(...)
    # We need to add: if (currentIndex === -1) return;

    # Handle findIndex pattern
    find_idx = re.search(
        rf"(const|var|let)\s+(\w+)\s*=\s*{arr_name}\.(indexOf|findIndex)\(",
        content
    )
    if find_idx:
        var_name = find_idx.group(2)
        # Find the semicolon ending this line
        semi_pos = content.find(";", find_idx.end())
        if semi_pos != -1:
            # Insert guard after the semicolon
            guard = f"\n            if ({var_name} === -1) return;"
            content = content[:semi_pos + 1] + guard + content[semi_pos + 1:]

    return content


def inject_completion_button_in_quiz(content, conv):
    """Add the 'Module Complete' button injection into the quiz function."""
    quiz_func = conv["quiz_func"]
    if not quiz_func:
        return content

    # Already injected?
    if "Module Complete" in content:
        return content

    # Strategy: find the confetti block in the quiz function and inject
    # the completion button code right after the confetti block.
    # Or if no confetti, inject after the results display code.
    #
    # We look for the pattern: if (passed && typeof confetti
    # and inject after the closing of the confetti if-block

    # Find the quiz function
    func_start = content.find(f"function {quiz_func}")
    if func_start == -1:
        print(f"    WARNING: Quiz function {quiz_func} not found")
        return content

    # Find the popup close section (exists in most modules)
    # Pattern: if (window.opener !== null)
    popup_pattern = content.find("if (window.opener !== null)", func_start)

    if popup_pattern != -1:
        # Insert the completion button code before the popup close block
        content = content[:popup_pattern] + COMPLETION_NAV_JS + "\n" + content[popup_pattern:]
    else:
        # Fallback: find the confetti block end
        confetti_start = content.find("if (passed && typeof confetti", func_start)
        if confetti_start != -1:
            # Find the end of the confetti if block
            brace_pos = content.find("{", confetti_start)
            if brace_pos != -1:
                depth = 0
                i = brace_pos
                while i < len(content):
                    if content[i] == "{":
                        depth += 1
                    elif content[i] == "}":
                        depth -= 1
                        if depth == 0:
                            insert_pos = i + 1
                            content = content[:insert_pos] + "\n" + COMPLETION_NAV_JS + content[insert_pos:]
                            break
                    i += 1
        else:
            # Last resort: find the results display and insert after it
            results_display = content.find("resultsDiv.style.display", func_start)
            if results_display == -1:
                results_display = content.find("quiz-results", func_start)
            if results_display != -1:
                # Find next line end
                line_end = content.find("\n", results_display)
                if line_end != -1:
                    content = content[:line_end] + "\n" + COMPLETION_NAV_JS + content[line_end:]

    return content


def remove_study_guide_forward_buttons(content):
    """Remove or change 'View Study Guide' forward buttons in the quiz section."""
    # Find buttons that navigate to study-guide from the quiz section
    # These are in section-nav or nav-buttons divs after the quiz

    # Pattern 1: "View Study Guide →" or "View Study Guide" buttons
    # Replace navigateTo('study-guide') with navigateTo('complete') in quiz section nav
    quiz_start = content.find('id="quiz"')
    if quiz_start == -1:
        return content

    study_guide_start = content.find('id="study-guide"')
    if study_guide_start == -1:
        study_guide_start = len(content)

    # Only modify between quiz section and study-guide section
    quiz_section = content[quiz_start:study_guide_start]

    # Replace forward navigation buttons to study-guide
    modified = quiz_section
    modified = re.sub(
        r"""onclick="navigateTo\(['"]study-guide['"]\)"([^>]*)>([^<]*Study Guide[^<]*)""",
        r"""onclick="navigateTo('complete')"\1>Module Complete →""",
        modified
    )

    if modified != quiz_section:
        content = content[:quiz_start] + modified + content[study_guide_start:]

    return content


def add_complete_nav_item(content, conv):
    """Add a 'Complete' nav item to the sidebar if not present."""
    if conv["has_complete"]:
        return content

    nav_attr = conv["nav_attr"]
    if not nav_attr:
        return content

    # Find the study-guide nav item and add complete after it
    study_nav = re.search(
        rf'<div class="nav-item"[^>]*{nav_attr}="study-guide"[^>]*>.*?</div>',
        content,
        re.DOTALL
    )

    if study_nav:
        # Insert complete nav item after study-guide, in same nav-section
        complete_nav = f"""
                <div class="nav-item" {nav_attr}="complete">
                    <div class="nav-icon">&#127942;</div>
                    <span class="nav-label">Complete</span>
                </div>"""

        insert_pos = study_nav.end()
        content = content[:insert_pos] + complete_nav + content[insert_pos:]

    return content


def process_module(folder_name, filepath):
    """Apply all completion flow changes to a single module."""
    if not os.path.exists(filepath):
        print(f"  SKIP: {filepath} (not found)")
        return False

    info = MODULE_INFO.get(folder_name)
    if not info:
        print(f"  SKIP: {folder_name} (no module info)")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Detect conventions
    conv = detect_conventions(content)
    print(f"  Conventions: nav={conv['nav_attr']}, array={conv['array_name']}, "
          f"quiz={conv['quiz_func']}, has_complete={conv['has_complete']}, "
          f"has_lab_cert={conv['has_lab_cert']}")

    # 1. Inject CSS
    content = inject_css(content)

    # 2. Lab certification checkbox
    content = inject_lab_certification(content, conv)

    # 3. Lab gate modal HTML
    content = inject_lab_modal(content)

    # 4. Completion screen HTML
    content = inject_completion_screen(content, info, conv)

    # 5. Lab gate JS (variables + modal functions)
    content = inject_lab_gate_js(content)

    # 6. Modify navigateTo → doNavigate with gate wrapper
    content = modify_navigate_function(content, conv)

    # 7. Update screens/sections array (add 'complete', remove 'study-guide')
    content = update_screens_array(content, conv)

    # 8. Fix progress calculation for study guide
    content = fix_progress_for_study_guide(content, conv)

    # 9. Inject completion button in quiz results
    content = inject_completion_button_in_quiz(content, conv)

    # 10. Change quiz "View Study Guide" buttons to "Module Complete"
    content = remove_study_guide_forward_buttons(content)

    # 11. Add Complete nav item to sidebar
    content = add_complete_nav_item(content, conv)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  UPDATED: {folder_name}")
        return True
    else:
        print(f"  NO CHANGE: {folder_name}")
        return False


def main():
    print("=" * 60)
    print("  Updating Module Completion Flow")
    print("  Changes: Lab cert + Quiz gate + Completion screen")
    print("=" * 60)
    print()

    updated = 0
    total = 0

    for folder_name in sorted(MODULE_INFO.keys()):
        filepath = os.path.join(BASE_DIR, folder_name, "index.html")
        print(f"\n[{folder_name}]")
        total += 1
        if process_module(folder_name, filepath):
            updated += 1

    print("\n" + "=" * 60)
    print(f"  Done: {updated}/{total} modules updated")
    print(f"  Next: Re-run create_packages.sh to update SCORM packages")
    print("=" * 60)


if __name__ == "__main__":
    main()
