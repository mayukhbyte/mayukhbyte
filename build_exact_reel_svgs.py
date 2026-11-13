import base64
import os
from PIL import Image
import io

ASSETS_DIR = r"C:\Users\meyon moyukh\.gemini\antigravity\scratch\mayukhbyte\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_b64(path, max_dim=520):
    im = Image.open(path)
    ratio = max_dim / max(im.size)
    if ratio < 1.0:
        im = im.resize((int(im.width * ratio), int(im.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

id_b64 = get_b64(os.path.join(ASSETS_DIR, "id.png"), 520)
char_b64 = get_b64(os.path.join(ASSETS_DIR, "right_pointing.png"), 520)

print("Compiling pure neon cyberpunk SVGs with universal radial gradients...")

FONT_DISPLAY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"

# ---------------------------------------------------------------------------
# 1. assets/hero.svg (Deep Neon Dark + Vibrant Glow + Fixed Text Positions)
# ---------------------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="380" viewBox="0 0 860 380" fill="none">
<defs>
  <!-- Deep Cyberpunk Neon Gradient Background -->
  <linearGradient id="h-bg" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="35%" stop-color="#050a18"/>
    <stop offset="70%" stop-color="#081026"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  
  <!-- Vibrant Neon Glowing Border -->
  <linearGradient id="h-border" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9"/>
    <stop offset="45%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="75%" stop-color="#ff0055" stop-opacity="0.6"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.8"/>
  </linearGradient>

  <!-- Glowing Text Gradients -->
  <linearGradient id="h-cyan-glow" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#00f0ff"/>
    <stop offset="50%" stop-color="#38bdf8"/>
    <stop offset="100%" stop-color="#00d2ff"/>
  </linearGradient>

  <!-- Universal Radial Glows -->
  <radialGradient id="h-glow-cyan" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.32"/>
    <stop offset="50%" stop-color="#00d2ff" stop-opacity="0.14"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
  </radialGradient>

  <radialGradient id="h-glow-crimson" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff0055" stop-opacity="0.28"/>
    <stop offset="60%" stop-color="#ff0055" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0"/>
  </radialGradient>

  <radialGradient id="h-glow-blue" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.25"/>
    <stop offset="60%" stop-color="#247bff" stop-opacity="0.06"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
  </radialGradient>

  <!-- Cyberpunk Dot Grid -->
  <pattern id="h-grid" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#00f0ff" fill-opacity="0.13"/>
  </pattern>

  <clipPath id="h-port-clip">
    <rect x="560" y="25" width="260" height="330" rx="18"/>
  </clipPath>
</defs>

<style>
  @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
  .blink-cur {{ animation: blink 1s infinite; }}
</style>

<!-- Neon Base Background -->
<rect width="860" height="380" rx="16" fill="url(#h-bg)"/>
<rect width="860" height="380" rx="16" fill="url(#h-grid)"/>

<!-- Glowing Ambient Lighting -->
<circle cx="680" cy="180" r="190" fill="url(#h-glow-cyan)"/>
<circle cx="750" cy="240" r="160" fill="url(#h-glow-crimson)"/>
<circle cx="200" cy="140" r="180" fill="url(#h-glow-blue)"/>

<!-- Neon Hairline Card Border -->
<rect x="0.5" y="0.5" width="859" height="379" rx="15.5" stroke="url(#h-border)" stroke-width="1.2"/>

<!-- LEFT COLUMN (Safe bounds: x=48 to 440, photo starts at x=560) -->
<!-- Top Tag -->
<g transform="translate(48, 42)">
  <rect width="140" height="25" rx="5" fill="#081329" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.6"/>
  <circle cx="13" cy="12.5" r="3.5" fill="#00f0ff"/>
  <text x="25" y="16.5" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">PORTFOLIO // 2026<tspan class="blink-cur" fill="#ff0055">_</tspan></text>
</g>

<!-- Big Bold Typography matching Reel -->
<!-- Row 1: "MAYUKH" (White) + "///" + "BUILD. BEYOND." positioned SAFELY next to it -->
<g transform="translate(48, 122)">
  <text x="0" y="0" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="46" font-weight="900" letter-spacing="-1">MAYUKH</text>
  
  <!-- "/// BUILD. BEYOND." starts at x=205 and ends at x=315 (245px before photo at x=560!) -->
  <g transform="translate(205, -34)">
    <rect x="0" y="5" width="3.5" height="18" fill="#ff0055" transform="skewX(-20)"/>
    <rect x="6" y="5" width="3.5" height="18" fill="#ff0055" transform="skewX(-20)"/>
    <rect x="12" y="5" width="3.5" height="18" fill="#ff0055" transform="skewX(-20)"/>
    <text x="22" y="14" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="900" letter-spacing="1">BUILD.</text>
    <text x="22" y="26" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="900" letter-spacing="1">BEYOND.</text>
  </g>
</g>

<!-- Row 2: "BHATTACHARJEE" in Radiant Neon Cyan/Blue (Width ~330px, ends at x=378) -->
<g transform="translate(48, 168)">
  <text x="0" y="0" fill="url(#h-cyan-glow)" font-family="{FONT_DISPLAY}" font-size="39" font-weight="900" letter-spacing="-0.5">BHATTACHARJEE</text>
</g>

<!-- Role Subtitle & Bio -->
<text x="48" y="208" fill="#00f0ff" font-family="{FONT_MONO}" font-size="12" font-weight="700" letter-spacing="0.8">FULL-STACK DEVELOPER &amp; AI BUILDER</text>
<text x="48" y="235" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="400">
  Building scalable software, intelligent AI systems &amp; web applications.
</text>
<text x="48" y="257" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="12.5" font-weight="400">
  Creator of ai-educator, Paypaal-pro &amp; aizen-detector.
</text>

<!-- Bottom Metric Pills -->
<g transform="translate(48, 298)">
  <rect x="0" y="0" width="85" height="28" rx="6" fill="#081022" stroke="#1e293b"/>
  <text x="12" y="18" font-size="11">📍</text>
  <text x="30" y="18" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="600">India</text>

  <rect x="95" y="0" width="135" height="28" rx="6" fill="#081022" stroke="#00f0ff" stroke-width="0.8" stroke-opacity="0.5"/>
  <text x="108" y="18" font-size="11">⭐</text>
  <text x="126" y="18" fill="#00f0ff" font-family="{FONT_MONO}" font-size="11" font-weight="700">12 Public Repos</text>

  <rect x="240" y="0" width="145" height="28" rx="6" fill="#081022" stroke="#1e293b"/>
  <circle cx="254" cy="14" r="3.5" fill="#10b981"/>
  <text x="265" y="18" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="600">Open to Projects</text>
</g>

<!-- RIGHT CONTENT: Stylized Photo Cutout with Badge (Starts at x=560) -->
<g>
  <rect x="560" y="25" width="260" height="330" rx="18" fill="#050a16" stroke="#00f0ff" stroke-width="1.2" stroke-opacity="0.6"/>
  <g clip-path="url(#h-port-clip)">
    <image x="555" y="15" width="270" height="345" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
  </g>
  <rect x="560.5" y="25.5" width="259" height="329" rx="17.5" fill="none" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.5"/>
  
  <!-- Overlay Pill Badge centered on photo bottom -->
  <g transform="translate(595, 305)">
    <rect width="190" height="34" rx="8" fill="#060f24" stroke="#00f0ff" stroke-width="1.2"/>
    <rect x="12" y="10" width="4" height="14" fill="#00f0ff" rx="1"/>
    <rect x="18" y="10" width="4" height="14" fill="#ff0055" rx="1"/>
    <text x="28" y="22" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="800" letter-spacing="0.8">ENGINEER / BUILDER</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("wrote assets/hero.svg")

# ---------------------------------------------------------------------------
# 2. assets/about-life.svg (Neon Cyberpunk Dual Card)
# ---------------------------------------------------------------------------
about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="390" viewBox="0 0 860 390" fill="none">
<defs>
  <linearGradient id="ab-bg" x1="0" y1="0" x2="860" y2="390" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060d1f"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="ab-border" x1="0" y1="0" x2="860" y2="390" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#ff0055" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.6"/>
  </linearGradient>
  <radialGradient id="ab-glow-cyan" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.25"/>
    <stop offset="60%" stop-color="#00f0ff" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="ab-glow-crimson" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff0055" stop-opacity="0.22"/>
    <stop offset="60%" stop-color="#ff0055" stop-opacity="0.04"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0"/>
  </radialGradient>
  <pattern id="ab-dots" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#00f0ff" fill-opacity="0.11"/>
  </pattern>
  <clipPath id="thumb-clip">
    <rect x="0" y="0" width="95" height="95" rx="8"/>
  </clipPath>
</defs>

<!-- Outer Container -->
<rect width="860" height="390" rx="16" fill="url(#ab-bg)"/>
<rect width="860" height="390" rx="16" fill="url(#ab-dots)"/>
<circle cx="220" cy="180" r="160" fill="url(#ab-glow-cyan)"/>
<circle cx="640" cy="180" r="160" fill="url(#ab-glow-crimson)"/>
<rect x="0.5" y="0.5" width="859" height="389" rx="15.5" stroke="url(#ab-border)" stroke-width="1.2"/>

<!-- LEFT CARD (x=30, width=385) -->
<g transform="translate(30, 25)">
  <rect width="385" height="340" rx="14" fill="#050a16" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.4"/>
  
  <text x="22" y="28" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">FROM THOUGHT TO THING</text>
  <text x="22" y="54" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="19" font-weight="900" letter-spacing="-0.5">IDEAS. BUILT DIFFERENT.</text>

  <!-- Blue Code-Bar Box -->
  <g transform="translate(22, 70)">
    <rect width="341" height="94" rx="8" fill="#091326" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="14" y="20" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9">github.com / mayukhbyte / build</text>
    <text x="14" y="37" fill="#ffffff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">turn_curiosity_into_impact() {{</text>
    
    <!-- Step Pills -->
    <g transform="translate(14, 50)">
      <rect x="0" y="0" width="80" height="28" rx="5" fill="#0d1f3d" stroke="#00f0ff" stroke-width="0.8"/>
      <text x="8" y="13" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">01</text>
      <text x="8" y="22" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="7.5">CREATE</text>

      <text x="86" y="18" fill="#64748b" font-family="{FONT_DISPLAY}" font-size="11">→</text>

      <rect x="98" y="0" width="90" height="28" rx="5" fill="#0d1f3d" stroke="#00f0ff" stroke-width="0.8"/>
      <text x="106" y="13" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">02</text>
      <text x="106" y="22" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="7.5">ENGINEER</text>

      <text x="194" y="18" fill="#64748b" font-family="{FONT_DISPLAY}" font-size="11">→</text>

      <rect x="206" y="0" width="80" height="28" rx="5" fill="#240e1a" stroke="#ff0055" stroke-width="1.2"/>
      <text x="214" y="13" fill="#ff0055" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">03</text>
      <text x="214" y="22" fill="#ffffff" font-family="{FONT_MONO}" font-size="7.5" font-weight="700">SHIP</text>
    </g>
  </g>

  <!-- 3 Capabilities Rows -->
  <g transform="translate(22, 184)">
    <rect x="0" y="6" width="6" height="2" fill="#00f0ff"/>
    <text x="14" y="10" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12.5" font-weight="800">Modern Web &amp; App Dev</text>
    <text x="14" y="25" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11">From first interaction to production.</text>

    <rect x="0" y="48" width="6" height="2" fill="#38bdf8"/>
    <text x="14" y="52" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12.5" font-weight="800">AI &amp; Cloud Integration</text>
    <text x="14" y="67" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11">Scalable systems. Useful intelligence.</text>

    <rect x="0" y="90" width="6" height="2" fill="#ff0055"/>
    <text x="14" y="94" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12.5" font-weight="800">Autonomous Fintech &amp; Security</text>
    <text x="14" y="109" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11">Concurrent Go crawling &amp; dispute automation.</text>
  </g>
</g>

<!-- RIGHT CARD (x=445, width=385) -->
<g transform="translate(445, 25)">
  <rect width="385" height="340" rx="14" fill="#050a16" stroke="#ff0055" stroke-width="1" stroke-opacity="0.4"/>
  
  <text x="22" y="28" fill="#ff0055" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">02 / LIFE OUTSIDE THE COMMIT</text>
  <text x="22" y="54" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="19" font-weight="900" letter-spacing="-0.5">MORE THAN A JOB TITLE.</text>
  <rect x="22" y="62" width="28" height="2.5" fill="#00f0ff"/>
  <rect x="52" y="62" width="16" height="2.5" fill="#ff0055"/>

  <!-- Upper Subsection -->
  <g transform="translate(22, 76)">
    <!-- Photo Thumbnail -->
    <g>
      <rect width="95" height="95" rx="8" fill="#0d1424" stroke="#00f0ff" stroke-width="0.8"/>
      <g clip-path="url(#thumb-clip)">
        <image x="-5" y="-5" width="105" height="105" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
      </g>
      <rect y="74" width="95" height="21" rx="0" fill="#050a16" opacity="0.9"/>
      <text x="47" y="88" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="7.5" font-weight="700">MAYUKH / BUILDER</text>
    </g>

    <!-- 3 Red Steps -->
    <g transform="translate(115, 8)">
      <text x="0" y="14" fill="#ff0055" font-family="{FONT_MONO}" font-size="10.5" font-weight="800">01</text>
      <text x="24" y="14" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="800" letter-spacing="0.5">FIND THE GAP</text>

      <text x="0" y="44" fill="#ff0055" font-family="{FONT_MONO}" font-size="10.5" font-weight="800">02</text>
      <text x="24" y="44" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="800" letter-spacing="0.5">BUILD YOUR FLAG</text>

      <text x="0" y="74" fill="#ff0055" font-family="{FONT_MONO}" font-size="10.5" font-weight="800">03</text>
      <text x="24" y="74" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="800" letter-spacing="0.5">TAKE THE LEAP</text>
    </g>
  </g>

  <!-- Lower Subsection -->
  <g transform="translate(22, 205)">
    <line x1="0" y1="0" x2="341" y2="0" stroke="#1e293b"/>
    <text x="0" y="24" fill="#64748b" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">MAKE THE NEXT MOVE.</text>
    <text x="0" y="50" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="17" font-weight="900">1:1 Engineering &amp; Collab</text>
    <text x="0" y="70" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">A clearer roadmap. A stronger engineer.</text>
    <text x="0" y="94" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700">01 / 03</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "about-life.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)
print("wrote assets/about-life.svg")

# ---------------------------------------------------------------------------
# 3. assets/stack.svg (Neon Engine Room)
# ---------------------------------------------------------------------------
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="420" viewBox="0 0 860 420" fill="none">
<defs>
  <linearGradient id="st-bg" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060d1f"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="st-border" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#ff0055" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.6"/>
  </linearGradient>
  <radialGradient id="st-glow-cyan" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.25"/>
    <stop offset="60%" stop-color="#00f0ff" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="st-glow-crimson" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff0055" stop-opacity="0.22"/>
    <stop offset="60%" stop-color="#ff0055" stop-opacity="0.04"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0"/>
  </radialGradient>
  <pattern id="st-dots" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#00f0ff" fill-opacity="0.11"/>
  </pattern>
</defs>

<style>
  @keyframes orb-pulse {{ 0%, 100% {{ opacity: 0.35; }} 50% {{ opacity: 0.85; }} }}
  .orbit-track {{ animation: orb-pulse 4s ease-in-out infinite; }}
</style>

<rect width="860" height="420" rx="16" fill="url(#st-bg)"/>
<rect width="860" height="420" rx="16" fill="url(#st-dots)"/>
<circle cx="215" cy="240" r="160" fill="url(#st-glow-cyan)"/>
<circle cx="600" cy="220" r="160" fill="url(#st-glow-crimson)"/>
<rect x="0.5" y="0.5" width="859" height="419" rx="15.5" stroke="url(#st-border)" stroke-width="1.2"/>

<!-- Header -->
<g transform="translate(45, 36)">
  <text x="0" y="0" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">03 / MY ENGINE ROOM</text>
  <text x="0" y="28" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">TOOLS CHANGE. CURIOSITY DOESN'T.</text>
  <text x="0" y="46" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="2">LANGUAGES / SYSTEMS / INTELLIGENCE</text>
</g>

<!-- LEFT: Planetary Atom Orbits (Center at x=215, y=240) -->
<g transform="translate(215, 240)">
  <ellipse class="orbit-track" cx="0" cy="0" rx="150" ry="65" fill="none" stroke="#00f0ff" stroke-width="1.4" stroke-opacity="0.5" transform="rotate(-25)"/>
  <ellipse class="orbit-track" cx="0" cy="0" rx="140" ry="55" fill="none" stroke="#ff0055" stroke-width="1.4" stroke-opacity="0.45" transform="rotate(25)"/>
  <ellipse class="orbit-track" cx="0" cy="0" rx="110" ry="42" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-opacity="0.6" transform="rotate(-65)"/>

  <!-- Nucleus Hexagon -->
  <polygon points="0,-26 22,-13 22,13 0,26 -22,13 -22,-13" fill="#050a16" stroke="#00f0ff" stroke-width="2"/>
  <polygon points="0,-16 14,-8 14,8 0,16 -14,8 -14,-8" fill="#0d1f3d"/>
  <text x="0" y="5" text-anchor="middle" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="1">MB</text>

  <!-- Nodes -->
  <g transform="translate(-120, -32)">
    <circle cx="0" cy="0" r="14" fill="#050a16" stroke="#00f0ff" stroke-width="1.4"/>
    <text x="0" y="4" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">Py</text>
  </g>
  <g transform="translate(115, 28)">
    <circle cx="0" cy="0" r="14" fill="#050a16" stroke="#00ADD8" stroke-width="1.4"/>
    <text x="0" y="4" text-anchor="middle" fill="#00ADD8" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">Go</text>
  </g>
  <g transform="translate(-55, 60)">
    <circle cx="0" cy="0" r="14" fill="#050a16" stroke="#61DAFB" stroke-width="1.4"/>
    <text x="0" y="4" text-anchor="middle" fill="#61DAFB" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">Re</text>
  </g>
  <g transform="translate(65, -55)">
    <circle cx="0" cy="0" r="14" fill="#050a16" stroke="#34d399" stroke-width="1.4"/>
    <text x="0" y="4" text-anchor="middle" fill="#34d399" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">No</text>
  </g>

  <text x="0" y="145" text-anchor="middle" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700" letter-spacing="1">CODE IS THE TOOL. IMPACT IS THE POINT.</text>
</g>

<!-- RIGHT: Categorized Tech Chips (Starts at x=445) -->
<g transform="translate(445, 110)">
  <!-- 01 / LANGUAGES -->
  <text x="0" y="12" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">01 / LANGUAGES</text>
  <g transform="translate(0, 22)">
    <rect x="0" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="12" y="20" font-size="12">🐍</text>
    <text x="34" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">Python</text>

    <rect x="122" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="134" y="20" font-size="12">🐹</text>
    <text x="156" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">Golang</text>

    <rect x="244" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="256" y="20" font-size="12">📘</text>
    <text x="278" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">TypeScript</text>
  </g>

  <!-- 02 / FRONTEND & RUNTIME -->
  <text x="0" y="80" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">02 / FRONTEND &amp; RUNTIME</text>
  <g transform="translate(0, 90)">
    <rect x="0" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="12" y="20" font-size="12">⚛️</text>
    <text x="34" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">React 18</text>

    <rect x="122" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="134" y="20" font-size="12">▲</text>
    <text x="156" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">Next.js</text>

    <rect x="244" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="256" y="20" font-size="12">🔥</text>
    <text x="278" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">SvelteKit</text>
  </g>

  <!-- 03 / BACKEND, CLOUD & AI -->
  <text x="0" y="148" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">03 / BACKEND, CLOUD &amp; AI</text>
  <g transform="translate(0, 158)">
    <rect x="0" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="12" y="20" font-size="12">🟢</text>
    <text x="34" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">Node / Gin</text>

    <rect x="122" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="134" y="20" font-size="12">👁️</text>
    <text x="156" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">OpenCV</text>

    <rect x="244" y="0" width="112" height="32" rx="6" fill="#081022" stroke="#1e293b"/>
    <text x="256" y="20" font-size="12">⚡</text>
    <text x="278" y="20" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11" font-weight="700">Supabase</text>
  </g>

  <text x="0" y="230" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9" font-weight="700" letter-spacing="1">BUILD / MENTOR / CREATE / REPEAT</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "stack.svg"), "w", encoding="utf-8") as f:
    f.write(stack_svg)
print("wrote assets/stack.svg")

# ---------------------------------------------------------------------------
# 4. assets/projects-table.svg (Dark Neon Projects Table matching Image 3!)
# ---------------------------------------------------------------------------
projects_table_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="230" viewBox="0 0 860 230" fill="none">
<defs>
  <linearGradient id="pt-bg" x1="0" y1="0" x2="860" y2="230" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060d1f"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="pt-border" x1="0" y1="0" x2="860" y2="230" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#247bff" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0.6"/>
  </linearGradient>
</defs>

<rect width="860" height="230" rx="14" fill="url(#pt-bg)"/>
<rect x="0.5" y="0.5" width="859" height="229" rx="13.5" stroke="url(#pt-border)" stroke-width="1.2"/>

<!-- Table Header Row -->
<rect x="20" y="16" width="820" height="38" rx="6" fill="#071024" stroke="#00f0ff" stroke-width="0.8" stroke-opacity="0.5"/>
<text x="40" y="40" fill="#00f0ff" font-family="{FONT_MONO}" font-size="11" font-weight="800" letter-spacing="1">PROJECT</text>
<text x="210" y="40" fill="#00f0ff" font-family="{FONT_MONO}" font-size="11" font-weight="800" letter-spacing="1">WHAT IT DOES</text>
<text x="700" y="40" fill="#00f0ff" font-family="{FONT_MONO}" font-size="11" font-weight="800" letter-spacing="1">FOCUS</text>

<!-- Row 1: ai-educator -->
<g transform="translate(20, 60)">
  <rect width="820" height="46" rx="6" fill="#050a16" stroke="#1e293b"/>
  <text x="20" y="28" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">ai-educator</text>
  <text x="190" y="28" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="12">AI tutoring system with multi-level doubt solving &amp; adaptive quizzes</text>
  <rect x="670" y="11" width="130" height="24" rx="4" fill="#081730" stroke="#00f0ff" stroke-width="0.8"/>
  <text x="735" y="27" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">AI + Learning</text>
</g>

<!-- Row 2: Paypaal-pro -->
<g transform="translate(20, 112)">
  <rect width="820" height="46" rx="6" fill="#050a16" stroke="#1e293b"/>
  <text x="20" y="28" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">Paypaal-pro</text>
  <text x="190" y="28" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="12">Autonomous agent financial operations engine with AI dispute synthesis</text>
  <rect x="670" y="11" width="130" height="24" rx="4" fill="#240c1a" stroke="#ff0055" stroke-width="0.8"/>
  <text x="735" y="27" text-anchor="middle" fill="#ff0055" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">Fintech + Agents</text>
</g>

<!-- Row 3: aizen-detector -->
<g transform="translate(20, 164)">
  <rect width="820" height="46" rx="6" fill="#050a16" stroke="#1e293b"/>
  <text x="20" y="28" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">aizen-detector</text>
  <text x="190" y="28" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="12">Real-time URL threat crawler with 21 concurrent Go goroutines &amp; 39 signals</text>
  <rect x="670" y="11" width="130" height="24" rx="4" fill="#081e18" stroke="#34d399" stroke-width="0.8"/>
  <text x="735" y="27" text-anchor="middle" fill="#34d399" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">Security + Go</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "projects-table.svg"), "w", encoding="utf-8") as f:
    f.write(projects_table_svg)
print("wrote assets/projects-table.svg")

# ---------------------------------------------------------------------------
# 5. assets/id-dashboard.svg (Neon Lanyard Card & Dashboard)
# ---------------------------------------------------------------------------
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="430" viewBox="0 0 860 430" fill="none">
<defs>
  <linearGradient id="id-bg" x1="0" y1="0" x2="860" y2="430" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060d1f"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="id-border" x1="0" y1="0" x2="860" y2="430" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#ff0055" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.6"/>
  </linearGradient>
  <radialGradient id="id-glow-cyan" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.25"/>
    <stop offset="60%" stop-color="#00f0ff" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="id-glow-crimson" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff0055" stop-opacity="0.22"/>
    <stop offset="60%" stop-color="#ff0055" stop-opacity="0.04"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0"/>
  </radialGradient>
  <clipPath id="lanyard-port">
    <rect x="18" y="52" width="164" height="145" rx="8"/>
  </clipPath>
  <linearGradient id="foil-shine" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="45%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="50%" stop-color="#ffffff" stop-opacity="0.4"/>
    <stop offset="55%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
  </linearGradient>
</defs>

<style>
  @keyframes swing {{
    0% {{ transform: rotate(0deg); }}
    50% {{ transform: rotate(1.7deg); }}
    100% {{ transform: rotate(-1.7deg); }}
  }}
  @keyframes foil {{
    0% {{ transform: translateX(-200px); }}
    35%, 100% {{ transform: translateX(250px); }}
  }}
  .lanyard-card {{
    transform-origin: 145px 0px;
    animation: swing 5s ease-in-out infinite alternate;
  }}
  .foil-sweep {{
    animation: foil 6s ease-in-out infinite;
  }}
</style>

<rect width="860" height="430" rx="16" fill="url(#id-bg)"/>
<circle cx="150" cy="200" r="160" fill="url(#id-glow-cyan)"/>
<circle cx="650" cy="220" r="180" fill="url(#id-glow-crimson)"/>
<rect x="0.5" y="0.5" width="859" height="429" rx="15.5" stroke="url(#id-border)" stroke-width="1.2"/>

<!-- Header -->
<g transform="translate(45, 34)">
  <text x="0" y="0" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">04 / BUILDER CREDENTIALS</text>
  <text x="0" y="26" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">REAL WORK. REAL IMPACT.</text>
  <text x="0" y="44" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="2">PUBLIC SNAPSHOT // 2026</text>
</g>

<!-- LEFT: Lanyard Card -->
<g class="lanyard-card">
  <rect x="135" y="0" width="22" height="32" fill="#061229" rx="2"/>
  <line x1="146" y1="0" x2="146" y2="32" stroke="#00f0ff" stroke-width="2"/>
  <text x="146" y="20" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="7" font-weight="700" transform="rotate(90, 146, 20)">MAYUKH</text>

  <rect x="128" y="30" width="36" height="14" rx="3" fill="#64748b" stroke="#cbd5e1" stroke-width="0.8"/>
  <circle cx="146" cy="37" r="3.5" fill="#1e293b"/>
  <ellipse cx="146" cy="48" rx="7" ry="7" fill="none" stroke="#94a3b8" stroke-width="3"/>

  <!-- ID Badge Body (200 x 310) -->
  <g transform="translate(45, 54)">
    <rect width="200" height="310" rx="14" fill="#060d1c" stroke="#ff0055" stroke-width="1.2"/>
    <rect width="200" height="310" rx="14" fill="#0a142c" opacity="0.6"/>

    <rect width="200" height="32" rx="14" fill="#09142b"/>
    <text x="18" y="21" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="800" letter-spacing="1">MB / BUILDER PASS</text>
    <text x="182" y="21" text-anchor="end" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10" font-weight="800">0510</text>
    <line x1="0" y1="32" x2="200" y2="32" stroke="#1e293b"/>

    <rect x="18" y="44" width="164" height="150" rx="8" fill="#040813" stroke="#1e293b"/>
    <g clip-path="url(#lanyard-port)">
      <image x="18" y="38" width="164" height="160" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
    </g>
    <g transform="translate(24, 168)">
      <rect width="95" height="18" rx="4" fill="#08152e" stroke="#00f0ff" stroke-width="0.8"/>
      <text x="47" y="12" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">FULL-STACK / AI</text>
    </g>

    <!-- Name: Font size 12 so "MAYUKH BHATTACHARJEE" never overflows -->
    <text x="18" y="214" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="0.2">MAYUKH BHATTACHARJEE</text>
    <text x="18" y="228" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="700">INDIA // DEVELOPER</text>

    <!-- Golden SIM Microchip -->
    <g transform="translate(150, 218)">
      <rect width="32" height="24" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="0.8"/>
      <line x1="16" y1="0" x2="16" y2="24" stroke="#d97706" stroke-width="1"/>
      <line x1="0" y1="12" x2="32" y2="12" stroke="#d97706" stroke-width="1"/>
    </g>

    <!-- Barcode -->
    <g transform="translate(18, 252)">
      <rect x="0" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="4" y="0" width="4" height="24" fill="#94a3b8"/>
      <rect x="11" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="15" y="0" width="5" height="24" fill="#94a3b8"/>
      <rect x="23" y="0" width="1" height="24" fill="#94a3b8"/>
      <rect x="27" y="0" width="3" height="24" fill="#94a3b8"/>
      <rect x="33" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="38" y="0" width="4" height="24" fill="#94a3b8"/>
      <rect x="45" y="0" width="1" height="24" fill="#94a3b8"/>
      <rect x="48" y="0" width="5" height="24" fill="#94a3b8"/>
      <rect x="56" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="61" y="0" width="4" height="24" fill="#94a3b8"/>
      <rect x="68" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="73" y="0" width="5" height="24" fill="#94a3b8"/>
      <rect x="81" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="86" y="0" width="4" height="24" fill="#94a3b8"/>
      <rect x="93" y="0" width="1" height="24" fill="#94a3b8"/>
      <rect x="97" y="0" width="4" height="24" fill="#94a3b8"/>
      <rect x="104" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="109" y="0" width="5" height="24" fill="#94a3b8"/>
      <rect x="117" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="122" y="0" width="3" height="24" fill="#94a3b8"/>
      <rect x="128" y="0" width="4" height="24" fill="#94a3b8"/>
      <rect x="135" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="140" y="0" width="4" height="24" fill="#94a3b8"/>
      <rect x="147" y="0" width="3" height="24" fill="#94a3b8"/>
      <rect x="153" y="0" width="2" height="24" fill="#94a3b8"/>
      <rect x="158" y="0" width="4" height="24" fill="#94a3b8"/>
    </g>
    <text x="100" y="292" text-anchor="middle" fill="#64748b" font-family="{FONT_MONO}" font-size="7.5" letter-spacing="1">MB-2026-AUTH-PASS-SECURED</text>

    <!-- Foil Shine -->
    <g clip-path="url(#lanyard-port)">
      <rect class="foil-sweep" x="0" y="44" width="80" height="150" fill="url(#foil-shine)"/>
    </g>
  </g>
</g>

<!-- RIGHT: Dashboard Grid (Starts at x=285, ends safely at x=819) -->
<g transform="translate(285, 95)">
  <!-- 3 Metric Boxes -->
  <g transform="translate(0, 0)">
    <rect width="170" height="85" rx="8" fill="#050a16" stroke="#ff0055" stroke-width="1" stroke-opacity="0.5"/>
    <text x="14" y="24" fill="#ff0055" font-family="{FONT_MONO}" font-size="9" font-weight="700">FEATURED</text>
    <text x="14" y="58" fill="#ff0055" font-family="{FONT_DISPLAY}" font-size="32" font-weight="900">3</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="8.5">FLAGSHIP PLATFORMS</text>
  </g>

  <g transform="translate(182, 0)">
    <rect width="170" height="85" rx="8" fill="#050a16" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="14" y="24" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9" font-weight="700">REPOSITORIES</text>
    <text x="14" y="58" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="32" font-weight="900">12</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="8.5">PUBLIC ACTIVE</text>
  </g>

  <g transform="translate(364, 0)">
    <rect width="170" height="85" rx="8" fill="#050a16" stroke="#1e293b"/>
    <text x="14" y="24" fill="#94a3b8" font-family="{FONT_MONO}" font-size="9" font-weight="700">CONTRIBUTIONS</text>
    <text x="14" y="58" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="32" font-weight="900">64+</text>
    <text x="14" y="74" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="8.5">ANNUAL METRICS</text>
  </g>

  <!-- Middle: MOST-STARRED / PUBLIC REPOSITORIES -->
  <g transform="translate(0, 108)">
    <text x="0" y="14" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">MOST-STARRED / PUBLIC REPOSITORIES</text>
    <text x="520" y="14" fill="#ff0055" font-size="12">★</text>

    <!-- Bar 1: ai-educator -->
    <g transform="translate(0, 26)">
      <text x="0" y="12" fill="#ffffff" font-family="{FONT_MONO}" font-size="11">ai-educator</text>
      <text x="520" y="12" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">3</text>
      <rect x="0" y="18" width="510" height="7" rx="3.5" fill="#0a142c"/>
      <rect x="0" y="18" width="460" height="7" rx="3.5" fill="#00f0ff"/>
    </g>

    <!-- Bar 2: Paypaal-pro -->
    <g transform="translate(0, 62)">
      <text x="0" y="12" fill="#ffffff" font-family="{FONT_MONO}" font-size="11">Paypaal-pro</text>
      <text x="520" y="12" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">2</text>
      <rect x="0" y="18" width="510" height="7" rx="3.5" fill="#0a142c"/>
      <rect x="0" y="18" width="370" height="7" rx="3.5" fill="#247bff"/>
    </g>

    <!-- Bar 3: aizen-detector -->
    <g transform="translate(0, 98)">
      <text x="0" y="12" fill="#ffffff" font-family="{FONT_MONO}" font-size="11">aizen-detector</text>
      <text x="520" y="12" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">2</text>
      <rect x="0" y="18" width="510" height="7" rx="3.5" fill="#0a142c"/>
      <rect x="0" y="18" width="290" height="7" rx="3.5" fill="#34d399"/>
    </g>
  </g>

  <!-- Bottom: Announcement Card -->
  <g transform="translate(0, 240)">
    <rect width="534" height="64" rx="8" fill="#071228" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.4"/>
    <rect x="14" y="14" width="38" height="18" rx="4" fill="#ff0055"/>
    <text x="33" y="26" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="9" font-weight="800">NOW</text>
    
    <text x="60" y="27" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Building scalable software &amp; AI systems</text>
    <text x="14" y="48" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11">Open to high-impact engineering roles, full-stack builds &amp; open source.</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "id-dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(id_dashboard_svg)
print("wrote assets/id-dashboard.svg")

# ---------------------------------------------------------------------------
# 6. assets/connect.svg (Neon Connect Card)
# ---------------------------------------------------------------------------
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="320" viewBox="0 0 860 320" fill="none">
<defs>
  <linearGradient id="cn-bg" x1="0" y1="0" x2="860" y2="320" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060d1f"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="cn-border" x1="0" y1="0" x2="860" y2="320" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#ff0055" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.6"/>
  </linearGradient>
  <radialGradient id="cn-glow-cyan" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.25"/>
    <stop offset="60%" stop-color="#00f0ff" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="cn-glow-crimson" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff0055" stop-opacity="0.22"/>
    <stop offset="60%" stop-color="#ff0055" stop-opacity="0.04"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0"/>
  </radialGradient>
  <clipPath id="cn-char-clip">
    <rect x="25" y="20" width="265" height="280" rx="14"/>
  </clipPath>
</defs>

<style>
  @keyframes nudge {{ 0%, 100% {{ transform: translateX(0); }} 50% {{ transform: translateX(6px); }} }}
  .nudge-arrow {{ animation: nudge 1.8s ease-in-out infinite; }}
</style>

<rect width="860" height="320" rx="16" fill="url(#cn-bg)"/>
<circle cx="160" cy="160" r="160" fill="url(#cn-glow-cyan)"/>
<circle cx="650" cy="160" r="180" fill="url(#cn-glow-crimson)"/>
<rect x="0.5" y="0.5" width="859" height="319" rx="15.5" stroke="url(#cn-border)" stroke-width="1.2"/>

<!-- Left: Character pointing towards connect buttons -->
<g clip-path="url(#cn-char-clip)">
  <image x="15" y="10" width="280" height="300" href="data:image/png;base64,{char_b64}" preserveAspectRatio="xMidYMid slice"/>
</g>
<rect x="24" y="19" width="267" height="282" rx="14" fill="none" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.4"/>

<!-- Header -->
<g transform="translate(320, 32)">
  <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">05 / START A CONVERSATION</text>
  <text x="0" y="36" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">BUILD SOMETHING GREAT.</text>
  <text x="0" y="56" fill="#64748b" font-family="{FONT_MONO}" font-size="11" font-weight="700">Ideas. Opportunities. Your next move.</text>
</g>

<!-- Social Cards -->
<g transform="translate(320, 110)">
  <!-- LinkedIn Card (Top) -->
  <g transform="translate(0, 0)">
    <rect width="495" height="54" rx="8" fill="#071226" stroke="#0A66C2" stroke-width="1.2"/>
    <rect x="14" y="11" width="32" height="32" rx="6" fill="#0A66C2"/>
    <text x="30" y="32" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="16" font-weight="900">in</text>
    
    <text x="58" y="24" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">LinkedIn Profile</text>
    <text x="58" y="41" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10">Mayukh Bhattacharjee · Connect Professionally</text>
    
    <g class="nudge-arrow" transform="translate(458, 32)">
      <text x="0" y="0" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
    </g>
  </g>

  <!-- GitHub Card (Middle) -->
  <g transform="translate(0, 66)">
    <rect width="495" height="54" rx="8" fill="#071226" stroke="#00f0ff" stroke-width="1"/>
    <rect x="14" y="11" width="32" height="32" rx="6" fill="#1e293b"/>
    <text x="30" y="32" text-anchor="middle" fill="#ffffff" font-size="16">🐙</text>
    
    <text x="58" y="24" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">GitHub Profile</text>
    <text x="58" y="41" fill="#94a3b8" font-family="{FONT_MONO}" font-size="10">@mayukhbyte · Repositories, commits &amp; architecture</text>
    
    <g class="nudge-arrow" transform="translate(458, 32)">
      <text x="0" y="0" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
    </g>
  </g>

  <!-- Email Card (Bottom) -->
  <g transform="translate(0, 132)">
    <rect width="495" height="54" rx="8" fill="#071226" stroke="#ff0055" stroke-width="1"/>
    <rect x="14" y="11" width="32" height="32" rx="6" fill="#ff0055"/>
    <text x="30" y="32" text-anchor="middle" fill="#ffffff" font-size="15">✉️</text>
    
    <text x="58" y="24" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Direct Inquiries</text>
    <text x="58" y="41" fill="#94a3b8" font-family="{FONT_MONO}" font-size="10">mayukhbhttchrj@gmail.com · Collaborations</text>
    
    <g class="nudge-arrow" transform="translate(458, 32)">
      <text x="0" y="0" fill="#ff0055" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
    </g>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "connect.svg"), "w", encoding="utf-8") as f:
    f.write(connect_svg)
print("wrote assets/connect.svg")

print("All 6 neon cyberpunk SVGs compiled successfully!")
