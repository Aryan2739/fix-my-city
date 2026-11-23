import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"c:\Users\0110a\OneDrive\Desktop\deforestration\canopy-observatory\fix-my-city"
os.makedirs(output_dir, exist_ok=True)

# Helper function to get default or simple font
def get_font(size, bold=False):
    font_paths = [
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\tahoma.ttf"
    ]
    if bold:
        font_paths = [
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\tahomabd.ttf"
        ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

font_title = get_font(28, bold=True)
font_h1 = get_font(22, bold=True)
font_h2 = get_font(18, bold=True)
font_body = get_font(14, bold=False)
font_body_b = get_font(14, bold=True)
font_small = get_font(11, bold=False)
font_small_b = get_font(11, bold=True)

# Theme colors
DARK_BG = (30, 30, 30)
SIDEBAR_BG = (44, 44, 44)
HEADER_BG = (38, 38, 38)
CARD_BG = (255, 255, 255)
TEAL_PRIMARY = (13, 148, 136)
TEAL_LIGHT = (204, 251, 241)
ACCENT_BLUE = (14, 165, 233)
TEXT_DARK = (15, 23, 42)
TEXT_MUTED = (100, 116, 139)
BORDER_COL = (226, 232, 240)
STATUS_OPEN = (239, 68, 68)
STATUS_PROG = (245, 158, 11)
STATUS_RESOLVED = (16, 185, 129)
PROTOTYPE_WIRE = (56, 189, 248)

# -------------------------------------------------------------------------
# IMAGE 1: Figma Canvas Overview with Prototype Interaction Noodles
# -------------------------------------------------------------------------
def create_canvas_overview():
    w, h = 1600, 950
    img = Image.new("RGB", (w, h), DARK_BG)
    draw = ImageDraw.Draw(img)

    # 1. Top Figma Menu Bar
    draw.rectangle([0, 0, w, 44], fill=HEADER_BG)
    # Figma icon & breadcrumb
    draw.rectangle([14, 12, 24, 32], fill=(242, 78, 30))
    draw.text((36, 14), "Fix My City — UI/UX Interactive Prototype v1.0", fill=(240, 240, 240), font=font_body_b)
    draw.text((550, 14), "Drafts / Civic Technology / FixMyCity", fill=(160, 160, 160), font=font_small)
    
    # Right top bar controls
    draw.rectangle([w - 170, 8, w - 85, 36], fill=(59, 130, 246), outline=(96, 165, 250))
    draw.text((w - 152, 14), "▷ Present", fill=(255, 255, 255), font=font_small_b)
    draw.rectangle([w - 80, 8, w - 15, 36], fill=(50, 50, 50), outline=(80, 80, 80))
    draw.text((w - 65, 14), "Share", fill=(255, 255, 255), font=font_small_b)

    # 2. Left Layers / Pages Sidebar
    draw.rectangle([0, 44, 260, h], fill=SIDEBAR_BG)
    draw.text((16, 56), "PAGES", fill=(160, 160, 160), font=font_small_b)
    draw.text((16, 78), "✓ 📄 01 | Interactive Citizen Flow", fill=(255, 255, 255), font=font_small_b)
    draw.text((16, 98), "   📄 02 | Municipal Admin Queue", fill=(180, 180, 180), font=font_small)
    draw.text((16, 118), "   📄 03 | Design Tokens & System", fill=(180, 180, 180), font=font_small)
    
    draw.line([0, 145, 260, 145], fill=(60, 60, 60), width=1)
    draw.text((16, 155), "LAYERS", fill=(160, 160, 160), font=font_small_b)
    layers = [
        "❖ Frame 1: Splash & Onboarding",
        "  ↳ # Header_Hero_Container",
        "  ↳ ❖ Button_Report_Issue",
        "❖ Frame 2: 4-Step Incident Form",
        "  ↳ # Category_Grid_Selector",
        "  ↳ # Input_GPS_Location",
        "  ↳ ❖ Button_Submit_Ticket",
        "❖ Frame 3: Live Civic Feed & Map",
        "  ↳ # Map_Cluster_Container",
        "  ↳ ❖ Card_Complaint_Item",
        "❖ Frame 4: Ticket Status Stepper",
        "  ↳ # Stepper_Lifecycle_Track",
        "  ↳ # Comparison_Before_After"
    ]
    ly = 175
    for l in layers:
        col = (230, 230, 230) if "❖ Frame" in l else (170, 170, 170)
        draw.text((20, ly), l, fill=col, font=font_small)
        ly += 22

    # 3. Right Prototype & Design Inspector Sidebar
    draw.rectangle([w - 280, 44, w, h], fill=SIDEBAR_BG)
    draw.text((w - 265, 56), "PROTOTYPE SETTINGS", fill=(160, 160, 160), font=font_small_b)
    
    inspect_items = [
        ("Flow starting point:", "Citizen Complaint Journey"),
        ("Trigger:", "On Click"),
        ("Action:", "Navigate To -> Frame 2"),
        ("Animation:", "Smart Animate (Ease-out 250ms)"),
        ("Overlay Mode:", "Centered / Scrim 30%"),
        ("Design Tokens:", "Color / Primary / Teal-600"),
        ("Grid System:", "8pt Civic Grid (12-Col Desktop)")
    ]
    iy = 85
    for title, val in inspect_items:
        draw.text((w - 265, iy), title, fill=(150, 150, 150), font=font_small)
        draw.rectangle([w - 265, iy + 16, w - 20, iy + 38], fill=(30, 30, 30), outline=(70, 70, 70))
        draw.text((w - 255, iy + 22), val, fill=(240, 240, 240), font=font_small_b)
        iy += 48

    # 4. Canvas Center Background (Dot Grid Simulation)
    canvas_w = w - 540
    for gx in range(270, w - 280, 24):
        for gy in range(54, h, 24):
            draw.point((gx, gy), fill=(55, 55, 55))

    # Canvas Title Banner
    draw.rectangle([290, 60, 680, 95], fill=(45, 45, 45), outline=(70, 70, 70))
    draw.text((305, 68), "Figma Interactive Canvas — Prototype Flow View", fill=TEAL_LIGHT, font=font_h2)

    # 5. Artboard 1: Citizen Landing (Desktop)
    ab1_x, ab1_y, ab1_w, ab1_h = 290, 120, 280, 380
    draw.rectangle([ab1_x, ab1_y, ab1_x + ab1_w, ab1_y + ab1_h], fill=CARD_BG, outline=(120, 120, 120), width=1)
    draw.text((ab1_x, ab1_y - 18), "Frame 1: Citizen Landing (1440x900)", fill=(180, 180, 180), font=font_small_b)
    # Navbar
    draw.rectangle([ab1_x, ab1_y, ab1_x + ab1_w, ab1_y + 35], fill=(245, 247, 250))
    draw.rectangle([ab1_x + 10, ab1_y + 8, ab1_x + 28, ab1_y + 26], fill=TEAL_PRIMARY)
    draw.text((ab1_x + 34, ab1_y + 11), "FixMyCity", fill=TEXT_DARK, font=font_small_b)
    # Hero
    draw.rectangle([ab1_x + 10, ab1_y + 50, ab1_x + ab1_w - 10, ab1_y + 160], fill=(240, 253, 250))
    draw.text((ab1_x + 18, ab1_y + 60), "Spotted a problem in your city?", fill=TEXT_DARK, font=font_body_b)
    draw.text((ab1_x + 18, ab1_y + 78), "Report it. Track it. Get it fixed.", fill=TEAL_PRIMARY, font=font_small_b)
    # CTA Button
    btn_report_rect = [ab1_x + 18, ab1_y + 115, ab1_x + 140, ab1_y + 145]
    draw.rectangle(btn_report_rect, fill=TEAL_PRIMARY)
    draw.text((ab1_x + 26, ab1_y + 124), "+ Report an Issue", fill=(255, 255, 255), font=font_small_b)
    # Stats
    draw.rectangle([ab1_x + 15, ab1_y + 180, ab1_x + 130, ab1_y + 230], fill=(255, 255, 255), outline=BORDER_COL)
    draw.text((ab1_x + 25, ab1_y + 190), "14,890+", fill=TEXT_DARK, font=font_body_b)
    draw.text((ab1_x + 25, ab1_y + 210), "Resolved", fill=STATUS_RESOLVED, font=font_small)
    draw.rectangle([ab1_x + 145, ab1_y + 180, ab1_x + 265, ab1_y + 230], fill=(255, 255, 255), outline=BORDER_COL)
    draw.text((ab1_x + 155, ab1_y + 190), "94% SLA", fill=TEXT_DARK, font=font_body_b)
    draw.text((ab1_x + 155, ab1_y + 210), "On Time", fill=STATUS_PROG, font=font_small)

    # 6. Artboard 2: Report Form Modal (Mobile/Modal)
    ab2_x, ab2_y, ab2_w, ab2_h = 630, 120, 280, 420
    draw.rectangle([ab2_x, ab2_y, ab2_x + ab2_w, ab2_y + ab2_h], fill=CARD_BG, outline=TEAL_PRIMARY, width=2)
    draw.text((ab2_x, ab2_y - 18), "Frame 2: 4-Step Incident Report Modal", fill=TEAL_LIGHT, font=font_small_b)
    # Modal Header
    draw.rectangle([ab2_x, ab2_y, ab2_x + ab2_w, ab2_y + 35], fill=TEAL_PRIMARY)
    draw.text((ab2_x + 12, ab2_y + 10), "Submit Civic Complaint", fill=(255, 255, 255), font=font_small_b)
    # Step 1: Category grid
    draw.text((ab2_x + 12, ab2_y + 48), "1. Select Category:", fill=TEXT_DARK, font=font_small_b)
    cats = ["Roads", "Lights", "Waste", "Water"]
    cx = ab2_x + 12
    for c in cats:
        draw.rectangle([cx, ab2_y + 68, cx + 58, ab2_y + 98], fill=TEAL_LIGHT if c == "Roads" else (248, 250, 252), outline=TEAL_PRIMARY if c == "Roads" else BORDER_COL)
        draw.text((cx + 10, ab2_y + 78), c, fill=TEXT_DARK, font=font_small)
        cx += 65
    # Step 2: Form fields
    draw.text((ab2_x + 12, ab2_y + 112), "Issue Title:", fill=TEXT_DARK, font=font_small)
    draw.rectangle([ab2_x + 12, ab2_y + 128, ab2_x + ab2_w - 12, ab2_y + 154], fill=(248, 250, 252), outline=BORDER_COL)
    draw.text((ab2_x + 18, ab2_y + 134), "Deep Pothole on Oak St...", fill=TEXT_MUTED, font=font_small)
    # Step 3: GPS
    draw.text((ab2_x + 12, ab2_y + 168), "Location Pin:", fill=TEXT_DARK, font=font_small)
    draw.rectangle([ab2_x + 12, ab2_y + 184, ab2_x + ab2_w - 12, ab2_y + 210], fill=(248, 250, 252), outline=BORDER_COL)
    draw.text((ab2_x + 18, ab2_y + 190), "GPS: 40.7128° N, 74.0060° W", fill=TEAL_PRIMARY, font=font_small)
    # Step 4: Photo Evidence upload box
    draw.rectangle([ab2_x + 12, ab2_y + 225, ab2_x + ab2_w - 12, ab2_y + 310], fill=(245, 245, 245), outline=(200, 200, 200))
    draw.text((ab2_x + 60, ab2_y + 260), "📷 [Photo Preview Attached]", fill=TEXT_MUTED, font=font_small)
    # Submit button
    btn_submit_rect = [ab2_x + 12, ab2_y + 360, ab2_x + ab2_w - 12, ab2_y + 395]
    draw.rectangle(btn_submit_rect, fill=TEAL_PRIMARY)
    draw.text((ab2_x + 75, ab2_y + 372), "Submit & Generate Ticket", fill=(255, 255, 255), font=font_small_b)

    # 7. Artboard 3: Civic Feed & Interactive Map
    ab3_x, ab3_y, ab3_w, ab3_h = 290, 540, 280, 360
    draw.rectangle([ab3_x, ab3_y, ab3_x + ab3_w, ab3_y + ab3_h], fill=CARD_BG, outline=(120, 120, 120), width=1)
    draw.text((ab3_x, ab3_y - 18), "Frame 3: Live Feed & Geospatial Map", fill=(180, 180, 180), font=font_small_b)
    # Map container
    draw.rectangle([ab3_x + 10, ab3_y + 10, ab3_x + ab3_w - 10, ab3_y + 150], fill=(224, 242, 254), outline=(186, 230, 253))
    draw.text((ab3_x + 20, ab3_y + 20), "🗺️ Interactive Leaflet Map", fill=(3, 105, 161), font=font_small_b)
    # Map pins
    draw.ellipse([ab3_x + 60, ab3_y + 60, ab3_x + 76, ab3_y + 76], fill=STATUS_OPEN, outline=(255, 255, 255))
    draw.ellipse([ab3_x + 140, ab3_y + 80, ab3_x + 156, ab3_y + 96], fill=STATUS_PROG, outline=(255, 255, 255))
    draw.ellipse([ab3_x + 200, ab3_y + 50, ab3_x + 216, ab3_y + 66], fill=STATUS_RESOLVED, outline=(255, 255, 255))
    # Complaint Card Item
    draw.rectangle([ab3_x + 10, ab3_y + 165, ab3_x + ab3_w - 10, ab3_y + 270], fill=(255, 255, 255), outline=BORDER_COL)
    draw.rectangle([ab3_x + 18, ab3_y + 175, ab3_x + 75, ab3_y + 195], fill=(254, 226, 226))
    draw.text((ab3_x + 24, ab3_y + 179), "OPEN", fill=STATUS_OPEN, font=font_small_b)
    draw.text((ab3_x + 18, ab3_y + 205), "Pothole at Oak St & 4th Ave", fill=TEXT_DARK, font=font_small_b)
    draw.text((ab3_x + 18, ab3_y + 225), "👍 42 Upvotes   |   Track ->", fill=TEAL_PRIMARY, font=font_small_b)

    # 8. Artboard 4: Lifecycle Tracker & Before/After Proof
    ab4_x, ab4_y, ab4_w, ab4_h = 630, 560, 280, 340
    draw.rectangle([ab4_x, ab4_y, ab4_x + ab4_w, ab4_y + ab4_h], fill=CARD_BG, outline=(120, 120, 120), width=1)
    draw.text((ab4_x, ab4_y - 18), "Frame 4: Ticket Status Stepper (#FMC-103)", fill=(180, 180, 180), font=font_small_b)
    # Ticket banner
    draw.rectangle([ab4_x + 10, ab4_y + 10, ab4_x + ab4_w - 10, ab4_y + 40], fill=TEAL_LIGHT)
    draw.text((ab4_x + 18, ab4_y + 18), "Ticket #FMC-103: Garbage Dump", fill=TEAL_PRIMARY, font=font_small_b)
    # 4-step progress
    steps = ["1. Registered (Nov 21)", "2. Verified (Nov 21)", "3. Dispatched (Nov 22)", "4. Resolved (Nov 22)"]
    sy = ab4_y + 55
    for s in steps:
        draw.ellipse([ab4_x + 15, sy, ab4_x + 29, sy + 14], fill=STATUS_RESOLVED)
        draw.text((ab4_x + 36, sy), s, fill=TEXT_DARK, font=font_small)
        sy += 24
    # Before vs After photo boxes
    draw.rectangle([ab4_x + 15, ab4_y + 165, ab4_x + 130, ab4_y + 250], fill=(254, 226, 226), outline=STATUS_OPEN)
    draw.text((ab4_x + 25, ab4_y + 175), "[BEFORE]", fill=STATUS_OPEN, font=font_small_b)
    draw.text((ab4_x + 25, ab4_y + 195), "Overflowing\nDumpster", fill=TEXT_DARK, font=font_small)

    draw.rectangle([ab4_x + 145, ab4_y + 165, ab4_x + 260, ab4_y + 250], fill=(209, 250, 229), outline=STATUS_RESOLVED)
    draw.text((ab4_x + 155, ab4_y + 175), "[AFTER]", fill=STATUS_RESOLVED, font=font_small_b)
    draw.text((ab4_x + 155, ab4_y + 195), "Sanitized &\nCleared", fill=TEXT_DARK, font=font_small)

    # 9. Artboard 5: Municipal Admin Operations
    ab5_x, ab5_y, ab5_w, ab5_h = 950, 120, 330, 420
    draw.rectangle([ab5_x, ab5_y, ab5_x + ab5_w, ab5_y + ab5_h], fill=CARD_BG, outline=(120, 120, 120), width=1)
    draw.text((ab5_x, ab5_y - 18), "Frame 5: Municipal Admin Operations (Queue)", fill=(180, 180, 180), font=font_small_b)
    # Admin header
    draw.rectangle([ab5_x, ab5_y, ab5_x + ab5_w, ab5_y + 45], fill=(15, 23, 42))
    draw.text((ab5_x + 12, ab5_y + 14), "🛡️ Municipal Command Portal", fill=(255, 255, 255), font=font_small_b)
    # Queue rows
    q_items = [
        ("#FMC-101", "Roads Dept", "OPEN", STATUS_OPEN),
        ("#FMC-102", "Lighting Dept", "IN PROGRESS", STATUS_PROG),
        ("#FMC-103", "Sanitation", "RESOLVED", STATUS_RESOLVED),
        ("#FMC-104", "Water Works", "IN PROGRESS", STATUS_PROG),
        ("#FMC-105", "Parks Dept", "OPEN", STATUS_OPEN)
    ]
    qy = ab5_y + 60
    for tid, dept, st, col in q_items:
        draw.rectangle([ab5_x + 10, qy, ab5_x + ab5_w - 10, qy + 40], fill=(248, 250, 252), outline=BORDER_COL)
        draw.text((ab5_x + 18, qy + 12), tid, fill=TEXT_DARK, font=font_small_b)
        draw.text((ab5_x + 85, qy + 12), dept, fill=TEXT_MUTED, font=font_small)
        draw.rectangle([ab5_x + 210, qy + 8, ab5_x + ab5_w - 20, qy + 30], fill=col)
        draw.text((ab5_x + 218, qy + 12), st, fill=(255, 255, 255), font=font_small_b)
        qy += 48

    # 10. Draw Prototype Interaction Noodles (Wires connecting frames in Figma!)
    # Wire 1: From Frame 1 "+ Report an Issue" Button to Frame 2 Modal
    p1_start = (ab1_x + 140, ab1_y + 130)
    p1_end = (ab2_x, ab2_y + 130)
    draw.ellipse([p1_start[0] - 5, p1_start[1] - 5, p1_start[0] + 5, p1_start[1] + 5], fill=PROTOTYPE_WIRE)
    draw.line([p1_start[0], p1_start[1], p1_end[0] - 10, p1_end[1]], fill=PROTOTYPE_WIRE, width=3)
    draw.polygon([(p1_end[0], p1_end[1]), (p1_end[0] - 12, p1_end[1] - 6), (p1_end[0] - 12, p1_end[1] + 6)], fill=PROTOTYPE_WIRE)
    draw.text((p1_start[0] + 15, p1_start[1] - 18), "On Click -> Open Modal", fill=PROTOTYPE_WIRE, font=font_small_b)

    # Wire 2: From Frame 2 "Submit Button" to Frame 4 Tracker
    p2_start = (ab2_x + 140, ab2_y + 395)
    p2_end = (ab4_x + 140, ab4_y)
    draw.ellipse([p2_start[0] - 5, p2_start[1] - 5, p2_start[0] + 5, p2_start[1] + 5], fill=PROTOTYPE_WIRE)
    draw.line([p2_start[0], p2_start[1], p2_end[0], p2_end[1] - 10], fill=PROTOTYPE_WIRE, width=3)
    draw.polygon([(p2_end[0], p2_end[1]), (p2_end[0] - 6, p2_end[1] - 12), (p2_end[0] + 6, p2_end[1] - 12)], fill=PROTOTYPE_WIRE)
    draw.text((p2_start[0] + 10, p2_start[1] + 60), "Submit -> Navigate to Tracker", fill=PROTOTYPE_WIRE, font=font_small_b)

    # Wire 3: From Frame 3 "Track" button to Frame 4 Tracker
    p3_start = (ab3_x + 230, ab3_y + 225)
    p3_end = (ab4_x, ab4_y + 200)
    draw.ellipse([p3_start[0] - 5, p3_start[1] - 5, p3_start[0] + 5, p3_start[1] + 5], fill=PROTOTYPE_WIRE)
    draw.line([p3_start[0], p3_start[1], p3_end[0] - 10, p3_end[1]], fill=PROTOTYPE_WIRE, width=3)
    draw.polygon([(p3_end[0], p3_end[1]), (p3_end[0] - 12, p3_end[1] - 6), (p3_end[0] - 12, p3_end[1] + 6)], fill=PROTOTYPE_WIRE)

    # Watermark / Legend
    draw.rectangle([w - 260, h - 100, w - 20, h - 20], fill=(20, 20, 20), outline=(60, 60, 60))
    draw.text((w - 245, h - 90), "FIGMA PROTOTYPE WIRES", fill=PROTOTYPE_WIRE, font=font_small_b)
    draw.text((w - 245, h - 68), "🔵 Blue Splines = Interactive Flows", fill=(200, 200, 200), font=font_small)
    draw.text((w - 245, h - 48), "Smart Animate & Overlay States", fill=(160, 160, 160), font=font_small)

    img.save(os.path.join(output_dir, "figma_canvas_overview.png"), quality=95)
    print("Created figma_canvas_overview.png")

# -------------------------------------------------------------------------
# IMAGE 2: Mobile UI/UX Wireframe Flow (4 Artboards Connected)
# -------------------------------------------------------------------------
def create_mobile_flow():
    w, h = 1500, 850
    img = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(img)

    # Title Banner
    draw.text((50, 40), "Fix My City — Mobile Citizen Flow (Figma Artboards 390x844)", fill=TEXT_DARK, font=font_title)
    draw.text((50, 80), "Step-by-step user journey from sighting a civic problem to receiving resolution verification.", fill=TEXT_MUTED, font=font_body)

    screens = [
        ("Screen 1: Splash & Discovery", "Onboarding hero, quick categories, & civic impact metrics.", TEAL_PRIMARY),
        ("Screen 2: Category & Details", "Select problem type, title, urgency, & descriptive note.", ACCENT_BLUE),
        ("Screen 3: GPS Pin & Photo Upload", "Interactive map pin placement & camera evidence capture.", (168, 85, 247)),
        ("Screen 4: Lifecycle Tracker", "Live municipal dispatch stepper & Before/After QA proof.", STATUS_RESOLVED)
    ]

    sx = 50
    phone_w, phone_h = 300, 620
    for i, (title, desc, accent) in enumerate(screens):
        # Phone body frame (iPhone Mockup style)
        draw.rectangle([sx, 130, sx + phone_w, 130 + phone_h], fill=(255, 255, 255), outline=(15, 23, 42), width=3)
        # Phone notch
        draw.rectangle([sx + 90, 130, sx + 210, 150], fill=(15, 23, 42))
        
        # Header inside phone
        draw.rectangle([sx, 150, sx + phone_w, 195], fill=accent)
        draw.text((sx + 15, 165), f"FixMyCity • Step {i+1}", fill=(255, 255, 255), font=font_small_b)
        
        # Screen specific mockup content
        if i == 0:
            draw.text((sx + 20, 220), "Civic Problem?", fill=TEXT_DARK, font=font_h2)
            draw.text((sx + 20, 245), "Report issues directly to\ncity municipal crews.", fill=TEXT_MUTED, font=font_small)
            # 4 category cards
            cats = [("Potholes", "bi-cone"), ("Streetlights", "bi-light"), ("Garbage", "bi-trash"), ("Water Leak", "bi-water")]
            cy = 300
            for name, ic in cats:
                draw.rectangle([sx + 20, cy, sx + phone_w - 20, cy + 42], fill=(241, 245, 249), outline=BORDER_COL)
                draw.text((sx + 35, cy + 12), f"⚠️ {name}", fill=TEXT_DARK, font=font_small_b)
                cy += 50
            # Bottom CTA
            draw.rectangle([sx + 20, 130 + phone_h - 70, sx + phone_w - 20, 130 + phone_h - 25], fill=TEAL_PRIMARY)
            draw.text((sx + 70, 130 + phone_h - 55), "Report an Issue ->", fill=(255, 255, 255), font=font_small_b)

        elif i == 1:
            draw.text((sx + 20, 220), "1. Problem Category", fill=TEXT_DARK, font=font_h2)
            draw.rectangle([sx + 20, 255, sx + phone_w - 20, cy + 30], fill=TEAL_LIGHT, outline=TEAL_PRIMARY)
            draw.text((sx + 35, 265), "✓ Selected: Roads & Potholes", fill=TEAL_PRIMARY, font=font_small_b)
            
            draw.text((sx + 20, 310), "Issue Title:", fill=TEXT_DARK, font=font_small_b)
            draw.rectangle([sx + 20, 330, sx + phone_w - 20, 365], fill=(248, 250, 252), outline=BORDER_COL)
            draw.text((sx + 30, 340), "Severe crater on 4th Ave", fill=TEXT_DARK, font=font_small)

            draw.text((sx + 20, 385), "Urgency Level:", fill=TEXT_DARK, font=font_small_b)
            draw.rectangle([sx + 20, 405, sx + 130, 435], fill=(254, 226, 226), outline=STATUS_OPEN)
            draw.text((sx + 35, 415), "Urgent / Hazard", fill=STATUS_OPEN, font=font_small_b)

            draw.rectangle([sx + 20, 130 + phone_h - 70, sx + phone_w - 20, 130 + phone_h - 25], fill=ACCENT_BLUE)
            draw.text((sx + 75, 130 + phone_h - 55), "Next: Location ->", fill=(255, 255, 255), font=font_small_b)

        elif i == 2:
            draw.text((sx + 20, 215), "2. Pin Location & Photo", fill=TEXT_DARK, font=font_h2)
            # Simulated GPS map
            draw.rectangle([sx + 20, 250, sx + phone_w - 20, 370], fill=(224, 242, 254), outline=(186, 230, 253))
            draw.ellipse([sx + 135, 295, sx + 165, 325], fill=STATUS_OPEN, outline=(255, 255, 255), width=2)
            draw.text((sx + 35, 345), "GPS: 40.7128° N, 74.0060° W", fill=(3, 105, 161), font=font_small_b)

            # Camera box
            draw.rectangle([sx + 20, 390, sx + phone_w - 20, 520], fill=(241, 245, 249), outline=BORDER_COL)
            draw.text((sx + 75, 445), "📷 Photo Evidence\n[pothole_crater.jpg]", fill=TEXT_MUTED, font=font_small)

            draw.rectangle([sx + 20, 130 + phone_h - 70, sx + phone_w - 20, 130 + phone_h - 25], fill=(168, 85, 247))
            draw.text((sx + 65, 130 + phone_h - 55), "Submit Complaint ✓", fill=(255, 255, 255), font=font_small_b)

        elif i == 3:
            draw.rectangle([sx + 20, 215, sx + phone_w - 20, 260], fill=(209, 250, 229))
            draw.text((sx + 35, 228), "Ticket #FMC-103", fill=STATUS_RESOLVED, font=font_h2)

            draw.text((sx + 20, 280), "Live Municipal Status:", fill=TEXT_DARK, font=font_small_b)
            # Stepper
            steps = ["✓ 1. Registered", "✓ 2. Verified by City", "✓ 3. Crew Dispatched", "✓ 4. Fully Resolved"]
            py = 310
            for s in steps:
                draw.rectangle([sx + 20, py, sx + phone_w - 20, py + 30], fill=(240, 253, 250), outline=STATUS_RESOLVED)
                draw.text((sx + 35, py + 7), s, fill=STATUS_RESOLVED, font=font_small_b)
                py += 38

            # Before / After preview
            draw.rectangle([sx + 20, 480, sx + 135, 560], fill=(254, 226, 226))
            draw.text((sx + 30, 515), "Before\n[Damage]", fill=STATUS_OPEN, font=font_small)

            draw.rectangle([sx + 155, 480, sx + phone_w - 20, 560], fill=(209, 250, 229))
            draw.text((sx + 175, 515), "After\n[Fixed]", fill=STATUS_RESOLVED, font=font_small)

        # Draw connection arrow between phones
        if i < 3:
            arr_start_x = sx + phone_w + 5
            arr_end_x = sx + phone_w + 55
            arr_y = 130 + (phone_h // 2)
            draw.line([arr_start_x, arr_y, arr_end_x, arr_y], fill=PROTOTYPE_WIRE, width=3)
            draw.polygon([(arr_end_x + 5, arr_y), (arr_end_x - 7, arr_y - 6), (arr_end_x - 7, arr_y + 6)], fill=PROTOTYPE_WIRE)

        sx += phone_w + 65

    img.save(os.path.join(output_dir, "figma_mobile_user_flow.png"), quality=95)
    print("Created figma_mobile_user_flow.png")

# -------------------------------------------------------------------------
# IMAGE 3: Figma Design System, Style Guide & Component Tokens
# -------------------------------------------------------------------------
def create_design_system():
    w, h = 1400, 900
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([0, 0, w, 90], fill=(15, 23, 42))
    draw.text((40, 25), "Fix My City — UI/UX Design System & Component Library", fill=(255, 255, 255), font=font_title)
    draw.text((40, 60), "Figma Foundations: Color Tokens, Typography Scale, UI Components, & Elevation", fill=TEAL_LIGHT, font=font_small)

    # 1. Color Palette Tokens
    draw.text((40, 120), "1. COLOR TOKENS & PALETTE (Figma Variables)", fill=TEXT_DARK, font=font_h1)
    
    colors = [
        ("Civic Teal (Primary)", "#0D9488", TEAL_PRIMARY),
        ("Teal Subtle", "#CCFBF1", TEAL_LIGHT),
        ("Slate Dark (Header)", "#0F172A", TEXT_DARK),
        ("Status: Open (Red)", "#EF4444", STATUS_OPEN),
        ("Status: In Progress", "#F59E0B", STATUS_PROG),
        ("Status: Resolved", "#10B981", STATUS_RESOLVED),
        ("Card Border", "#E2E8F0", BORDER_COL)
    ]
    cx = 40
    for name, hexcode, rgb in colors:
        draw.rectangle([cx, 160, cx + 160, 240], fill=rgb, outline=(200, 200, 200))
        draw.rectangle([cx, 240, cx + 160, 290], fill=(248, 250, 252), outline=BORDER_COL)
        draw.text((cx + 10, 248), name, fill=TEXT_DARK, font=font_small_b)
        draw.text((cx + 10, 268), hexcode, fill=TEXT_MUTED, font=font_small)
        cx += 185

    # 2. Typography Scale
    draw.text((40, 330), "2. TYPOGRAPHY HIERARCHY (Inter / System Sans)", fill=TEXT_DARK, font=font_h1)
    
    typos = [
        ("Display H1 (Hero)", "32px / Bold 700", "Spotted a problem in your city? Report it."),
        ("Section H2", "24px / SemiBold 600", "Live Neighborhood Complaints Feed"),
        ("Card Title H3", "18px / SemiBold 600", "Deep Dangerous Pothole near School"),
        ("Body Regular", "14px / Regular 400", "Clean water pouring steadily from broken underground conduit."),
        ("Caption / Code", "12px / Medium 500", "Ticket #FMC-101 • 2 hours ago • Ward 4")
    ]
    ty = 370
    for role, specs, sample in typos:
        draw.rectangle([40, ty, 260, ty + 36], fill=(241, 245, 249), outline=BORDER_COL)
        draw.text((50, ty + 10), f"{role} ({specs})", fill=TEXT_DARK, font=font_small_b)
        draw.text((280, ty + 10), sample, fill=TEXT_DARK, font=font_body if "H" in role else font_small)
        ty += 46

    # 3. Interactive UI Components
    draw.text((40, 620), "3. ATOMIC UI COMPONENTS & VARIANTS", fill=TEXT_DARK, font=font_h1)

    # Component Box A: Buttons
    draw.rectangle([40, 660, 420, 850], fill=(248, 250, 252), outline=BORDER_COL)
    draw.text((60, 675), "❖ Component: Action Buttons", fill=TEXT_DARK, font=font_h2)
    # Primary Button
    draw.rectangle([60, 710, 220, 750], fill=TEAL_PRIMARY)
    draw.text((80, 722), "+ Report an Issue", fill=(255, 255, 255), font=font_small_b)
    # Outline Button
    draw.rectangle([240, 710, 390, 750], fill=(255, 255, 255), outline=TEAL_PRIMARY)
    draw.text((260, 722), "Track Status ->", fill=TEAL_PRIMARY, font=font_small_b)
    # Upvote Button
    draw.rectangle([60, 770, 190, 810], fill=(241, 245, 249), outline=BORDER_COL)
    draw.text((75, 782), "👍 42 Upvotes", fill=TEXT_DARK, font=font_small_b)

    # Component Box B: Status Badges
    draw.rectangle([460, 660, 880, 850], fill=(248, 250, 252), outline=BORDER_COL)
    draw.text((480, 675), "❖ Component: Status Badges & Pills", fill=TEXT_DARK, font=font_h2)
    
    # Open badge
    draw.rectangle([480, 720, 620, 755], fill=(254, 226, 226), outline=STATUS_OPEN)
    draw.ellipse([490, 732, 502, 744], fill=STATUS_OPEN)
    draw.text((510, 728), "OPEN / TRIAGE", fill=STATUS_OPEN, font=font_small_b)
    # In Progress badge
    draw.rectangle([640, 720, 800, 755], fill=(254, 243, 199), outline=STATUS_PROG)
    draw.ellipse([650, 732, 662, 744], fill=STATUS_PROG)
    draw.text((670, 728), "IN PROGRESS", fill=STATUS_PROG, font=font_small_b)
    # Resolved badge
    draw.rectangle([480, 775, 640, 810], fill=(209, 250, 229), outline=STATUS_RESOLVED)
    draw.ellipse([490, 787, 502, 799], fill=STATUS_RESOLVED)
    draw.text((510, 783), "RESOLVED ✓", fill=STATUS_RESOLVED, font=font_small_b)

    # Component Box C: 8pt Grid Spec
    draw.rectangle([920, 660, w - 40, 850], fill=(248, 250, 252), outline=BORDER_COL)
    draw.text((940, 675), "❖ Spatial System: 8pt Grid", fill=TEXT_DARK, font=font_h2)
    draw.text((940, 715), "• Spacing 8px: Card inner padding\n• Spacing 16px: Input margins & gutters\n• Spacing 24px: Section dividers\n• Elevation 1: 0 2px 4px rgba(15,23,42,0.06)\n• Elevation 2: 0 12px 24px rgba(15,23,42,0.12)", fill=TEXT_MUTED, font=font_body)

    img.save(os.path.join(output_dir, "figma_design_system.png"), quality=95)
    print("Created figma_design_system.png")

if __name__ == "__main__":
    create_canvas_overview()
    create_mobile_flow()
    create_design_system()
    print("All Figma demonstration images successfully generated!")
