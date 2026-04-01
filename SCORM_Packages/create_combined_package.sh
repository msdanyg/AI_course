#!/bin/bash

# Combined SCORM Package Creator for Solo Pilot to Squadron Leader Course
# Creates a single SCORM 1.2 package with all 14 modules as separate SCOs

COURSE_DIR="/Users/dglickman@bgrove.com/AI course"
SCORM_DIR="$COURSE_DIR/SCORM_Packages"
OUTPUT_DIR="$SCORM_DIR/output"
COMBINED_DIR="$SCORM_DIR/combined_course"

# Create combined course directory
rm -rf "$COMBINED_DIR"
mkdir -p "$COMBINED_DIR"

# Module definitions
declare -a MODULES=(
    "0:Pre-Flight Check:Setup, Policy & Boundaries"
    "1:The Cognitive Shift:Understanding the Reasoning Engine"
    "2:Model Selection:The Thinking Protocol"
    "3:Prompt Architecture:Advanced Prompt Architecture (XML)"
    "4:Personal Projects & Folders:Claude Projects and ChatGPT Folders"
    "5:The Sensory System:Gemini & Granola"
    "6:Decision Hygiene:Beating Sycophancy"
    "7:The Hybrid Agent:Mac, Mobile & Docs"
    "8:Introduction to Skills:Building Reusable Prompt Templates"
    "9:Systemizing Intelligence:Team Collaboration and Shared Projects"
    "10:Agentic Data Analysis:The No Math Rule"
    "11:Code Execution:File Creation (Excel, PPT, PDF)"
    "12:Future Frontiers:Agents & MCP"
    "13:Capstone & Governance:Accountability & Certification"
)

# Copy shared SCORM API
cp "$SCORM_DIR/scorm_api.js" "$COMBINED_DIR/"

# Start building manifest
cat > "$COMBINED_DIR/imsmanifest.xml" << 'MANIFEST_HEAD'
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="com.activtrak.squadron-leader-course" version="1.0"
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

  <organizations default="ORG-001">
    <organization identifier="ORG-001">
      <title>Solo Pilot to Squadron Leader: Practical AI for Knowledge Work</title>
MANIFEST_HEAD

# Build items and resources sections
ITEMS=""
RESOURCES=""

for module_def in "${MODULES[@]}"; do
    IFS=':' read -r num title subtitle <<< "$module_def"

    # Find the module folder
    module_folder=$(find "$COURSE_DIR" -maxdepth 1 -type d -name "Module ${num} -*" | head -1)

    if [ -z "$module_folder" ] || [ ! -f "$module_folder/index.html" ]; then
        echo "Warning: Module $num not found or missing index.html, skipping..."
        continue
    fi

    echo "Adding Module $num: $title..."

    # Create module subdirectory
    module_dir="module_${num}"
    mkdir -p "$COMBINED_DIR/$module_dir"

    # Copy and modify index.html to include SCORM
    sed 's|<head>|<head>\n    <script src="../scorm_api.js"></script>|' "$module_folder/index.html" > "$COMBINED_DIR/$module_dir/index.html"

    # Add item to manifest
    ITEMS="${ITEMS}
      <item identifier=\"ITEM-${num}\" identifierref=\"RES-${num}\" isvisible=\"true\">
        <title>Module ${num}: ${title}</title>
      </item>"

    # Add resource to manifest
    RESOURCES="${RESOURCES}
    <resource identifier=\"RES-${num}\" type=\"webcontent\" adlcp:scormtype=\"sco\" href=\"${module_dir}/index.html\">
      <file href=\"${module_dir}/index.html\"/>
      <file href=\"scorm_api.js\"/>
    </resource>"
done

# Complete the manifest
cat >> "$COMBINED_DIR/imsmanifest.xml" << MANIFEST_ITEMS
${ITEMS}
    </organization>
  </organizations>

  <resources>${RESOURCES}
  </resources>

</manifest>
MANIFEST_ITEMS

# Create the combined zip
echo ""
echo "Creating combined SCORM package..."
(cd "$COMBINED_DIR" && zip -r "$OUTPUT_DIR/Squadron_Leader_Complete_Course.zip" *)

echo ""
echo "====================================="
echo "Combined SCORM Package created:"
echo "$OUTPUT_DIR/Squadron_Leader_Complete_Course.zip"
echo "====================================="
ls -lh "$OUTPUT_DIR/Squadron_Leader_Complete_Course.zip"

# Show package contents
echo ""
echo "Package contents:"
unzip -l "$OUTPUT_DIR/Squadron_Leader_Complete_Course.zip"
