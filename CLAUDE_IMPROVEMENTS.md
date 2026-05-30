# Suggested CLAUDE.md Improvements

Based on recent work (Module 4 button improvements and SCORM packaging), here are recommended additions to CLAUDE.md:

---

## Section to Add: "Building Individual SCORM Packages"

Add this after the "SCORM Packaging" section:

```markdown
## Building Individual Module SCORM Packages

To build a single module package (recommended after module updates):

```bash
# Method 1: Manual build for single module
SCORM_DIR="SCORM_Packages/temp_module_X"
rm -rf "$SCORM_DIR"
mkdir -p "$SCORM_DIR"

# Copy files
cp "SCORM_Packages/scorm_api.js" "$SCORM_DIR/"
cp "Module X - Title/index.html" "$SCORM_DIR/"

# Create manifest (see template below)
# Then zip
cd "$SCORM_DIR" && zip -r "../output/Module_X_Title.zip" .

# Clean up
rm -rf "$SCORM_DIR"
```

# Method 2: Use `/build-scorm X` skill for automated building
```

**CRITICAL: XML Escaping in Manifests**
- Ampersands MUST be escaped: `&` → `&amp;`
- Common in titles like "Projects & Folders"
- Validate manifest before packaging: `xmllint --noout imsmanifest.xml`

**Manifest template for individual module:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="com.activtrak.squadron-leader.module-X" version="1.0"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG-001">
    <organization identifier="ORG-001">
      <title>Module X: Title</title>
      <item identifier="ITEM-001" identifierref="RES-001" isvisible="true">
        <title>Module X: Title - Subtitle</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-001" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
      <file href="scorm_api.js"/>
      <!-- Add if video exists: <file href="moduleX_video.mp4"/> -->
    </resource>
  </resources>
</manifest>
```
```

---

## Section to Add: "Modifying Module HTML Files"

Add this after "Module index.html Architecture":

```markdown
## Modifying Module HTML Files

When updating existing module HTML (UI improvements, content fixes):

**1. Preserve SCORM Integration:**
- Ensure `<script src="scorm_api.js"></script>` remains in `<head>` (typically line 6)
- Don't modify quiz completion logic that calls `setSCORMScore()` and `setSCORMStatus()`
- Test quiz locally to verify alerts and results display still work

**2. ActivTrak Brand Compliance:**
- Use teal (#2ED4B5) for CTA buttons and interactive elements
- Maintain Century Gothic font family
- Keep color variables from `:root` CSS section
- Run `python update_branding.py` after bulk HTML changes

**3. Common UI Patterns:**

**Button styling (replacing `<details>` elements):**
```javascript
// Add to <script> section
function toggleExample(id) {
    const element = document.getElementById(id);
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
}
```

```html
<!-- Replace <details> with styled button -->
<button onclick="toggleExample('example1')"
        style="margin-top: 30px; padding: 12px 24px; background-color: #2ED4B5;
               color: #14203F; border: none; border-radius: 6px; font-weight: bold;
               cursor: pointer; font-size: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    💡 Button Text
</button>
<div id="example1" style="display: none; margin-top: 15px; padding: 20px;
                          background-color: #f5f5f5; border-left: 4px solid #2ED4B5;">
    Content here
</div>
```

**4. After Modifications:**
- Rebuild SCORM package: `/build-scorm X` or manual build (see above)
- Validate manifest XML: `xmllint --noout imsmanifest.xml`
- Verify SCORM integration: `grep -c "setSCORMScore\|setSCORMStatus" index.html` (should be ≥ 4)
```

---

## Section to Add: "SCORM Package Verification Checklist"

Add this after "Verify SCORM integration" section:

```markdown
## SCORM Package Verification Checklist

Before uploading to Articulate Reach 360:

```bash
# 1. Validate manifest XML (CRITICAL)
xmllint --noout SCORM_Packages/temp_module_X/imsmanifest.xml
# Should output: (nothing) or "✓ XML is valid"
# Errors indicate XML syntax issues (often unescaped & characters)

# 2. Verify SCORM script reference
grep -n "scorm_api.js" "Module X - Title/index.html" | head -1
# Should show line ~6: <script src="scorm_api.js"></script>

# 3. Count SCORM function calls in quiz
grep -c "setSCORMScore\|setSCORMStatus" "Module X - Title/index.html"
# Should return: 4 (two functions called twice each)

# 4. List package contents
unzip -l "SCORM_Packages/output/Module_X_Title.zip"
# Should show: imsmanifest.xml, index.html, scorm_api.js, [optional: video.mp4]

# 5. Check package size
ls -lh "SCORM_Packages/output/Module_X_Title.zip"
# Without video: ~40-50KB
# With video: ~600-700MB (depending on video length)
```

**Common Issues:**

| Issue | Cause | Fix |
|-------|-------|-----|
| `parser error: xmlParseEntityRef: no name` | Unescaped `&` in manifest | Replace `&` with `&amp;` in XML |
| Quiz doesn't report completion | Missing SCORM calls | Add `setSCORMScore(score)` and `setSCORMStatus(status)` to quiz completion |
| LMS rejects package | Invalid XML structure | Run `xmllint --noout` to find syntax errors |
| Video doesn't play | .mov format used | Convert to .mp4: `ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4` |
| Package missing video | Video file not in manifest | Add `<file href="moduleX_video.mp4"/>` to resources section |
```

---

## Section to Add: "Video File Management"

Add this after "Common Commands":

```markdown
## Video File Management

**Storage Location:**
- Source videos (typically .mov): `Module X - Title/` folder
- Converted videos (.mp4): Same folder, renamed with `_video.mp4` suffix
- Example: `module4_video.mp4`, `Modele 0 video.mp4`

**Video Requirements for SCORM:**
- Format: MUST be .mp4 (H.264 video, AAC audio)
- Browsers don't support .mov in HTML5 `<video>` tags
- Max recommended size: 700MB (LMS upload limits vary)

**Conversion Command:**
```bash
cd "Module X - Title"
/opt/homebrew/bin/ffmpeg -i "source_video.mov" -c:v libx264 -c:a aac "moduleX_video.mp4"
```

**Video in SCORM Packages:**
- Automatically included if found in module folder (by `create_packages.sh`)
- Must be referenced in manifest: `<file href="moduleX_video.mp4"/>`
- Significantly increases package size (600-700MB typical)
- Optional: Can build packages without video for faster LMS testing
```

---

## Modification to "Common Commands" Section

Replace the video conversion line with:

```bash
# Convert video from .mov to .mp4 (required for SCORM)
# Must use H.264 codec and AAC audio for browser compatibility
cd "Module X - Title"
/opt/homebrew/bin/ffmpeg -i "source_video.mov" -c:v libx264 -c:a aac "moduleX_video.mp4"

# Quick quality check (should show H.264/AAC)
ffprobe "moduleX_video.mp4" 2>&1 | grep -E "Video:|Audio:"
```
```

---

## Priority Rankings

**High Priority (Add immediately):**
1. XML Escaping warning (CRITICAL for SCORM compliance)
2. SCORM Package Verification Checklist
3. Individual module building instructions

**Medium Priority (Nice to have):**
4. Modifying Module HTML Files section
5. Video File Management details

**Low Priority (Optional):**
6. Expanded troubleshooting table
