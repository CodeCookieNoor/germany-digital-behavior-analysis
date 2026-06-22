from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap


OUT = Path("tableau_workbook_extract/Image/insights_dashboard.png")
W, H = 1920, 1080


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


BG = "#fbfbff"
SIDEBAR = "#f7f1f6"
NAV_PINK = "#eaa5b0"
NAV_PURPLE = "#c4bdf0"
NAV_TEAL = "#b9e5ec"
TEXT = "#07112f"
MUTED = "#33415c"
CARD = "#ffffff"
LINE = "#e6e3ef"
PURPLE = "#6f45e8"
PINK = "#ff4d8d"
TEAL = "#079ca0"
ORANGE = "#fa5f15"
BLUE = "#1d5bc3"


def rounded(draw, xy, fill, outline=LINE, radius=18, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, size=24, fill=TEXT, bold=False, anchor=None):
    draw.text(xy, value, fill=fill, font=font(size, bold), anchor=anchor)


def wrapped(draw, xy, value, size=22, fill=MUTED, width=55, line_gap=8, bold=False):
    x, y = xy
    for line in textwrap.wrap(value, width=width):
        draw.text((x, y), line, fill=fill, font=font(size, bold))
        y += size + line_gap
    return y


def icon_box(draw, xy, color, symbol):
    x, y = xy
    rounded(draw, (x, y, x + 72, y + 72), fill=color + "22", outline=color + "33", radius=18, width=1)
    text(draw, (x + 36, y + 35), symbol, size=34, fill=color, bold=True, anchor="mm")


def panel(draw, xy, title, items, accent):
    x1, y1, x2, y2 = xy
    rounded(draw, xy, fill=CARD, outline=LINE, radius=16, width=2)
    text(draw, (x1 + 28, y1 + 26), title, size=26, fill=TEXT, bold=True)
    y = y1 + 80
    for heading, body, color, sym in items:
        rounded(draw, (x1 + 24, y, x2 - 24, y + 122), fill="#fbfdff", outline="#ece8f5", radius=14, width=1)
        icon_box(draw, (x1 + 48, y + 25), color, sym)
        text(draw, (x1 + 142, y + 26), heading, size=22, fill=color, bold=True)
        wrapped(draw, (x1 + 142, y + 58), body, size=18, fill=TEXT, width=62)
        y += 142


def recommendation(draw, xy, number, title, body, color, symbol):
    x1, y1, x2, y2 = xy
    rounded(draw, xy, fill="#ffffff", outline=color + "55", radius=14, width=1)
    icon_box(draw, (x1 + 22, y1 + 24), color, symbol)
    text(draw, (x1 + 112, y1 + 26), f"{number}. {title}", size=20, fill=color, bold=True)
    wrapped(draw, (x1 + 112, y1 + 58), body, size=17, fill=TEXT, width=34)


img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Sidebar
rounded(draw, (0, 0, 215, H), fill=SIDEBAR, outline="#ddd6e9", radius=16, width=2)
rounded(draw, (76, 32, 144, 100), fill="#fff0fb", outline="#e6d9fb", radius=14, width=1)
text(draw, (110, 66), "H", size=40, fill=PURPLE, bold=True, anchor="mm")
rounded(draw, (38, 166, 178, 228), fill=NAV_PINK, outline="#ed7f6f", radius=10, width=2)
text(draw, (108, 198), "Overview", size=18, fill="#ffffff", bold=True, anchor="mm")
rounded(draw, (38, 242, 178, 304), fill=NAV_PURPLE, outline="#b9b0e5", radius=10, width=2)
text(draw, (108, 274), "Demographics", size=18, fill="#ffffff", bold=True, anchor="mm")
rounded(draw, (38, 318, 178, 380), fill=NAV_TEAL, outline="#8ed0da", radius=10, width=2)
text(draw, (108, 350), "Insights", size=18, fill="#ffffff", bold=True, anchor="mm")
rounded(draw, (42, 905, 182, 1010), fill="#faf5f9", outline="#eadfeb", radius=12, width=1)
text(draw, (112, 930), "Data Source", size=17, fill="#000000", bold=True, anchor="mm")
text(draw, (112, 958), "Eurostat Data", size=15, fill="#000000", anchor="mm")
text(draw, (112, 982), "2020 - 2025", size=15, fill="#000000", anchor="mm")

# Header
text(draw, (250, 42), "Germany Digital Insights & Recommendations", size=34, fill=TEXT, bold=True)
text(draw, (250, 86), "Key takeaways from digital behavior and e-commerce analysis, 2020 - 2025", size=20, fill=MUTED)
rounded(draw, (1498, 34, 1668, 88), fill="#ffffff", outline="#e8e8f3", radius=16, width=1)
text(draw, (1583, 62), "2020 - 2025", size=18, fill="#244a83", bold=True, anchor="mm")
rounded(draw, (1685, 34, 1855, 88), fill="#b4b4b4", outline="#c5c5c5", radius=10, width=1)
text(draw, (1770, 62), "Download PDF", size=18, fill="#ffffff", bold=True, anchor="mm")

# Panels
panel(
    draw,
    (240, 125, 1040, 585),
    "Key Insights",
    [
        ("Email leads the digital landscape", "Email remains the most adopted digital activity across the full period, with participation staying above other online behaviors.", PURPLE, "@"),
        ("Product search supports e-commerce", "Product information search is an important step before online buying and helps explain the positive digital-commerce relationship.", TEAL, "?"),
        ("Adults 25-54 are the core drivers", "The 25-54 group shows the most balanced digital and e-commerce engagement across the dashboard.", ORANGE, "25"),
    ],
    PURPLE,
)
panel(
    draw,
    (1060, 125, 1860, 585),
    "Opportunities to Focus On",
    [
        ("Grow e-commerce adoption", "E-commerce activity remains lower than general digital activity, creating a clear growth opportunity.", PINK, "$"),
        ("Leverage high education segment", "Highly educated individuals show stronger engagement and can act as early adopters for digital services.", PURPLE, "^"),
        ("Bridge the age gap", "Older users show lower participation, indicating the need for digital literacy and simpler online experiences.", TEAL, "!"),
    ],
    PINK,
)

# Recommendations
rounded(draw, (240, 610, 1860, 835), fill=CARD, outline=LINE, radius=16, width=2)
text(draw, (268, 638), "Strategic Recommendations", size=26, fill=TEXT, bold=True)
recommendation(draw, (265, 690, 640, 810), "1", "Focus on 25-54 age group", "Prioritize marketing and engagement campaigns toward the strongest balanced segment.", PURPLE, "1")
recommendation(draw, (665, 690, 1040, 810), "2", "Use email as core channel", "Email has the highest adoption rate and should support communication and retention.", TEAL, "2")
recommendation(draw, (1065, 690, 1440, 810), "3", "Invest in product discovery", "Improve product information, reviews, and search experience to convert searchers into buyers.", ORANGE, "3")
recommendation(draw, (1465, 690, 1840, 810), "4", "Promote digital inclusion", "Design simpler online journeys for older adults to increase confidence and participation.", PINK, "4")

# Summary
rounded(draw, (240, 865, 1860, 1015), fill="#f1efff", outline="#e1dafd", radius=16, width=2)
icon_box(draw, (270, 905), PURPLE, "*")
text(draw, (370, 912), "Executive Summary:", size=24, fill=PURPLE, bold=True)
wrapped(
    draw,
    (590, 912),
    "Germany demonstrates strong digital adoption, led by email usage. The 25-54 age group and highly educated individuals drive much of the digital engagement and e-commerce activity. Product information search appears especially important for online purchasing, making it a valuable area for digital marketing investment and user experience optimization.",
    size=19,
    fill=TEXT,
    width=105,
)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
