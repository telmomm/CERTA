#!/usr/bin/env python3
"""Generates the CERTA visual identity PNGs from the palette of `visual-identity.png`.

Usage, from the repository root:  python3 docs/assets/generate.py
Requires `rsvg-convert` (librsvg) and the Avenir Next font. Standard library only.
"""
import math
import random
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
NAVY, TEAL, BLUE, SKY, ICE = "#0B2D4A", "#00BFA5", "#00AEEF", "#A7E3F7", "#E6EEF6"
NIGHT = "#071E33"
FONT = "font-family=\"Avenir Next, Avenir, Helvetica Neue, Arial, sans-serif\""


# --- Parts ----------------------------------------------------------------

def c_arc(cx, cy, r, opening):
    """C-shaped arc open to the right by `opening` degrees on each side."""
    a = math.radians(opening)
    x, dy = cx + r * math.cos(a), r * math.sin(a)
    return f"M{x:.1f},{cy - dy:.1f} A{r},{r} 0 1 0 {x:.1f},{cy + dy:.1f}"


def mark(x=0, y=0, scale=1.0, dark=False, uid="m"):
    """Logo mark (210x200 box). `dark` is the variant for dark backgrounds."""
    outer = f"url(#{uid}e)" if dark else NAVY
    traces = [
        ("M122,82 L146,58 H170", (178, 58)),
        ("M112,94 H184", (192, 94)),
        ("M96,118 H184", (192, 118)),
        ("M134,118 L156,140 H164", (172, 140)),
    ]
    strokes = "".join(f'<path d="{d}"/><circle cx="{cx}" cy="{cy}" r="6.5"/>' for d, (cx, cy) in traces)
    return f"""<g transform="translate({x},{y}) scale({scale})" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <defs>
    <linearGradient id="{uid}e" gradientUnits="userSpaceOnUse" x1="20" y1="20" x2="120" y2="190">
      <stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="#0A6FB8"/></linearGradient>
    <linearGradient id="{uid}i" gradientUnits="userSpaceOnUse" x1="50" y1="150" x2="140" y2="50">
      <stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
    <linearGradient id="{uid}p" gradientUnits="userSpaceOnUse" x1="120" y1="0" x2="200" y2="0">
      <stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
  </defs>
  <path d="{c_arc(100, 100, 80, 48)}" stroke="{outer}" stroke-width="24" stroke-linecap="butt"/>
  <path d="{c_arc(100, 100, 48, 52)}" stroke="url(#{uid}i)" stroke-width="12" stroke-linecap="butt"/>
  <g stroke="url(#{uid}p)" stroke-width="5">{strokes}</g>
  <path d="M70,100 L90,120 L130,74" stroke="{TEAL}" stroke-width="13"/>
</g>"""


ICONS = {
    "certification": '<path d="M48,10 L80,22 V46 C80,66 67,80 48,88 C29,80 16,66 16,46 V22 Z"/>'
                     '<path d="M34,48 L44,58 L63,37"/>',
    "embedded": '<rect x="26" y="26" width="44" height="44" rx="6"/><rect x="40" y="40" width="16" height="16" rx="2"/>'
                + "".join(f'<path d="M{p},12 V26 M{p},70 V84 M12,{p} H26 M70,{p} H84"/>' for p in (36, 48, 60)),
    "risk": '<path d="M48,14 L86,80 H10 Z"/><path d="M48,38 V58"/><path d="M48,69 V70"/>',
    "test": '<path d="M8,50 H28 L37,30 L47,76 L58,16 L66,58 L72,50 H88"/>',
}
LABELS = {"certification": "Certification", "embedded": "Embedded", "risk": "Risk-aware", "test": "Test design"}
ICON_BOX = {"certification": (NAVY, "#fff"), "embedded": (TEAL, "#fff"), "risk": (BLUE, "#fff"), "test": (SKY, NAVY)}


def icon(name, x=0, y=0, size=96, color=NAVY, width=5):
    return (f'<g transform="translate({x},{y}) scale({size / 96})" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


def text(x, y, s, size, weight=500, color="#fff", extra=""):
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{s}</text>'


def icon_row(x, y, step, size=34, font_size=17, color="#fff"):
    out = []
    for i, n in enumerate(ICONS):
        xi = x + i * step
        out.append(icon(n, xi, y, size, color, 6))
        out.append(text(xi + size + 12, y + size / 2 + font_size * 0.35, LABELS[n], font_size, 500, color))
        if i:
            out.append(f'<path d="M{xi - 18},{y - 2} V{y + size + 2}" stroke="{BLUE}" stroke-opacity=".45" stroke-width="1.5"/>')
    return "".join(out)


def deco_traces(w, h, n, seed, color=BLUE, opacity=0.5, side="right"):
    """Decorative circuit traces that enter from one side and end in a node."""
    rnd = random.Random(seed)
    s = -1 if side == "right" else 1
    x0 = w if side == "right" else 0
    out = []
    for i in range(n):
        y = h * (i + 0.5) / n + rnd.uniform(-0.3, 0.3) * h / n
        l1, d, l2 = rnd.uniform(0.04, 0.16) * w, rnd.choice((-1, 1)) * rnd.uniform(0.03, 0.09) * h, rnd.uniform(0.02, 0.10) * w
        x1, x2, y2 = x0 + s * l1, x0 + s * (l1 + abs(d)), y + d
        x3 = x2 + s * l2
        out.append(f'<path d="M{x0},{y:.0f} H{x1:.0f} L{x2:.0f},{y2:.0f} H{x3:.0f}"/>'
                   f'<circle cx="{x3 + s * 6:.0f}" cy="{y2:.0f}" r="6"/>')
    return (f'<g fill="none" stroke="{color}" stroke-opacity="{opacity}" stroke-width="2.5" '
            f'stroke-linecap="round" stroke-linejoin="round">{"".join(out)}</g>')


def spectrum(x0, x1, base, height, peaks, color, opacity, filled=False):
    """Frequency-response-like curve: sum of Gaussian peaks (centre, width, weight)."""
    pts = []
    for i in range(161):
        t = i / 160
        v = sum(p * math.exp(-((t - c) / a) ** 2) for c, a, p in peaks)
        pts.append(f"{x0 + t * (x1 - x0):.1f},{base - v * height:.1f}")
    d = "M" + " L".join(pts)
    if filled:
        return f'<path d="{d} L{x1},{base} L{x0},{base} Z" fill="{color}" fill-opacity="{opacity}"/>'
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-opacity="{opacity}" stroke-width="2.5" stroke-linejoin="round"/>'


def chip(cx, cy, side, color=SKY):
    """Integrated circuit with pins and traces to nodes, as the central motif."""
    m, n = side / 2, 5
    pat = "".join(
        f'<path d="M{cx - m + (i + 1) * side / (n + 1):.0f},{cy - m - 16} v16 M{cx - m + (i + 1) * side / (n + 1):.0f},{cy + m} v16 '
        f'M{cx - m - 16},{cy - m + (i + 1) * side / (n + 1):.0f} h16 M{cx + m},{cy - m + (i + 1) * side / (n + 1):.0f} h16"/>'
        for i in range(n))
    branches = [(-1, -40, -110, -60), (-1, 30, -150, 40), (1, -30, 120, -70), (1, 40, 150, 60), (-1, 0, -90, 0), (1, 0, 80, 0)]
    traces = ""
    for s, dy, lx, ly in branches:
        xa, ya = cx + s * (m + 16), cy + dy
        xb = xa + s * 30
        xc, yc = xb + s * abs(ly - dy), cy + ly
        xd = cx + lx + s * (m + 60)
        traces += f'<path d="M{xa},{ya} H{xb} L{xc},{yc} H{xd}"/><circle cx="{xd + s * 6}" cy="{yc}" r="6"/>'
    return f"""<g fill="none" stroke-linecap="round" stroke-linejoin="round">
  <g stroke="{TEAL}" stroke-width="2.5" stroke-opacity=".8">{traces}</g>
  <rect x="{cx - m}" y="{cy - m}" width="{side}" height="{side}" rx="12" fill="{NIGHT}" fill-opacity=".85" stroke="{color}" stroke-width="3"/>
  <rect x="{cx - m * .5}" y="{cy - m * .5}" width="{m}" height="{m}" rx="6" stroke="{BLUE}" stroke-width="2.5"/>
  <g stroke="{color}" stroke-width="3">{pat}</g>
  <path d="M{cx - 16},{cy} l11,11 l22,-24" stroke="{TEAL}" stroke-width="6"/>
</g>"""


def dark_background(w, h, uid="f", focus=(0.8, 0.45)):
    return f"""<defs>
  <linearGradient id="{uid}l" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NIGHT}"/><stop offset=".55" stop-color="{NAVY}"/><stop offset="1" stop-color="#0E4168"/></linearGradient>
  <radialGradient id="{uid}r" cx="{focus[0]}" cy="{focus[1]}" r=".55">
    <stop offset="0" stop-color="{BLUE}" stop-opacity=".30"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
  <pattern id="{uid}p" width="32" height="32" patternUnits="userSpaceOnUse">
    <circle cx="16" cy="16" r="1.2" fill="{SKY}" fill-opacity=".16"/></pattern>
</defs>
<rect width="{w}" height="{h}" fill="url(#{uid}l)"/><rect width="{w}" height="{h}" fill="url(#{uid}p)"/>
<rect width="{w}" height="{h}" fill="url(#{uid}r)"/>"""


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'


PEAKS_A = [(0.25, 0.07, 0.95), (0.55, 0.12, 0.45), (0.82, 0.08, 0.6)]
PEAKS_B = [(0.35, 0.10, 0.6), (0.68, 0.09, 0.85)]


# --- Compositions ---------------------------------------------------------

def logo(dark):
    c = "#fff" if dark else NAVY
    return svg(760, 240, mark(20, 20, 1.0, dark)
               + text(244, 112, "CERTA", 104, 800, c, 'letter-spacing="1"')
               + text(248, 156, "Certified, Embedded, Risk-aware", 27, 500, c)
               + text(248, 190, "Test design for ", 27, 500, c)
               .replace("</text>", f'<tspan fill="{TEAL}">Analog circuits</tspan></text>'))


def banner_github():
    w, h = 1280, 400
    return svg(w, h, dark_background(w, h)
               + spectrum(700, w, h, 230, PEAKS_A, BLUE, 0.10, True) + spectrum(700, w, h, 230, PEAKS_A, BLUE, 0.55)
               + spectrum(700, w, h, 190, PEAKS_B, TEAL, 0.08, True) + spectrum(700, w, h, 190, PEAKS_B, TEAL, 0.55)
               + chip(985, 180, 120)
               + mark(56, 44, 0.64, True)
               + text(204, 112, "CERTA", 82, 800, "#fff", 'letter-spacing="1"')
               + text(206, 150, "Certified, Embedded, Risk-aware", 24, 500)
               + text(206, 182, "Test design for ", 24, 500).replace("</text>", f'<tspan fill="{TEAL}">Analog circuits</tspan></text>')
               + text(60, 246, "Smarter test design for more reliable analog systems.", 20, 400, SKY)
               + f'<path d="M60,272 h44" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>'
               + icon_row(60, 312, 172))


def banner_social():
    w, h = 1280, 640
    return svg(w, h, dark_background(w, h, focus=(0.78, 0.5))
               + spectrum(640, w, h, 340, PEAKS_A, BLUE, 0.10, True) + spectrum(640, w, h, 340, PEAKS_A, BLUE, 0.55)
               + spectrum(640, w, h, 280, PEAKS_B, TEAL, 0.08, True) + spectrum(640, w, h, 280, PEAKS_B, TEAL, 0.55)
               + chip(985, 290, 150)
               + mark(72, 96, 0.8, True)
               + text(258, 190, "CERTA", 104, 800, "#fff", 'letter-spacing="1"')
               + text(76, 316, "Certified, Embedded, Risk-aware", 32, 500)
               + text(76, 358, "Test design for ", 32, 500).replace("</text>", f'<tspan fill="{TEAL}">Analog circuits</tspan></text>')
               + text(76, 424, "Smarter test design for more reliable analog systems.", 21, 400, SKY)
               + f'<path d="M76,456 h52" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>'
               + icon_row(76, 516, 168, 32, 16))


def banner_square():
    w = h = 1080
    return svg(w, h, dark_background(w, h, focus=(0.7, 0.75))
               + spectrum(0, w, h, 300, PEAKS_A, BLUE, 0.10, True) + spectrum(0, w, h, 300, PEAKS_A, BLUE, 0.5)
               + spectrum(0, w, h, 240, PEAKS_B, TEAL, 0.08, True) + spectrum(0, w, h, 240, PEAKS_B, TEAL, 0.5)
               + deco_traces(w, h * 0.5, 5, 3, TEAL, 0.35)
               + mark(80, 96, 0.95, True)
               + text(296, 232, "CERTA", 128, 800, "#fff", 'letter-spacing="1"')
               + text(84, 380, "Certified, Embedded,", 50, 500)
               + text(84, 442, "Risk-aware Test design", 50, 500)
               + text(84, 504, "for ", 50, 500).replace("</text>", f'<tspan fill="{TEAL}">Analog circuits</tspan></text>')
               + f'<path d="M84,552 h64" stroke="{TEAL}" stroke-width="5" stroke-linecap="round"/>'
               + text(84, 612, "Research project", 30, 400, SKY)
               + icon_row(84, 700, 236, 40, 22))


def background(light):
    w, h = 1920, 1080
    if light:
        base = (f'<rect width="{w}" height="{h}" fill="#F6FAFD"/>'
                + spectrum(0, w, h, 420, PEAKS_A, BLUE, 0.07, True) + spectrum(0, w, h, 330, PEAKS_B, TEAL, 0.07, True)
                + deco_traces(w, h, 9, 5, BLUE, 0.22) + deco_traces(w, h, 9, 9, TEAL, 0.22, "left"))
    else:
        base = (dark_background(w, h, focus=(0.5, 0.6))
                + spectrum(0, w, h, 420, PEAKS_A, BLUE, 0.10, True) + spectrum(0, w, h, 420, PEAKS_A, BLUE, 0.35)
                + spectrum(0, w, h, 330, PEAKS_B, TEAL, 0.08, True) + spectrum(0, w, h, 330, PEAKS_B, TEAL, 0.35)
                + deco_traces(w, h, 9, 5, BLUE, 0.35) + deco_traces(w, h, 9, 9, TEAL, 0.35, "left"))
    return svg(w, h, base)


def divider():
    w, h = 1280, 48
    return svg(w, h, f"""<defs><linearGradient id="s" x1="0" x2="1"><stop offset="0" stop-color="{TEAL}" stop-opacity="0"/>
  <stop offset=".35" stop-color="{TEAL}"/><stop offset=".65" stop-color="{BLUE}"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></linearGradient></defs>
<path d="M0,24 H580 L592,12 L606,40 L622,4 L636,34 L646,24 H1280" fill="none" stroke="url(#s)" stroke-width="3"
  stroke-linecap="round" stroke-linejoin="round"/>""")


def outputs():
    yield "logo/certa-logo.png", logo(False), 2
    yield "logo/certa-logo-dark.png", logo(True), 2
    yield "logo/certa-mark.png", svg(210, 200, mark()), 4
    yield "logo/certa-mark-dark.png", svg(210, 200, mark(dark=True)), 4
    fav = f'<rect width="256" height="256" rx="56" fill="{NAVY}"/>' + mark(31, 33, 0.95, True)
    yield "logo/certa-favicon.png", svg(256, 256, fav), 2
    yield "banners/certa-banner-github.png", banner_github(), 2
    yield "banners/certa-banner-social.png", banner_social(), 1
    yield "banners/certa-banner-square.png", banner_square(), 1
    yield "backgrounds/certa-background-dark.png", background(False), 1
    yield "backgrounds/certa-background-light.png", background(True), 1
    yield "backgrounds/certa-divider.png", divider(), 2
    for n in ICONS:
        yield f"icons/{n}.png", svg(96, 96, icon(n)), 4
        yield f"icons/{n}-white.png", svg(96, 96, icon(n, color="#fff")), 4
        bg, fg = ICON_BOX[n]
        yield f"icons/{n}-box.png", svg(128, 128, f'<rect width="128" height="128" rx="14" fill="{bg}"/>' + icon(n, 24, 24, 80, fg)), 4


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        for path, content, zoom in outputs():
            target = HERE / path
            target.parent.mkdir(exist_ok=True)
            source = Path(tmp) / (target.stem + ".svg")
            source.write_text(content, encoding="utf-8")
            subprocess.run(["rsvg-convert", "-z", str(zoom), "-o", str(target), str(source)], check=True)
            print(path)
