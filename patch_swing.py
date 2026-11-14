
import os, io, base64
from PIL import Image

ASSETS_DIR = r"C:\Users\meyon moyukh\.gemini\antigravity\scratch\mayukhbyte\assets"

def get_b64(path, max_dim=540):
    im = Image.open(path)
    ratio = max_dim / max(im.size)
    if ratio < 1.0:
        im = im.resize((int(im.width * ratio), int(im.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

id_pass_b64 = get_b64(os.path.join(ASSETS_DIR, "id_pass_photo.png"), 520)

FONT_DISPLAY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"

# ==============================================================================
# id-dashboard2.svg
# Pendulum swing via SMIL <animateTransform type="rotate"> — GitHub-safe
# Photo clipped via nested <svg overflow="hidden"> — Blink-safe
# ==============================================================================
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="860" height="450" viewBox="0 0 860 450" fill="none">
<defs>
  <linearGradient id="id-bg" x1="0" y1="0" x2="860" y2="450" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060e22"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="id-border" x1="0" y1="0" x2="860" y2="450" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#ff0055" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.6"/>
  </linearGradient>
  <linearGradient id="metal-clamp" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#475569"/>
    <stop offset="35%" stop-color="#e2e8f0"/>
    <stop offset="70%" stop-color="#94a3b8"/>
    <stop offset="100%" stop-color="#334155"/>
  </linearGradient>
  <linearGradient id="gold-chip" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#fbbf24"/>
    <stop offset="50%" stop-color="#d97706"/>
    <stop offset="100%" stop-color="#f59e0b"/>
  </linearGradient>
</defs>

<rect width="860" height="450" rx="16" fill="url(#id-bg)"/>
<rect x="0.5" y="0.5" width="859" height="449" rx="15.5" stroke="url(#id-border)" stroke-width="1.2"/>

<!-- Ambient background text -->
<text x="20" y="145" fill="#081836" font-family="{FONT_DISPLAY}" font-size="68" font-weight="900">THE</text>

<!-- Fixed anchor plate at top (stays still) -->
<rect x="128" y="0" width="28" height="12" rx="4" fill="url(#metal-clamp)" stroke="#64748b" stroke-width="0.8"/>

<!-- ============================================================
     SWINGING LANYARD GROUP
     Pivot: (142, 0) = top-center of ribbon
     SMIL animateTransform: GitHub renders this, CSS is stripped
     ============================================================ -->
<g>
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="-3.5,142,0; 3.5,142,0; -3.5,142,0"
    dur="3.6s"
    repeatCount="indefinite"
    calcMode="spline"
    keyTimes="0;0.5;1"
    keySplines="0.45 0.05 0.55 0.95;0.45 0.05 0.55 0.95"/>

  <!-- Blue Lanyard Ribbon -->
  <rect x="129" y="0" width="26" height="68" fill="#1d4ed8"/>
  <text x="142" y="44" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="7" font-weight="800"
        transform="rotate(-90 142 44)" letter-spacing="1">MB0510 // BUILDER</text>

  <!-- Metallic Buckle Clasp -->
  <rect x="128" y="62" width="30" height="14" rx="4" fill="url(#metal-clamp)" stroke="#64748b" stroke-width="0.8"/>
  <rect x="136" y="66" width="16" height="6" rx="2" fill="#0a1224"/>

  <!-- ID Pass Card -->
  <g transform="translate(34, 74)">
    <rect width="222" height="318" rx="12" fill="#091428" stroke="#1e293b" stroke-width="1.2"/>
    <!-- Top red accent line -->
    <line x1="16" y1="2" x2="206" y2="2" stroke="#ff0055" stroke-width="2.5" stroke-linecap="round"/>

    <!-- Header row -->
    <text x="14" y="19" fill="#ffffff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800" letter-spacing="0.5">MB / BUILDER PASS</text>
    <text x="208" y="19" text-anchor="end" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">0510</text>

    <!-- Photo box background -->
    <rect x="12" y="28" width="198" height="174" rx="8" fill="#050c1c" stroke="#1e293b"/>

    <!-- Nested SVG for photo clip — works in Blink without clipPath bug -->
    <svg x="12" y="28" width="198" height="174" overflow="hidden">
      <rect width="198" height="174" rx="8" fill="#050c1c"/>
      <image x="0" y="0" width="198" height="174"
             href="data:image/png;base64,{id_pass_b64}"
             xlink:href="data:image/png;base64,{id_pass_b64}"
             preserveAspectRatio="xMidYMid slice"/>
    </svg>

    <!-- Photo frame overlay -->
    <rect x="12" y="28" width="198" height="174" rx="8" fill="none" stroke="#00f0ff" stroke-width="0.8" stroke-opacity="0.5"/>

    <!-- FULL-STACK / AI pill -->
    <rect x="18" y="170" width="118" height="22" rx="11" fill="#0066ff" stroke="#38bdf8" stroke-width="0.8"/>
    <circle cx="30" cy="181" r="3.5" fill="#ffffff"/>
    <text x="41" y="185" fill="#ffffff" font-family="{FONT_MONO}" font-size="9" font-weight="800" letter-spacing="0.5">FULL-STACK / AI</text>

    <!-- Gold SIM Chip (placed first in DOM so text is always on top) -->
    <rect x="170" y="214" width="38" height="28" rx="4" fill="url(#gold-chip)" stroke="#b45309" stroke-width="0.6"/>
    <line x1="170" y1="228" x2="208" y2="228" stroke="#92400e" stroke-width="0.8"/>
    <line x1="189" y1="214" x2="189" y2="242" stroke="#92400e" stroke-width="0.8"/>
    <rect x="181" y="221" width="16" height="14" rx="2" fill="none" stroke="#92400e" stroke-width="0.8"/>

    <!-- Name & Location (stacked, prominent, 100% clear of the SIM chip) -->
    <text x="16" y="218" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="0.5">MAYUKH</text>
    <text x="16" y="232" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="0.5">BHATTACHARJEE</text>
    <text x="16" y="244" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" letter-spacing="0.5">INDIA // DEVELOPER</text>

    <!-- Barcode -->
    <g transform="translate(14, 254)">
      <rect x="0"   y="0" width="2"   height="22" fill="#cbd5e1"/>
      <rect x="4"   y="0" width="4"   height="22" fill="#cbd5e1"/>
      <rect x="11"  y="0" width="1.5" height="22" fill="#cbd5e1"/>
      <rect x="15"  y="0" width="3"   height="22" fill="#cbd5e1"/>
      <rect x="21"  y="0" width="5"   height="22" fill="#cbd5e1"/>
      <rect x="29"  y="0" width="1.5" height="22" fill="#cbd5e1"/>
      <rect x="33"  y="0" width="3"   height="22" fill="#cbd5e1"/>
      <rect x="38"  y="0" width="4.5" height="22" fill="#cbd5e1"/>
      <rect x="45"  y="0" width="2"   height="22" fill="#cbd5e1"/>
      <rect x="49"  y="0" width="6"   height="22" fill="#cbd5e1"/>
      <rect x="58"  y="0" width="1.5" height="22" fill="#cbd5e1"/>
      <rect x="62"  y="0" width="3.5" height="22" fill="#cbd5e1"/>
      <rect x="68"  y="0" width="2"   height="22" fill="#cbd5e1"/>
      <rect x="73"  y="0" width="5"   height="22" fill="#cbd5e1"/>
      <rect x="81"  y="0" width="2"   height="22" fill="#cbd5e1"/>
      <rect x="85"  y="0" width="4"   height="22" fill="#cbd5e1"/>
      <rect x="92"  y="0" width="1.5" height="22" fill="#cbd5e1"/>
      <rect x="96"  y="0" width="3"   height="22" fill="#cbd5e1"/>
      <rect x="101" y="0" width="6"   height="22" fill="#cbd5e1"/>
      <rect x="110" y="0" width="2"   height="22" fill="#cbd5e1"/>
      <rect x="114" y="0" width="4"   height="22" fill="#cbd5e1"/>
      <rect x="121" y="0" width="1.5" height="22" fill="#cbd5e1"/>
      <rect x="125" y="0" width="5"   height="22" fill="#cbd5e1"/>
      <rect x="133" y="0" width="2.5" height="22" fill="#cbd5e1"/>
      <rect x="138" y="0" width="4"   height="22" fill="#cbd5e1"/>
      <rect x="145" y="0" width="2"   height="22" fill="#cbd5e1"/>
      <rect x="150" y="0" width="6"   height="22" fill="#cbd5e1"/>
      <rect x="159" y="0" width="1.5" height="22" fill="#cbd5e1"/>
      <rect x="163" y="0" width="3.5" height="22" fill="#cbd5e1"/>
      <rect x="169" y="0" width="4"   height="22" fill="#cbd5e1"/>
      <rect x="176" y="0" width="2"   height="22" fill="#cbd5e1"/>
      <rect x="181" y="0" width="5"   height="22" fill="#cbd5e1"/>
    </g>

    <!-- INDEPENDENT CREATOR ID footer -->
    <text x="111" y="296" text-anchor="middle" fill="#64748b" font-family="{FONT_MONO}" font-size="7.5" letter-spacing="1">INDEPENDENT CREATOR ID - MB0510</text>
  </g>
</g>

<!-- BEHIND THE CODE. - fixed, doesn't swing -->
<text x="142" y="425" text-anchor="middle" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="21" font-weight="900" letter-spacing="1.5">BEHIND THE CODE.</text>

<!-- ============================================================
     RIGHT: Dashboard — 75 contributions, 14 repos, NO stars
     ============================================================ -->
<g transform="translate(295, 30)">
  <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">04 / BUILDER CREDENTIALS</text>
  <text x="0" y="36" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900">REAL WORK. REAL IMPACT.</text>
  <text x="0" y="54" fill="#64748b" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">PUBLIC SNAPSHOT // 2026</text>

  <!-- 2 Metric Boxes -->
  <rect x="0"   y="70" width="258" height="82" rx="8" fill="#08142c" stroke="#ff0055" stroke-width="1.2" stroke-opacity="0.6"/>
  <text x="18"  y="94" fill="#ff0055" font-family="{FONT_MONO}" font-size="10" font-weight="800" letter-spacing="1">CONTRIBUTIONS</text>
  <text x="18"  y="128" fill="#ff0055" font-family="{FONT_DISPLAY}" font-size="36" font-weight="900">75</text>
  <text x="18"  y="142" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">IN LAST YEAR</text>

  <rect x="272" y="70" width="258" height="82" rx="8" fill="#08142c" stroke="#00f0ff" stroke-width="1.2" stroke-opacity="0.6"/>
  <text x="290" y="94" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10" font-weight="800" letter-spacing="1">REPOSITORIES</text>
  <text x="290" y="128" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="36" font-weight="900">14</text>
  <text x="290" y="142" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">PUBLIC GITHUB</text>

  <!-- Repo bars -->
  <text x="0" y="186" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">MOST-STARRED / PUBLIC REPOSITORIES</text>

  <text x="0"  y="212" fill="#ffffff" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">Paypaal-pro</text>
  <rect x="0"  y="218" width="530" height="9" rx="4.5" fill="#0c1832"/>
  <rect x="0"  y="218" width="508" height="9" rx="4.5" fill="#0070f3"/>

  <text x="0"  y="250" fill="#ffffff" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">ai-educator</text>
  <rect x="0"  y="256" width="530" height="9" rx="4.5" fill="#0c1832"/>
  <rect x="0"  y="256" width="408" height="9" rx="4.5" fill="#0070f3"/>

  <text x="0"  y="288" fill="#ffffff" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">Aizen-detector-url</text>
  <rect x="0"  y="294" width="530" height="9" rx="4.5" fill="#0c1832"/>
  <rect x="0"  y="294" width="308" height="9" rx="4.5" fill="#0070f3"/>

  <!-- NOW Card -->
  <rect x="0"  y="318" width="530" height="66" rx="8" fill="#08142c" stroke="#1e293b"/>
  <rect x="14" y="332" width="38"  height="18" rx="4" fill="#ff0055"/>
  <text x="33" y="344" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="9" font-weight="800">NOW</text>
  <text x="60" y="345" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Building scalable software &amp; AI systems</text>
  <text x="14" y="366" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11">Creator of Paypaal-pro, ai-educator &amp; Aizen-detector-url.</text>
</g>
</svg>'''

out2 = os.path.join(ASSETS_DIR, "id-dashboard2.svg")
with open(out2, "w", encoding="utf-8") as f:
    f.write(svg)
out3 = os.path.join(ASSETS_DIR, "id-dashboard3.svg")
with open(out3, "w", encoding="utf-8") as f:
    f.write(svg)
print("Wrote id-dashboard2.svg and id-dashboard3.svg with SMIL pendulum swing")
