#!/bin/bash

# SCORM Package Creator for Solo Pilot to Squadron Leader Course
# Creates SCORM 1.2 packages for Articulate Reach 360

COURSE_DIR="/Users/dglickman@bgrove.com/AI course"
SCORM_DIR="$COURSE_DIR/SCORM_Packages"
OUTPUT_DIR="$SCORM_DIR/output"

# Create output directory
mkdir -p "$OUTPUT_DIR"

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

# Function to create manifest
create_manifest() {
    local module_num=$1
    local title=$2
    local subtitle=$3
    local output_file=$4
    local video_file=$5

    cat > "$output_file" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="com.activtrak.squadron-leader.module-${module_num}" version="1.0"
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
      <title>Module ${module_num}: ${title}</title>
      <item identifier="ITEM-001" identifierref="RES-001" isvisible="true">
        <title>Module ${module_num}: ${title} - ${subtitle}</title>
      </item>
    </organization>
  </organizations>

  <resources>
    <resource identifier="RES-001" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
      <file href="scorm_api.js"/>
EOF

    # Add video file if it exists
    if [ -n "$video_file" ]; then
        echo "      <file href=\"$video_file\"/>" >> "$output_file"
    fi

    cat >> "$output_file" << EOF
    </resource>
  </resources>

</manifest>
EOF
}

# Process each module
for module_def in "${MODULES[@]}"; do
    IFS=':' read -r num title subtitle <<< "$module_def"

    # Find the module folder
    module_folder=$(find "$COURSE_DIR" -maxdepth 1 -type d -name "Module ${num} -*" | head -1)

    if [ -z "$module_folder" ]; then
        echo "Warning: Module $num folder not found, skipping..."
        continue
    fi

    echo "Processing Module $num: $title..."

    # Check if index.html exists
    if [ ! -f "$module_folder/index.html" ]; then
        echo "  Warning: index.html not found in $module_folder, skipping..."
        continue
    fi

    # Create temp directory for this module
    temp_dir="$SCORM_DIR/temp_module_$num"
    mkdir -p "$temp_dir"

    # Copy scorm_api.js
    cp "$SCORM_DIR/scorm_api.js" "$temp_dir/"

    # Copy and modify index.html to include SCORM
    # Insert SCORM script reference after opening <head>
    sed 's|<head>|<head>\n    <script src="scorm_api.js"></script>|' "$module_folder/index.html" > "$temp_dir/index.html"

    # Check for video files and copy if found
    video_file=""
    video_path=$(find "$module_folder" -maxdepth 1 -name "*.mp4" | head -1)
    if [ -n "$video_path" ]; then
        video_file=$(basename "$video_path")
        echo "  Found video: $video_file"
        cp "$video_path" "$temp_dir/"
    fi

    # Create manifest
    create_manifest "$num" "$title" "$subtitle" "$temp_dir/imsmanifest.xml" "$video_file"

    # Create zip file
    zip_name="Module_${num}_$(echo "$title" | tr ' ' '_' | tr -cd '[:alnum:]_').zip"
    (cd "$temp_dir" && zip -r "$OUTPUT_DIR/$zip_name" *)

    echo "  Created: $zip_name"

    # Clean up temp directory
    rm -rf "$temp_dir"
done

# Create master zip with all modules
echo ""
echo "Creating master zip with all modules..."
(cd "$OUTPUT_DIR" && zip -r "Squadron_Leader_All_Modules.zip" *.zip)

echo ""
echo "====================================="
echo "SCORM Packages created in: $OUTPUT_DIR"
echo "====================================="
ls -la "$OUTPUT_DIR"
