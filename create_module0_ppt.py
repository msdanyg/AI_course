#!/usr/bin/env python3
"""
Create Module 0 PowerPoint Presentation
Pre-Flight Check: Setup, Policy & Boundaries

Uses Official ActivTrak Brand Guidelines from slide_layouts.md
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ActivTrak Official Brand Colors (from slide_layouts.md)
DARK_NAVY = RGBColor(0x14, 0x20, 0x3F)      # #14203F - Body text, closing slide bg
MEDIUM_NAVY = RGBColor(0x19, 0x31, 0x6A)    # #19316A - Header bars, accents
BLUE = RGBColor(0x16, 0x57, 0xA0)           # #1657A0 - Section dividers
WHITE = RGBColor(0xFF, 0xFF, 0xFF)          # #FFFFFF - Background, text on dark
TEAL = RGBColor(0x2E, 0xD4, 0xB5)           # #2ED4B5 - CTAs, accent lines
YELLOW = RGBColor(0xFF, 0xC8, 0x3B)         # #FFC83B - Secondary accents (sparingly)

# Traffic light colors
GREEN = RGBColor(0x22, 0xC5, 0x5E)
AMBER = RGBColor(0xF5, 0xA6, 0x23)
RED = RGBColor(0xEF, 0x44, 0x44)

def set_slide_background(slide, color):
    """Set slide background color"""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_title_slide(prs, title, subtitle):
    """
    Title Slide: Opening slide of presentation
    - White background
    - Dark Navy accent bar at top
    - Centered title (44pt, Dark Navy, bold)
    - Optional centered subtitle (24pt, Medium Navy)
    """
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, WHITE)

    # Dark Navy accent bar at top
    accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(0.5))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = DARK_NAVY
    accent_bar.line.fill.background()

    # Title - centered
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.8), Inches(9), Inches(1.2))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    # Subtitle - centered
    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(0.8))
        tf = sub_box.text_frame
        p = tf.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(24)
        p.font.color.rgb = MEDIUM_NAVY
        p.font.name = "Century Gothic"
        p.alignment = PP_ALIGN.CENTER

    return slide

def add_section_slide(prs, title):
    """
    Section Divider: Transition between major sections
    - Blue background
    - Teal accent line
    - Centered section title (40pt, white, bold)
    """
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, BLUE)

    # Teal accent line
    accent_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(3), Inches(3), Inches(4), Inches(0.05))
    accent_line.fill.solid()
    accent_line.fill.fore_color.rgb = TEAL
    accent_line.line.fill.background()

    # Centered title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.3), Inches(9), Inches(1.2))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    return slide

def add_content_slide(prs, title, bullets):
    """
    Content Slide: Standard information slides with bullet points
    - White background
    - Medium Navy header bar with title
    - Left-aligned title in header (32pt, white, bold)
    - Bullet points (20pt, Dark Navy)
    """
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, WHITE)

    # Medium Navy header bar
    header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(1.2))
    header_bar.fill.solid()
    header_bar.fill.fore_color.rgb = MEDIUM_NAVY
    header_bar.line.fill.background()

    # Left-aligned title in header
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(9), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"

    # Bullets (20pt, Dark Navy)
    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.7), Inches(9), Inches(5.3))
    tf = content_box.text_frame
    tf.word_wrap = True

    for i, bullet in enumerate(bullets):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = f"• {bullet}" if bullet else ""
        p.font.size = Pt(20)
        p.font.color.rgb = DARK_NAVY
        p.font.name = "Century Gothic"
        p.space_after = Pt(6)  # Line spacing: 20pt + 6pt = 26pt

    return slide

def add_two_column_slide(prs, title, left_title, left_items, right_title, right_items):
    """
    Two-Column Slide: Comparisons, before/after, pros/cons
    - White background
    - Medium Navy header bar
    - Two equal columns (18pt, Dark Navy)
    """
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, WHITE)

    # Medium Navy header bar
    header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(1.2))
    header_bar.fill.solid()
    header_bar.fill.fore_color.rgb = MEDIUM_NAVY
    header_bar.line.fill.background()

    # Left-aligned title in header
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(9), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"

    # Left column header
    left_header = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.2), Inches(0.5))
    tf = left_header.text_frame
    p = tf.paragraphs[0]
    p.text = left_title
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = MEDIUM_NAVY
    p.font.name = "Century Gothic"

    # Left column content
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.1), Inches(4.2), Inches(5))
    tf = left_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(left_items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = f"• {item}"
        p.font.size = Pt(18)
        p.font.color.rgb = DARK_NAVY
        p.font.name = "Century Gothic"
        p.space_after = Pt(6)

    # Right column header
    right_header = slide.shapes.add_textbox(Inches(5.3), Inches(1.5), Inches(4.2), Inches(0.5))
    tf = right_header.text_frame
    p = tf.paragraphs[0]
    p.text = right_title
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = MEDIUM_NAVY
    p.font.name = "Century Gothic"

    # Right column content
    right_box = slide.shapes.add_textbox(Inches(5.3), Inches(2.1), Inches(4.2), Inches(5))
    tf = right_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(right_items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = f"• {item}"
        p.font.size = Pt(18)
        p.font.color.rgb = DARK_NAVY
        p.font.name = "Century Gothic"
        p.space_after = Pt(6)

    return slide

def add_closing_slide(prs, message, cta=""):
    """
    Closing Slide: Final slide with call to action
    - Dark Navy background
    - Teal accent bar at bottom
    - Centered closing message (44pt, white, bold)
    - Optional CTA text (24pt, teal)
    """
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, DARK_NAVY)

    # Teal accent bar at bottom
    accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7), Inches(10), Inches(0.5))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = TEAL
    accent_bar.line.fill.background()

    # Centered closing message
    msg_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.8), Inches(9), Inches(1.2))
    tf = msg_box.text_frame
    p = tf.paragraphs[0]
    p.text = message
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    # Optional CTA
    if cta:
        cta_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(0.8))
        tf = cta_box.text_frame
        p = tf.paragraphs[0]
        p.text = cta
        p.font.size = Pt(24)
        p.font.color.rgb = TEAL
        p.font.name = "Century Gothic"
        p.alignment = PP_ALIGN.CENTER

    return slide

def add_traffic_light_slide(prs):
    """Add the traffic light protocol slide using content slide layout"""
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, WHITE)

    # Medium Navy header bar
    header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(1.2))
    header_bar.fill.solid()
    header_bar.fill.fore_color.rgb = MEDIUM_NAVY
    header_bar.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(9), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "The Traffic Light Protocol"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"

    # Green zone
    green_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.3), Inches(1.5), Inches(3), Inches(2.2))
    green_box.fill.solid()
    green_box.fill.fore_color.rgb = RGBColor(0xDC, 0xFC, 0xE7)
    green_box.line.color.rgb = GREEN
    green_box.line.width = Pt(3)

    green_title = slide.shapes.add_textbox(Inches(0.5), Inches(1.6), Inches(2.6), Inches(0.5))
    tf = green_title.text_frame
    p = tf.paragraphs[0]
    p.text = "GREEN: Go Freely"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x16, 0x65, 0x34)
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    green_content = slide.shapes.add_textbox(Inches(0.4), Inches(2.2), Inches(2.8), Inches(1.4))
    tf = green_content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Customer data, internal docs, analytics, business communications"
    p.font.size = Pt(14)
    p.font.color.rgb = DARK_NAVY
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    # Yellow zone
    yellow_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.5), Inches(1.5), Inches(3), Inches(2.2))
    yellow_box.fill.solid()
    yellow_box.fill.fore_color.rgb = RGBColor(0xFE, 0xF9, 0xC3)
    yellow_box.line.color.rgb = AMBER
    yellow_box.line.width = Pt(3)

    yellow_title = slide.shapes.add_textbox(Inches(3.7), Inches(1.6), Inches(2.6), Inches(0.5))
    tf = yellow_title.text_frame
    p = tf.paragraphs[0]
    p.text = "YELLOW: Review Required"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x92, 0x40, 0x0E)
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    yellow_content = slide.shapes.add_textbox(Inches(3.6), Inches(2.2), Inches(2.8), Inches(1.4))
    tf = yellow_content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Marketing with PII, competitive intel, NDA-covered data"
    p.font.size = Pt(14)
    p.font.color.rgb = DARK_NAVY
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    # Red zone
    red_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.7), Inches(1.5), Inches(3), Inches(2.2))
    red_box.fill.solid()
    red_box.fill.fore_color.rgb = RGBColor(0xFE, 0xE2, 0xE2)
    red_box.line.color.rgb = RED
    red_box.line.width = Pt(3)

    red_title = slide.shapes.add_textbox(Inches(6.9), Inches(1.6), Inches(2.6), Inches(0.5))
    tf = red_title.text_frame
    p = tf.paragraphs[0]
    p.text = "RED: Never Share"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    red_content = slide.shapes.add_textbox(Inches(6.8), Inches(2.2), Inches(2.8), Inches(1.4))
    tf = red_content.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "API keys, passwords, credentials, security configs"
    p.font.size = Pt(14)
    p.font.color.rgb = DARK_NAVY
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    # Core principle box with TEAL accent
    principle_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(4.2), Inches(8), Inches(1.5))
    principle_box.fill.solid()
    principle_box.fill.fore_color.rgb = RGBColor(0xF0, 0xF8, 0xF5)
    principle_box.line.color.rgb = TEAL
    principle_box.line.width = Pt(2)

    principle_text = slide.shapes.add_textbox(Inches(1.2), Inches(4.4), Inches(7.6), Inches(0.6))
    tf = principle_text.text_frame
    p = tf.paragraphs[0]
    p.text = '"AI drafts. Humans send."'
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    sub_text = slide.shapes.add_textbox(Inches(1.2), Inches(5.1), Inches(7.6), Inches(0.5))
    tf = sub_text.text_frame
    p = tf.paragraphs[0]
    p.text = "You clear missions for takeoff. You own what leaves the runway."
    p.font.size = Pt(16)
    p.font.color.rgb = MEDIUM_NAVY
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    return slide

def add_squadron_roles_slide(prs):
    """Add the four squadron roles slide using content slide layout"""
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, WHITE)

    # Medium Navy header bar
    header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(1.2))
    header_bar.fill.solid()
    header_bar.fill.fore_color.rgb = MEDIUM_NAVY
    header_bar.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(9), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "The Squadron Framework"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"

    roles = [
        ("Mission Control", "Reasoning & Strategy", "Claude, ChatGPT, Claude Code, Cursor", DARK_NAVY),
        ("Recon & Radar", "Research & Grounding", "Gemini, Perplexity, NotebookLM", BLUE),
        ("Flight Recorder", "Capture & Memory", "Granola, Chorus.ai, Zoom AI", TEAL),
        ("Specialized Units", "Domain-Specific", "Figma AI, Zendesk AI, ChurnZero", MEDIUM_NAVY)
    ]

    for i, (name, role, tools, color) in enumerate(roles):
        x = Inches(0.3 + (i * 2.4))

        # Card background
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.5), Inches(2.2), Inches(3.8))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = RGBColor(0xE0, 0xE0, 0xE0)
        card.line.width = Pt(1)

        # Color bar at top of card
        color_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.5), Inches(2.2), Inches(0.3))
        color_bar.fill.solid()
        color_bar.fill.fore_color.rgb = color
        color_bar.line.fill.background()

        # Role name
        name_box = slide.shapes.add_textbox(x, Inches(2.0), Inches(2.2), Inches(0.6))
        tf = name_box.text_frame
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = DARK_NAVY
        p.font.name = "Century Gothic"
        p.alignment = PP_ALIGN.CENTER

        # Role description
        desc_box = slide.shapes.add_textbox(x, Inches(2.6), Inches(2.2), Inches(0.5))
        tf = desc_box.text_frame
        p = tf.paragraphs[0]
        p.text = role
        p.font.size = Pt(12)
        p.font.color.rgb = color
        p.font.name = "Century Gothic"
        p.alignment = PP_ALIGN.CENTER

        # Tools
        tools_box = slide.shapes.add_textbox(x, Inches(3.2), Inches(2.2), Inches(1.8))
        tf = tools_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tools
        p.font.size = Pt(11)
        p.font.color.rgb = MEDIUM_NAVY
        p.font.name = "Century Gothic"
        p.alignment = PP_ALIGN.CENTER

    # Bottom note with Teal accent
    note_box = slide.shapes.add_textbox(Inches(0.5), Inches(5.8), Inches(9), Inches(0.5))
    tf = note_box.text_frame
    p = tf.paragraphs[0]
    p.text = "Your Squadron = Your Available Tools. Think in roles, not specific tools."
    p.font.size = Pt(16)
    p.font.italic = True
    p.font.color.rgb = TEAL
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    return slide

def add_quote_slide(prs, quote, attribution=""):
    """Add a quote slide - uses Blue background like section divider"""
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, BLUE)

    # Quote
    quote_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(2.5))
    tf = quote_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f'"{quote}"'
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"
    p.alignment = PP_ALIGN.CENTER

    if attribution:
        attr_box = slide.shapes.add_textbox(Inches(1), Inches(5.2), Inches(8), Inches(0.5))
        tf = attr_box.text_frame
        p = tf.paragraphs[0]
        p.text = attribution
        p.font.size = Pt(18)
        p.font.color.rgb = TEAL
        p.font.name = "Century Gothic"
        p.alignment = PP_ALIGN.CENTER

    return slide

def add_key_takeaways_slide(prs, takeaways):
    """Add a key takeaways slide - content slide with Teal header"""
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_background(slide, WHITE)

    # Blue header bar for emphasis
    header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(1.2))
    header_bar.fill.solid()
    header_bar.fill.fore_color.rgb = BLUE
    header_bar.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(9), Inches(0.8))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "Key Takeaways"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Century Gothic"

    # Takeaways with Teal checkmarks
    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.7), Inches(9), Inches(5.3))
    tf = content_box.text_frame
    tf.word_wrap = True

    for i, takeaway in enumerate(takeaways):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = takeaway
        p.font.size = Pt(20)
        p.font.color.rgb = DARK_NAVY
        p.font.name = "Century Gothic"
        p.space_after = Pt(12)

    return slide

def create_presentation():
    """Create the full Module 0 presentation with ActivTrak branding"""
    prs = Presentation()
    # Official dimensions: 10" x 7.5" (4:3 aspect ratio)
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Slide 1: Title
    add_title_slide(prs,
        "Module 0: Pre-Flight Check",
        "Setup, Policy and Boundaries")

    # Slide 2: Opening quote
    add_quote_slide(prs,
        "Every pilot completes a pre-flight check before takeoff.",
        "It's not bureaucracy - it's what separates safe flights from disasters.")

    # Slide 3: Section - Squadron Framework
    add_section_slide(prs, "The Squadron Framework")

    # Slide 4: Squadron Roles
    add_squadron_roles_slide(prs)

    # Slide 5: Why Think in Roles?
    add_content_slide(prs, "Why Think in Roles?", [
        "Your Squadron depends on what tools you have access to",
        "You don't need every tool - understand what roles your tools fill",
        "Match tasks to capabilities, not to specific tool names",
        "Different employees have different tools - that's expected"
    ])

    # Slide 6: Scenario Examples
    add_content_slide(prs, "Matching Tasks to Roles", [
        "Draft a competitive positioning email - Mission Control (Claude, ChatGPT)",
        "Check competitor's current pricing - Recon and Radar (Gemini, Perplexity)",
        "Summarize yesterday's client call - Flight Recorder then Mission Control",
        "Research market trends with citations - Recon and Radar (Gemini)"
    ])

    # Slide 7: Section - Traffic Light Protocol
    add_section_slide(prs, "The Traffic Light Protocol")

    # Slide 8: Key Insight
    add_quote_slide(prs,
        "The risk is rarely in analyzing data. The risk is in sharing unreviewed AI output.")

    # Slide 9: Traffic Light
    add_traffic_light_slide(prs)

    # Slide 10: Green Zone Details
    add_content_slide(prs, "Green Zone: Go Freely", [
        "Customer names, emails, deal information",
        "Internal documents (meeting notes, project plans)",
        "Usage data and analytics",
        "Business communications",
        "Why green? AI processes privately. Review outputs before sharing externally."
    ])

    # Slide 11: Yellow and Red Zones
    add_two_column_slide(prs, "Yellow and Red Zones",
        "Yellow: Review Required",
        ["Marketing collateral with customer PII", "Competitive intelligence with source details", "Third-party data under NDA", "May need PR, Legal, or partner review"],
        "Red: Never Share",
        ["API keys and passwords", "Admin credentials", "Security configurations", "If in doubt, don't include it"])

    # Slide 12: Section - Setting Up Your Cockpit
    add_section_slide(prs, "Setting Up Your Cockpit")

    # Slide 13: Inventory Your Tools
    add_content_slide(prs, "Inventory Your Tools", [
        "Mission Control: Do you have Claude, ChatGPT, Claude Code, or Cursor?",
        "Recon and Radar: Do you have Gemini? Perplexity?",
        "Flight Recorder: Granola, Chorus, or Zoom AI summaries?",
        "Specialized Units: What department-specific AI tools do you have?"
    ])

    # Slide 14: Configuration Checklist
    add_content_slide(prs, "Configuration Checklist", [
        "Verify each tool is working (log in, run a test prompt)",
        "Check if you can upload files",
        "Note any special features or limitations",
        "Gemini is available company-wide for research",
        "If missing Mission Control, request Claude or ChatGPT from IT"
    ])

    # Slide 15: Restricted Tools
    add_content_slide(prs, "Restricted Tools", [
        "Some AI tools are NOT approved for ActivTrak use:",
        "DeepSeek AI - Security concerns",
        "RedNote AI apps - Security concerns",
        "When in doubt about a tool, check with IT"
    ])

    # Slide 16: Section - Squadron Mindset
    add_section_slide(prs, "The Squadron Mindset")

    # Slide 17: Solo Pilot vs Squadron Leader
    add_two_column_slide(prs, "Solo Pilot vs Squadron Leader",
        "Solo Pilot",
        ["Minimal context", "Freeform questions", "Starts fresh every time", "Generic outputs", "'Write me an email'"],
        "Squadron Leader",
        ["Rich background context", "Organized structure", "Maintains persistent knowledge", "Tailored outputs", "'Given this account's history...'"])

    # Slide 18: Key Takeaways
    add_key_takeaways_slide(prs, [
        "Four Squadron roles: Mission Control, Recon and Radar, Flight Recorder, Specialized Units",
        "Traffic Light Protocol: Green (go), Yellow (review), Red (never)",
        "Core principle: AI drafts, humans send",
        "Squadron Leader mindset: orchestrate with context, structure and review"
    ])

    # Slide 19: What's Next
    add_content_slide(prs, "What's Next?", [
        "Module 1: The Cognitive Shift",
        "Understand how reasoning engines actually work",
        "Move from search engine thinking to reasoning engine thinking",
        "Learn why context matters so much",
        "But first: Complete the lab exercise to verify your cockpit is operational!"
    ])

    # Slide 20: Closing
    add_closing_slide(prs,
        "Pre-Flight Check Complete",
        "Your cockpit is ready. See you in Module 1.")

    # Save
    output_path = "/Users/dglickman@bgrove.com/AI course/Module 0 - Pre-Flight Check/Module_0_Slides.pptx"
    prs.save(output_path)
    print(f"Presentation saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    create_presentation()
