# Build SCORM Package 

Create a SCORM 1.2 package from the course modules for import into an LLM.

## Package Structure (Multi-SCO)

Each module is a separate SCO (Sharable Content Object) for independent tracking:

```
Squadron_Leader_Full_Course.zip
├── imsmanifest.xml
├── scorm_api.js
├── module_0/index.html
├── module_1/index.html
...
└── module_13/index.html
```

## Step 1: Create Package Directory

```bash
SCORM_DIR="/Users/dglickman@bgrove.com/AI course/SCORM_Packages/full_course"
rm -rf "$SCORM_DIR"
mkdir -p "$SCORM_DIR"
```

## Step 2: Create scorm_api.js

Write to `$SCORM_DIR/scorm_api.js`:

```javascript
var API = null;
var findAPITries = 0;
var scormInitialized = false;

function findAPI(win) {
    while ((win.API == null) && (win.parent != null) && (win.parent != win)) {
        findAPITries++;
        if (findAPITries > 500) return null;
        win = win.parent;
    }
    return win.API;
}

function getAPI() {
    var theAPI = findAPI(window);
    if ((theAPI == null) && (window.opener != null) && (typeof(window.opener) != "undefined")) {
        theAPI = findAPI(window.opener);
    }
    return theAPI;
}

function initializeSCORM() {
    API = getAPI();
    if (API != null) {
        var result = API.LMSInitialize("");
        if (result == "true") {
            scormInitialized = true;
            var status = API.LMSGetValue("cmi.core.lesson_status");
            if (status == "not attempted" || status == "") {
                API.LMSSetValue("cmi.core.lesson_status", "incomplete");
                API.LMSCommit("");
            }
            return true;
        }
    }
    return false;
}

function setSCORMValue(key, value) {
    if (API != null && scormInitialized) {
        API.LMSSetValue(key, value);
        return true;
    }
    return false;
}

function setSCORMStatus(status) {
    if (setSCORMValue("cmi.core.lesson_status", status)) {
        API.LMSCommit("");
    }
}

function setSCORMScore(score) {
    if (API != null && scormInitialized) {
        setSCORMValue("cmi.core.score.raw", score.toString());
        setSCORMValue("cmi.core.score.min", "0");
        setSCORMValue("cmi.core.score.max", "100");
        API.LMSCommit("");
    }
}

function setSCORMPassed(passed) {
    setSCORMStatus(passed ? "passed" : "failed");
}

function finishSCORM() {
    if (API != null && scormInitialized) {
        API.LMSCommit("");
        API.LMSFinish("");
    }
}

window.addEventListener('load', function() { initializeSCORM(); });
window.addEventListener('beforeunload', function() { finishSCORM(); });
```

## Step 3: Copy Module HTML Files

For each module (0-13):
1. Create folder: `$SCORM_DIR/module_X/`
2. Copy the full index.html from the source module
3. Inject SCORM script reference after `<head>`:

```bash
sed 's|<head>|<head>\n    <script src="../scorm_api.js"></script>|' \
    "$SOURCE_MODULE/index.html" > "$SCORM_DIR/module_X/index.html"
```

**IMPORTANT:** Copy the FULL index.html - do not create abbreviated versions. Each module contains all sections (Welcome, Video, Lessons, Flashcards, Lab, Quiz, Study Guide).

## Step 4: Add SCORM Completion to Quiz Functions

Each module's quiz must report score and status when completed. Find the quiz completion function and add:

```javascript
// SCORM: Report score and completion
const scorePercent = Math.round((correct / total) * 100);
if (typeof setSCORMScore === 'function') {
    setSCORMScore(scorePercent);
}
if (typeof setSCORMStatus === 'function') {
    setSCORMStatus(scorePercent >= 70 ? 'passed' : 'failed');
}
```

### Quiz Function Patterns to Look For

| Pattern | Function Name | Where to Add SCORM |
|---------|--------------|-------------------|
| Progressive quiz | `showResults()` | After inline results display logic |
| All-at-once | `checkQuiz()` | After inline results display logic |
| Per-question | `check-answer-btn` click | When all questions answered |

Search for these patterns:
```bash
grep -n "showResults\|checkQuiz\|quizComplete" module_X/index.html
```

## Step 5: Create imsmanifest.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="ActivTrak_Squadron_Leader" version="1.0"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                              http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd
                              http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">

  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>

  <organizations default="org1">
    <organization identifier="org1">
      <title>Solo Pilot to Squadron Leader: Practical AI for Knowledge Work</title>

      <item identifier="item0" identifierref="res0" isvisible="true">
        <title>Module 0: Pre-Flight Check</title>
      </item>
      <!-- Repeat for modules 1-13 -->

    </organization>
  </organizations>

  <resources>
    <resource identifier="res0" type="webcontent" adlcp:scormtype="sco" href="module_0/index.html">
      <file href="module_0/index.html"/>
      <file href="scorm_api.js"/>
    </resource>
    <!-- Repeat for modules 1-13 -->
  </resources>

</manifest>
```

**CRITICAL: Escape ampersands** in module titles. `&` must become `&amp;` (e.g., "Projects &amp; Folders"). Validate with `xmllint --noout`.

## Step 6: Validate and Package

```bash
# Validate XML
xmllint --noout imsmanifest.xml

# Create zip (ALWAYS delete old zip first - updating in-place keeps stale files)
rm -f "../output/Squadron_Leader_Full_Course.zip"
cd "$SCORM_DIR"
zip -r "../output/Squadron_Leader_Full_Course.zip" imsmanifest.xml scorm_api.js module_*/
```

---

## Pre-Packaging Quality Gate

**Run these checks on EVERY source index.html BEFORE packaging.** Do not package a module that fails any check.

### Required `<head>` Scripts

Every module must have BOTH scripts in `<head>`:
```html
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
```
The SCORM script is injected during packaging (Step 3). The confetti CDN must already exist in the source file.

```bash
# Verify confetti library
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    if grep -q "canvas-confetti" "$dir/index.html" 2>/dev/null; then
        echo "Module $i: confetti CDN OK"
    else
        echo "Module $i: MISSING canvas-confetti CDN"
    fi
done
```

### Required ActivTrak Brand CSS Variables

Every module's `:root` block must define these brand variables:
```css
:root {
    /* ActivTrak Brand Colors */
    --dark-navy: #14203F;
    --medium-navy: #19316A;
    --blue: #1657A0;
    --teal: #2ED4B5;
    --yellow: #FFC83B;
    --white: #FFFFFF;
    /* ...additional legacy/module-specific vars... */
}
```

The header gradient uses `var(--dark-navy)` and `var(--medium-navy)`. If these are missing, the header renders with no background.

```bash
# Verify brand CSS variables
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    missing=""
    grep -q "\-\-dark-navy" "$dir/index.html" 2>/dev/null || missing="$missing --dark-navy"
    grep -q "\-\-medium-navy" "$dir/index.html" 2>/dev/null || missing="$missing --medium-navy"
    grep -q "\-\-yellow" "$dir/index.html" 2>/dev/null || missing="$missing --yellow"
    if [ -z "$missing" ]; then
        echo "Module $i: brand CSS OK"
    else
        echo "Module $i: MISSING CSS vars:$missing"
    fi
done
```

### Quiz UX Requirements

Quizzes MUST use inline results display. **NEVER use `alert()` for quiz scores** — it blocks confetti animation and is a UX dead-end.

Required quiz completion pattern:
1. **Inline results panel** (`<div id="quiz-results">`) with score, pass/fail message
2. **Retake button** calling `resetQuiz()` that clears selections and re-shows submit button
3. **Hide submit button** after submission (`display: none`)
4. **Scroll to results** (`resultsDiv.scrollIntoView({ behavior: 'smooth' })`)

```bash
# Verify quiz UX (no alert() for scores, has inline results)
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    file="$dir/index.html"
    [ ! -f "$file" ] && continue
    issues=""
    # Check for alert() in quiz functions (false positives possible, review manually)
    if grep -q 'alert(`You got' "$file" 2>/dev/null || grep -q "alert('You got" "$file" 2>/dev/null; then
        issues="$issues [USES ALERT FOR SCORE]"
    fi
    grep -q "quiz-results" "$file" 2>/dev/null || issues="$issues [NO INLINE RESULTS PANEL]"
    grep -q "resetQuiz" "$file" 2>/dev/null || issues="$issues [NO RETAKE FUNCTION]"
    if [ -z "$issues" ]; then
        echo "Module $i: quiz UX OK"
    else
        echo "Module $i:$issues"
    fi
done
```

### Confetti and Completion

Every module must have:
1. **Confetti celebration** on quiz pass (3 bursts with ActivTrak brand colors)
2. **Popup window close** behavior (`window.opener` check)
3. **No dead buttons** on completion screen (no `alert('Proceeding to...')` fake CTAs)

```bash
# Verify confetti + completion
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    file="$dir/index.html"
    [ ! -f "$file" ] && continue
    confetti_count=$(grep -c "particleCount" "$file" 2>/dev/null)
    has_opener=$(grep -c "window.opener" "$file" 2>/dev/null)
    echo "Module $i: confetti bursts=$confetti_count, popup_close=$has_opener"
done
```

### Video Format

All video files must be .mp4. Browsers in SCORM/LMS context do not support .mov.

```bash
# Check for .mov references (must be .mp4)
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    if grep -q '\.mov' "$dir/index.html" 2>/dev/null; then
        echo "Module $i: WARNING - references .mov file (convert to .mp4)"
    fi
done
```

### Unused Video Files

If a `.mp4` file exists in the module folder but is NOT referenced in the HTML,
it will be packaged as dead weight (the source is typically a Google Drive iframe
embed instead). This can inflate zip size by GB and cause upload failures.

**Real incident:** Module 3 shipped a 1.2GB zip because two unused `.mp4` files
were auto-included by `create_packages.sh`. The HTML referenced a Google Drive
iframe, not the local files. Fixed zip was 23KB.

```bash
# Detect unused .mp4 files (packaged but never played)
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    for mp4 in "$dir"/*.mp4; do
        [ ! -f "$mp4" ] && continue
        name=$(basename "$mp4")
        if ! grep -q "$name" "$dir/index.html"; then
            size=$(ls -lh "$mp4" | awk '{print $5}')
            echo "Module $i: UNUSED video '$name' ($size) - exclude from package"
        fi
    done
done
```

If a video is flagged unused, either:
- Move it out of the module folder (recommended): `mv "$dir/video.mp4" _unused_videos/`
- OR update `create_packages.sh` to only copy referenced videos

### JavaScript Syntax Validation

**Every module's inline `<script>` block must parse without errors.** A single
missing brace or bad reference silently breaks the entire module: no buttons
respond, no navigation works, no quiz submits. Nothing shows in the browser
console as an obvious error either — the script just fails at load.

**Real incidents from prior sessions:**
- Missing `}` after `if (typeof setSCORMStatus === 'function') { ... }` block
  trapped confetti and completion code inside, making quiz completion silent
- `const passed = scorePercent >= 70;` referenced undefined variable after
  another `passed` was declared in outer scope
- Near-pass encouragement code injected into `nextQuestion()` instead of
  `showResults()` — broke the "See Results" button

```bash
# Extract and validate each module's script block with node --check
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    file="$dir/index.html"
    [ ! -f "$file" ] && continue
    python3 -c "
content = open('$file').read()
s = content.rfind('<script>')
e = content.find('</script>', s)
if s != -1 and e != -1:
    open('/tmp/_m${i}.js', 'w').write(content[s+8:e])
"
    if [ -f /tmp/_m${i}.js ]; then
        if node --check /tmp/_m${i}.js 2>/dev/null; then
            echo "Module $i: JS syntax OK"
        else
            echo "Module $i: JS SYNTAX ERROR"
            node --check /tmp/_m${i}.js 2>&1 | head -3 | sed 's/^/    /'
        fi
    fi
done
```

**Any module with a syntax error must be fixed before packaging** — otherwise
the SCO is DOA in the LMS. Common fixes: search for `setSCORMStatus` and verify
the `if` block closes with `}` before the next comment. Check for `const`
redeclarations across nested blocks.

### Element ID Reference Integrity

JavaScript code like `document.getElementById('quiz-results')` will silently
return `null` if the target element doesn't exist. Dynamic code paths (adding
buttons, updating results) then silently fail when calling `.appendChild` or
`.style` on null.

**Real incident:** Our `apply_ux_fixes.py` script injected
`document.getElementById('quiz-results')` into every module's quiz function,
but modules use different IDs: `quizScore`, `quizResults`, `quiz-results`,
`quiz`, or nothing at all. In modules with no matching element, the "Module
Complete" button was never added to the DOM on quiz pass.

```bash
# Verify every getElementById('X') reference points to an existing id="X"
for i in {0..13}; do
    dir=$(ls -d "Module $i - "* 2>/dev/null)
    [ -z "$dir" ] && continue
    file="$dir/index.html"
    [ ! -f "$file" ] && continue
    grep -oE "getElementById\('[^']+'\)" "$file" | sort -u | while read ref; do
        target=$(echo "$ref" | sed -E "s/getElementById\('([^']+)'\)/\1/")
        if ! grep -q "id=\"$target\"" "$file"; then
            echo "Module $i: getElementById('$target') but no id=\"$target\" exists"
        fi
    done
done
```

This check has rare false positives (e.g., if an element is created
dynamically) but those are easy to verify manually. Most hits are real bugs.

### Package Size

Reach 360 rejects packages over ~200MB. If a module includes video, verify compressed size:
```bash
ls -lh SCORM_Packages/output/*.zip | awk '{print $5, $9}'
```
If over 200MB, compress video with: `/opt/homebrew/bin/ffmpeg -i input.mp4 -c:v libx264 -crf 28 -preset slow -c:a aac -b:a 128k output.mp4`

---

## Full Verification Checklist

Before packaging, verify:

- [ ] All 14 modules (0-13) copied with full content
- [ ] Each module has `<script src="../scorm_api.js">` after `<head>`
- [ ] Each module has canvas-confetti CDN in `<head>`
- [ ] Each module's `:root` defines `--dark-navy`, `--medium-navy`, `--yellow`
- [ ] Each module's quiz function calls `setSCORMScore()` and `setSCORMStatus()`
- [ ] Each module uses inline results panel (NOT `alert()`) for quiz scores
- [ ] Each module has `resetQuiz()` function for retake
- [ ] Each module has confetti celebration (3 bursts with brand colors)
- [ ] Each module has `window.opener` popup close behavior
- [ ] No completion screen buttons use `alert()` as fake navigation
- [ ] All video references use .mp4 (not .mov)
- [ ] Manifest has 14 items and 14 resources
- [ ] XML validates with `xmllint --noout`
- [ ] No `&` in manifest XML (must be `&amp;`)
- [ ] Final zip created fresh (old zip deleted first)
- [ ] Package size under 200MB

```bash
# Combined quick verification
for i in {0..13}; do
    file="module_$i/index.html"
    [ ! -f "$file" ] && echo "Module $i: FILE MISSING" && continue
    issues=""
    grep -q "setSCORMScore" "$file" || issues="$issues [NO SCORM]"
    grep -q "particleCount" "$file" || issues="$issues [NO CONFETTI]"
    grep -q "canvas-confetti" "$file" || issues="$issues [NO CONFETTI CDN]"
    grep -q "quiz-results" "$file" || issues="$issues [NO INLINE RESULTS]"
    grep -q "window.opener" "$file" || issues="$issues [NO POPUP CLOSE]"
    if [ -z "$issues" ]; then
        echo "Module $i: ALL OK"
    else
        echo "Module $i:$issues"
    fi
done
```

## Reach 360 Import

1. Go to Reach 360 > Manage > Courses > Add Courses
2. Select "Import course"
3. Upload the zip file
4. Wait for processing
5. Course appears with 14 lessons (one per module)

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| "Unable to read imsmanifest.xml" | Invalid XML | Run `xmllint --noout` to find errors |
| `xmlParseEntityRef: no name` | Unescaped `&` in manifest | Replace `&` with `&amp;` in title text |
| Modules merged into one | Single-SCO manifest | Use multi-SCO with separate items/resources |
| Quiz doesn't report completion | Missing SCORM calls | Add setSCORMScore/setSCORMStatus to quiz function |
| Score not showing | Wrong function patched | Find the actual quiz completion function |
| Confetti doesn't fire | canvas-confetti CDN missing from `<head>` | Add `<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>` |
| Header has no background | `--dark-navy`/`--medium-navy` CSS vars undefined | Add brand variables to `:root` block |
| Quiz score shows as browser popup | Uses `alert()` instead of inline display | Replace with `#quiz-results` div pattern |
| Old video still in zip | Updated zip in-place instead of fresh | Always `rm` old zip before creating new one |
| S3 AccessDenied on Reach 360 | Package too large (>200MB) | Compress video with ffmpeg CRF 28 |
| Video won't play in LMS | .mov format unsupported | Convert to .mp4 with ffmpeg |

## Pass Threshold

Default: 70% to pass. To change, modify this line in each module:
```javascript
setSCORMStatus(scorePercent >= 70 ? 'passed' : 'failed');
```

$ARGUMENTS
