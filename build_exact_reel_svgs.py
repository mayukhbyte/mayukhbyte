import base64
import os
from PIL import Image
import io

ASSETS_DIR = r"C:\Users\meyon moyukh\.gemini\antigravity\scratch\mayukhbyte\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_b64(path, max_dim=500):
    im = Image.open(path)
    ratio = max_dim / max(im.size)
    if ratio < 1.0:
        im = im.resize((int(im.width * ratio), int(im.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

id_b64 = get_b64(os.path.join(ASSETS_DIR, "id.png"), 520)
char_b64 = get_b64(os.path.join(ASSETS_DIR, "right_pointing.png"), 520)

print("Compiling pixel-perfect SVGs matching the Instagram Reel...")

# Common font styling: system-ui with condensed/impact weights
FONT_DISPLAY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"

# ---------------------------------------------------------------------------
# 1. assets/hero.svg (Matches Image 1 top)
# ---------------------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="380" viewBox="0 0 860 380" fill="none">
<defs>
  <linearGradient id="h-bg" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#050813"/>
    <stop offset="60%" stop-color="#090f1f"/>
    <stop offset="100%" stop-color="#050813"/>
  </linearGradient>
  <linearGradient id="h-border" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.6"/>
    <stop offset="60%" stop-color="#ff354f" stop-opacity="0.25"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0.4"/>
  </linearGradient>
  <linearGradient id="h-blue-glow" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#247bff"/>
    <stop offset="100%" stop-color="#00d2ff"/>
  </linearGradient>
  <pattern id="h-grid" width="24" height="24" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12"/>
  </pattern>
  <clipPath id="h-port-clip">
    <rect x="550" y="25" width="275" height="325" rx="18"/>
  </clipPath>
</defs>

<style>
  @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
  @keyframes pulse-ring {{ 0%, 100% {{ opacity: 0.3; }} 50% {{ opacity: 0.7; }} }}
  .blink-cur {{ animation: blink 1s infinite; }}
  .glow-ring {{ animation: pulse-ring 4s ease-in-out infinite; }}
</style>

<!-- Card Base -->
<rect width="860" height="380" rx="16" fill="url(#h-bg)"/>
<rect width="860" height="380" rx="16" fill="url(#h-grid)"/>
<rect x="0.5" y="0.5" width="859" height="379" rx="15.5" stroke="url(#h-border)" stroke-width="1"/>

<!-- Background Ambient Light -->
<circle cx="680" cy="180" r="160" fill="#247bff" opacity="0.14" filter="blur(40px)"/>
<circle cx="740" cy="220" r="120" fill="#ff354f" opacity="0.08" filter="blur(30px)"/>

<!-- LEFT CONTENT -->
<!-- Top Tag -->
<g transform="translate(50, 48)">
  <rect width="130" height="24" rx="4" fill="#0d172e" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.4"/>
  <circle cx="12" cy="12" r="3.5" fill="#247bff"/>
  <text x="24" y="16" fill="#94a3b8" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">PORTFOLIO // 2026<tspan class="blink-cur" fill="#ff354f">_</tspan></text>
</g>

<!-- Big Bold Typography matching Reel: "MAYUKH" (White) "BHATTACHARJEE" (Electric Blue) + BUILD. BEYOND. + /// -->
<g transform="translate(50, 135)">
  <text x="0" y="0" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="56" font-weight="900" letter-spacing="-1.5">MAYUKH</text>
  <text x="0" y="52" fill="url(#h-blue-glow)" font-family="{FONT_DISPLAY}" font-size="54" font-weight="900" letter-spacing="-1">BHATTACHARJEE</text>
  
  <!-- "BUILD. BEYOND." + Crimson slashes "///" -->
  <g transform="translate(435, 12)">
    <rect x="0" y="0" width="4" height="18" fill="#ff354f" transform="skewX(-20)"/>
    <rect x="7" y="0" width="4" height="18" fill="#ff354f" transform="skewX(-20)"/>
    <rect x="14" y="0" width="4" height="18" fill="#ff354f" transform="skewX(-20)"/>
    <text x="24" y="8" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="11" font-weight="900" letter-spacing="1">BUILD.</text>
    <text x="24" y="20" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11" font-weight="900" letter-spacing="1">BEYOND.</text>
  </g>
</g>

<!-- Role Subtitle & Bio -->
<text x="50" y="228" fill="#38bdf8" font-family="{FONT_MONO}" font-size="13" font-weight="700" letter-spacing="0.5">FULL-STACK DEVELOPER &amp; AI BUILDER</text>
<text x="50" y="254" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="14.5" font-weight="400">
  Building scalable software, intelligent AI systems &amp; high-performance web apps.
</text>
<text x="50" y="276" fill="#64748b" font-family="{FONT_DISPLAY}" font-size="13" font-weight="400">
  Creator of ai-educator, Paypaal-pro &amp; aizen-detector.
</text>

<!-- Bottom Metric Pills -->
<g transform="translate(50, 310)">
  <rect x="0" y="0" width="100" height="30" rx="6" fill="#0b1324" stroke="#1e293b"/>
  <text x="14" y="19" font-size="11">📍</text>
  <text x="32" y="19" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="600">India</text>

  <rect x="110" y="0" width="140" height="30" rx="6" fill="#0b1324" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.4"/>
  <text x="124" y="19" font-size="11">⭐</text>
  <text x="144" y="19" fill="#38bdf8" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">12 Public Repos</text>

  <rect x="260" y="0" width="150" height="30" rx="6" fill="#0b1324" stroke="#1e293b"/>
  <circle cx="274" cy="15" r="3.5" fill="#10b981"/>
  <text x="286" y="19" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="600">Open to Projects</text>
</g>

<!-- RIGHT CONTENT: Stylized Photo Cutout with Badge matching Reel -->
<g>
  <rect x="550" y="25" width="275" height="325" rx="18" fill="#080e1d" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.4"/>
  <g clip-path="url(#h-port-clip)">
    <image x="545" y="15" width="285" height="340" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
  </g>
  <!-- Inner gradient rim light -->
  <rect x="550.5" y="25.5" width="274" height="324" rx="17.5" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.3"/>
  
  <!-- Overlay Pill Badge (exact match to Reel: "ENGINEER / BUILDER" in blue pill) -->
  <g transform="translate(565, 298)">
    <rect width="180" height="34" rx="8" fill="#0b162c" stroke="#247bff" stroke-width="1.2" filter="drop-shadow(0 4px 10px rgba(0,0,0,0.6))"/>
    <rect x="12" y="10" width="4" height="14" fill="#247bff" rx="1"/>
    <rect x="18" y="10" width="4" height="14" fill="#ff354f" rx="1"/>
    <text x="30" y="22" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="800" letter-spacing="0.8">ENGINEER / BUILDER</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("wrote assets/hero.svg")

# ---------------------------------------------------------------------------
# 2. assets/about-life.svg (Matches Image 1 bottom: Two side-by-side cards)
# ---------------------------------------------------------------------------
about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="390" viewBox="0 0 860 390" fill="none">
<defs>
  <linearGradient id="ab-bg" x1="0" y1="0" x2="860" y2="390" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#050813"/>
    <stop offset="100%" stop-color="#090f1f"/>
  </linearGradient>
  <linearGradient id="ab-border" x1="0" y1="0" x2="860" y2="390" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0.2"/>
  </linearGradient>
  <pattern id="ab-dots" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.1"/>
  </pattern>
  <clipPath id="thumb-clip">
    <rect x="0" y="0" width="110" height="110" rx="10"/>
  </clipPath>
</defs>

<!-- Outer Container -->
<rect width="860" height="390" rx="16" fill="url(#ab-bg)"/>
<rect width="860" height="390" rx="16" fill="url(#ab-dots)"/>
<rect x="0.5" y="0.5" width="859" height="389" rx="15.5" stroke="url(#ab-border)" stroke-width="1"/>

<!-- LEFT CARD: "FROM THOUGHT TO THING" / "IDEAS. BUILT DIFFERENT." -->
<g transform="translate(30, 25)">
  <rect width="385" height="340" rx="14" fill="#080e1c" stroke="#1e293b"/>
  
  <!-- Header -->
  <text x="24" y="30" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">FROM THOUGHT TO THING</text>
  <text x="24" y="58" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="20" font-weight="900" letter-spacing="-0.5">IDEAS. BUILT DIFFERENT.</text>

  <!-- Blue Code-Bar Box: github.com/mayukhbyte / build -->
  <g transform="translate(24, 76)">
    <rect width="337" height="96" rx="10" fill="#0d172e" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>
    <text x="14" y="20" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9.5">github.com / mayukhbyte / build</text>
    <text x="14" y="38" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="11" font-weight="700">turn_curiosity_into_impact() {{</text>
    
    <!-- Step Pills: [01 CREATE] -> [02 ENGINEER] -> [03 SHIP] (Red outline on 03 as in Reel!) -->
    <g transform="translate(14, 52)">
      <!-- 01 CREATE -->
      <rect x="0" y="0" width="85" height="30" rx="6" fill="#132140" stroke="#247bff" stroke-width="0.8"/>
      <text x="10" y="14" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9" font-weight="800">01</text>
      <text x="10" y="24" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="8">CREATE</text>

      <!-- Arrow -->
      <text x="91" y="20" fill="#64748b" font-family="{FONT_DISPLAY}" font-size="12">→</text>

      <!-- 02 ENGINEER -->
      <rect x="105" y="0" width="95" height="30" rx="6" fill="#132140" stroke="#247bff" stroke-width="0.8"/>
      <text x="115" y="14" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9" font-weight="800">02</text>
      <text x="115" y="24" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="8">ENGINEER</text>

      <!-- Arrow -->
      <text x="206" y="20" fill="#64748b" font-family="{FONT_DISPLAY}" font-size="12">→</text>

      <!-- 03 SHIP (Highlighted with crimson border as in Reel) -->
      <rect x="220" y="0" width="85" height="30" rx="6" fill="#1f1422" stroke="#ff354f" stroke-width="1.2"/>
      <text x="230" y="14" fill="#ff354f" font-family="{FONT_MONO}" font-size="9" font-weight="800">03</text>
      <text x="230" y="24" fill="#ffffff" font-family="{FONT_MONO}" font-size="8" font-weight="700">SHIP</text>
    </g>
  </g>

  <!-- 3 Capabilities Rows matching Reel -->
  <g transform="translate(24, 192)">
    <!-- Row 1 -->
    <rect x="0" y="6" width="6" height="2" fill="#247bff"/>
    <text x="14" y="10" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Modern Web &amp; App Dev</text>
    <text x="14" y="26" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">From first interaction to production.</text>

    <!-- Row 2 -->
    <rect x="0" y="52" width="6" height="2" fill="#38bdf8"/>
    <text x="14" y="56" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">AI &amp; Cloud Integration</text>
    <text x="14" y="72" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">Scalable systems. Useful intelligence.</text>

    <!-- Row 3 -->
    <rect x="0" y="98" width="6" height="2" fill="#ff354f"/>
    <text x="14" y="102" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Autonomous Fintech &amp; Security</text>
    <text x="14" y="118" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">Concurrent Go crawling &amp; dispute automation.</text>
  </g>
</g>

<!-- RIGHT CARD: "02 / LIFE OUTSIDE THE COMMIT" / "MORE THAN A JOB TITLE." -->
<g transform="translate(445, 25)">
  <rect width="385" height="340" rx="14" fill="#080e1c" stroke="#1e293b"/>
  
  <!-- Header -->
  <text x="24" y="30" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">02 / LIFE OUTSIDE THE COMMIT</text>
  <text x="24" y="58" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="20" font-weight="900" letter-spacing="-0.5">MORE THAN A JOB TITLE.</text>
  <!-- Accent line under title -->
  <rect x="24" y="66" width="30" height="2.5" fill="#247bff"/>
  <rect x="56" y="66" width="18" height="2.5" fill="#ff354f"/>

  <!-- Upper Subsection: Photo Thumbnail + 3 Red Steps (exact match to Reel) -->
  <g transform="translate(24, 82)">
    <!-- Photo Thumbnail -->
    <g>
      <rect width="110" height="110" rx="10" fill="#0d1424" stroke="#247bff" stroke-width="0.8"/>
      <g clip-path="url(#thumb-clip)">
        <image x="-5" y="-5" width="120" height="120" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
      </g>
      <rect y="86" width="110" height="24" rx="0" fill="#090f1e" opacity="0.9"/>
      <text x="55" y="102" text-anchor="middle" fill="#38bdf8" font-family="{FONT_MONO}" font-size="8" font-weight="700">MAYUKH / BUILDER</text>
    </g>

    <!-- 3 Red Steps matching Reel -->
    <g transform="translate(130, 16)">
      <!-- 01 FIND THE GAP -->
      <text x="0" y="14" fill="#ff354f" font-family="{FONT_MONO}" font-size="11" font-weight="800">01</text>
      <text x="26" y="14" fill="#e2e8f0" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800" letter-spacing="0.5">FIND THE GAP</text>

      <!-- 02 BUILD YOUR FLAG -->
      <text x="0" y="48" fill="#ff354f" font-family="{FONT_MONO}" font-size="11" font-weight="800">02</text>
      <text x="26" y="48" fill="#e2e8f0" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800" letter-spacing="0.5">BUILD YOUR FLAG</text>

      <!-- 03 TAKE THE LEAP -->
      <text x="0" y="82" fill="#ff354f" font-family="{FONT_MONO}" font-size="11" font-weight="800">03</text>
      <text x="26" y="82" fill="#e2e8f0" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800" letter-spacing="0.5">TAKE THE LEAP</text>
    </g>
  </g>

  <!-- Lower Subsection: MAKE THE NEXT MOVE. -->
  <g transform="translate(24, 218)">
    <line x1="0" y1="0" x2="337" y2="0" stroke="#1e293b"/>
    <text x="0" y="24" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">MAKE THE NEXT MOVE.</text>
    <text x="0" y="52" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="18" font-weight="900">1:1 Engineering &amp; Collab</text>
    <text x="0" y="74" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="12">A clearer roadmap. A stronger engineer.</text>
    <text x="0" y="98" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="700">01 / 03</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "about-life.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)
print("wrote assets/about-life.svg")

# ---------------------------------------------------------------------------
# 3. assets/stack.svg (Matches Image 2: "TOOLS CHANGE. CURIOSITY DOESN'T.")
# ---------------------------------------------------------------------------
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="420" viewBox="0 0 860 420" fill="none">
<defs>
  <linearGradient id="st-bg" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#050813"/>
    <stop offset="100%" stop-color="#090f1f"/>
  </linearGradient>
  <linearGradient id="st-border" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="50%" stop-color="#ff354f" stop-opacity="0.25"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0.4"/>
  </linearGradient>
  <pattern id="st-dots" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.08"/>
  </pattern>
</defs>

<style>
  @keyframes orb-spin {{
    0% {{ transform: rotate(0deg); }}
    100% {{ transform: rotate(360deg); }}
  }}
  @keyframes orb-pulse {{
    0%, 100% {{ opacity: 0.3; }}
    50% {{ opacity: 0.8; }}
  }}
  .orbit-track {{ animation: orb-pulse 4s ease-in-out infinite; }}
</style>

<rect width="860" height="420" rx="16" fill="url(#st-bg)"/>
<rect width="860" height="420" rx="16" fill="url(#st-dots)"/>
<rect x="0.5" y="0.5" width="859" height="419" rx="15.5" stroke="url(#st-border)" stroke-width="1"/>

<!-- Header matching Reel: "03 / MY ENGINE ROOM" / "TOOLS CHANGE. CURIOSITY DOESN'T." -->
<g transform="translate(45, 36)">
  <text x="0" y="0" fill="#247bff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">03 / MY ENGINE ROOM</text>
  <text x="0" y="28" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">TOOLS CHANGE. CURIOSITY DOESN'T.</text>
  <text x="0" y="46" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="2">LANGUAGES / SYSTEMS / INTELLIGENCE</text>
</g>

<!-- SPLIT LAYOUT -->
<!-- LEFT: Planetary Atom Orbits with Central [ MB ] Hexagon Nucleus -->
<g transform="translate(225, 245)">
  <!-- Glow Core -->
  <circle cx="0" cy="0" r="110" fill="#247bff" opacity="0.08" filter="blur(30px)"/>

  <!-- Orbits matching Reel -->
  <ellipse class="orbit-track" cx="0" cy="0" rx="160" ry="70" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.4" transform="rotate(-25)"/>
  <ellipse class="orbit-track" cx="0" cy="0" rx="150" ry="60" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.35" transform="rotate(25)"/>
  <ellipse class="orbit-track" cx="0" cy="0" rx="120" ry="45" fill="none" stroke="#38bdf8" stroke-width="1" stroke-opacity="0.5" transform="rotate(-65)"/>

  <!-- Central Glowing Cube/Hexagon with Initials "MB" (Mayukh Bhattacharjee) -->
  <polygon points="0,-28 24,-14 24,14 0,28 -24,14 -24,-14" fill="#0d172e" stroke="#247bff" stroke-width="2"/>
  <polygon points="0,-18 16,-9 16,9 0,18 -16,9 -16,-9" fill="#132347"/>
  <text x="0" y="5" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="900" letter-spacing="1">MB</text>

  <!-- Orbit Nodes with tech badges matching Reel -->
  <!-- Python -->
  <g transform="translate(-130, -35)">
    <circle cx="0" cy="0" r="14" fill="#0b1324" stroke="#3776AB" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9" font-weight="800">Py</text>
  </g>
  <!-- Go -->
  <g transform="translate(125, 30)">
    <circle cx="0" cy="0" r="14" fill="#0b1324" stroke="#00ADD8" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#00ADD8" font-family="{FONT_MONO}" font-size="9" font-weight="800">Go</text>
  </g>
  <!-- React -->
  <g transform="translate(-60, 65)">
    <circle cx="0" cy="0" r="14" fill="#0b1324" stroke="#61DAFB" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#61DAFB" font-family="{FONT_MONO}" font-size="9" font-weight="800">Re</text>
  </g>
  <!-- Node -->
  <g transform="translate(70, -60)">
    <circle cx="0" cy="0" r="14" fill="#0b1324" stroke="#339933" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#34d399" font-family="{FONT_MONO}" font-size="9" font-weight="800">No</text>
  </g>
  <!-- TS -->
  <g transform="translate(-115, 45)">
    <circle cx="0" cy="0" r="13" fill="#0b1324" stroke="#3178C6" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#60a5fa" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">TS</text>
  </g>
  <!-- Next.js -->
  <g transform="translate(110, -45)">
    <circle cx="0" cy="0" r="13" fill="#0b1324" stroke="#ffffff" stroke-width="1"/>
    <text x="0" y="4" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">Nx</text>
  </g>

  <!-- Left Footer Text matching Reel -->
  <text x="0" y="145" text-anchor="middle" fill="#64748b" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">CODE IS THE TOOL. IMPACT IS THE POINT.</text>
</g>

<!-- RIGHT: Structured Grid of Tech Chips matching Reel -->
<g transform="translate(450, 110)">
  <!-- 01 / LANGUAGES -->
  <text x="0" y="12" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">01 / LANGUAGES</text>
  <g transform="translate(0, 22)">
    <!-- Python -->
    <rect x="0" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="12" y="21" font-size="13">🐍</text>
    <text x="36" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">Python</text>

    <!-- Go -->
    <rect x="125" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="137" y="21" font-size="13">🐹</text>
    <text x="161" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">Go (Golang)</text>

    <!-- TypeScript -->
    <rect x="250" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="262" y="21" font-size="13">📘</text>
    <text x="284" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">TypeScript</text>
  </g>

  <!-- 02 / FRONTEND & RUNTIME -->
  <text x="0" y="82" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">02 / FRONTEND &amp; RUNTIME</text>
  <g transform="translate(0, 92)">
    <!-- React -->
    <rect x="0" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="12" y="21" font-size="13">⚛️</text>
    <text x="36" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">React 18</text>

    <!-- Next.js -->
    <rect x="125" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="137" y="21" font-size="13">▲</text>
    <text x="161" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">Next.js</text>

    <!-- SvelteKit -->
    <rect x="250" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="262" y="21" font-size="13">🔥</text>
    <text x="284" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">SvelteKit</text>
  </g>

  <!-- 03 / BACKEND, CLOUD & AI -->
  <text x="0" y="152" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">03 / BACKEND, CLOUD &amp; AI</text>
  <g transform="translate(0, 162)">
    <!-- Node / Gin -->
    <rect x="0" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="12" y="21" font-size="13">🟢</text>
    <text x="36" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">Node / Gin</text>

    <!-- OpenCV -->
    <rect x="125" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="137" y="21" font-size="13">👁️</text>
    <text x="161" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">OpenCV</text>

    <!-- Supabase / Vercel -->
    <rect x="250" y="0" width="115" height="34" rx="6" fill="#0d1424" stroke="#1e293b"/>
    <text x="262" y="21" font-size="13">⚡</text>
    <text x="284" y="21" fill="#f1f5f9" font-family="{FONT_DISPLAY}" font-size="11.5" font-weight="700">Supabase</text>
  </g>

  <!-- Right Footer matching Reel -->
  <text x="0" y="235" fill="#38bdf8" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">BUILD / MENTOR / CREATE / REPEAT</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "stack.svg"), "w", encoding="utf-8") as f:
    f.write(stack_svg)
print("wrote assets/stack.svg")

# ---------------------------------------------------------------------------
# 4. assets/id-dashboard.svg (Matches Image 3: "REAL WORK. REAL IMPACT.")
# ---------------------------------------------------------------------------
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="430" viewBox="0 0 860 430" fill="none">
<defs>
  <linearGradient id="id-bg" x1="0" y1="0" x2="860" y2="430" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#050813"/>
    <stop offset="100%" stop-color="#090f1f"/>
  </linearGradient>
  <linearGradient id="id-border" x1="0" y1="0" x2="860" y2="430" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0.25"/>
  </linearGradient>
  <clipPath id="lanyard-port">
    <rect x="18" y="52" width="164" height="145" rx="8"/>
  </clipPath>
  <linearGradient id="foil-shine" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="45%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="50%" stop-color="#ffffff" stop-opacity="0.35"/>
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
<rect x="0.5" y="0.5" width="859" height="429" rx="15.5" stroke="url(#id-border)" stroke-width="1"/>

<!-- Header matching Reel: "04 / BUILDER CREDENTIALS" / "REAL WORK. REAL IMPACT." / "PUBLIC SNAPSHOT // 2026" -->
<g transform="translate(45, 34)">
  <text x="0" y="0" fill="#247bff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">04 / BUILDER CREDENTIALS</text>
  <text x="0" y="26" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">REAL WORK. REAL IMPACT.</text>
  <text x="0" y="44" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="2">PUBLIC SNAPSHOT // 2026</text>
</g>

<!-- LEFT: Hanging Lanyard Card matching Reel (Blue strap, metal clasp, SIM chip, barcode) -->
<g class="lanyard-card">
  <!-- Lanyard Strap entering from top -->
  <rect x="135" y="0" width="22" height="32" fill="#0d1b38" rx="2"/>
  <line x1="146" y1="0" x2="146" y2="32" stroke="#247bff" stroke-width="2"/>
  <text x="146" y="20" text-anchor="middle" fill="#60a5fa" font-family="{FONT_MONO}" font-size="7" font-weight="700" transform="rotate(90, 146, 20)">MAYUKH</text>

  <!-- Metal Clasp -->
  <rect x="128" y="30" width="36" height="14" rx="3" fill="#64748b" stroke="#cbd5e1" stroke-width="0.8"/>
  <circle cx="146" cy="37" r="3.5" fill="#1e293b"/>
  <ellipse cx="146" cy="48" rx="7" ry="7" fill="none" stroke="#94a3b8" stroke-width="3"/>

  <!-- ID Badge Body (200 x 310) matching Reel -->
  <g transform="translate(45, 54)">
    <rect width="200" height="310" rx="14" fill="#0b1222" stroke="#ff354f" stroke-width="1.2"/>
    <rect width="200" height="310" rx="14" fill="#0d172e" opacity="0.6"/>

    <!-- ID Header Bar matching Reel: "UG / BUILDER PASS" -> "MB / BUILDER PASS" -->
    <rect width="200" height="32" rx="14" fill="#0a1329"/>
    <text x="18" y="21" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="800" letter-spacing="1">MB / BUILDER PASS</text>
    <text x="182" y="21" text-anchor="end" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10" font-weight="800">0510</text>
    <line x1="0" y1="32" x2="200" y2="32" stroke="#1e293b"/>

    <!-- Photo Frame -->
    <rect x="18" y="44" width="164" height="150" rx="8" fill="#070c18" stroke="#1e293b"/>
    <g clip-path="url(#lanyard-port)">
      <image x="18" y="38" width="164" height="160" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
    </g>
    <!-- Tag on photo matching Reel: "FULL-STACK / AI" -->
    <g transform="translate(24, 168)">
      <rect width="95" height="18" rx="4" fill="#09142b" stroke="#247bff" stroke-width="0.8"/>
      <text x="47" y="12" text-anchor="middle" fill="#38bdf8" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">FULL-STACK / AI</text>
    </g>

    <!-- Name & Subtitle matching Reel -->
    <text x="18" y="214" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="15" font-weight="900" letter-spacing="0.5">MAYUKH BHATTACHARJEE</text>
    <text x="18" y="228" fill="#64748b" font-family="{FONT_MONO}" font-size="8.5" font-weight="700">INDIA // DEVELOPER</text>

    <!-- Golden SIM Microchip matching Reel -->
    <g transform="translate(150, 218)">
      <rect width="32" height="24" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="0.8"/>
      <line x1="16" y1="0" x2="16" y2="24" stroke="#d97706" stroke-width="1"/>
      <line x1="0" y1="12" x2="32" y2="12" stroke="#d97706" stroke-width="1"/>
    </g>

    <!-- Barcode simulation matching Reel -->
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

<!-- RIGHT: Dashboard Grid matching Reel exactly (3 metric boxes, most-starred bars, bottom announcement card) -->
<g transform="translate(285, 95)">
  <!-- 3 Metric Boxes matching Reel -->
  <!-- Box 1: FEATURED REPOS (Red number) -->
  <g transform="translate(0, 0)">
    <rect width="170" height="85" rx="8" fill="#080e1c" stroke="#1e293b"/>
    <text x="14" y="24" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700">FEATURED</text>
    <text x="14" y="60" fill="#ff354f" font-family="{FONT_DISPLAY}" font-size="34" font-weight="900">3</text>
    <text x="14" y="74" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">FLAGSHIP PLATFORMS</text>
  </g>

  <!-- Box 2: REPOSITORIES (Blue number) -->
  <g transform="translate(182, 0)">
    <rect width="170" height="85" rx="8" fill="#080e1c" stroke="#1e293b"/>
    <text x="14" y="24" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700">REPOSITORIES</text>
    <text x="14" y="60" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="34" font-weight="900">12</text>
    <text x="14" y="74" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">PUBLIC ACTIVE</text>
  </g>

  <!-- Box 3: CONTRIBUTIONS (White number) -->
  <g transform="translate(364, 0)">
    <rect width="170" height="85" rx="8" fill="#080e1c" stroke="#1e293b"/>
    <text x="14" y="24" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700">CONTRIBUTIONS</text>
    <text x="14" y="60" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="34" font-weight="900">64+</text>
    <text x="14" y="74" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">ANNUAL METRICS</text>
  </g>

  <!-- Middle: MOST-STARRED / PUBLIC REPOSITORIES matching Reel with Blue Progress Bars! -->
  <g transform="translate(0, 108)">
    <text x="0" y="14" fill="#64748b" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">MOST-STARRED / PUBLIC REPOSITORIES</text>
    <text x="520" y="14" fill="#ff354f" font-size="12">★</text>

    <!-- Bar 1: ai-educator -->
    <g transform="translate(0, 26)">
      <text x="0" y="12" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="11">ai-educator</text>
      <text x="520" y="12" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">3</text>
      <!-- Track and Fill -->
      <rect x="0" y="18" width="510" height="7" rx="3.5" fill="#131e36"/>
      <rect x="0" y="18" width="460" height="7" rx="3.5" fill="#247bff"/>
    </g>

    <!-- Bar 2: Paypaal-pro -->
    <g transform="translate(0, 62)">
      <text x="0" y="12" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="11">Paypaal-pro</text>
      <text x="520" y="12" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">2</text>
      <!-- Track and Fill -->
      <rect x="0" y="18" width="510" height="7" rx="3.5" fill="#131e36"/>
      <rect x="0" y="18" width="370" height="7" rx="3.5" fill="#247bff"/>
    </g>

    <!-- Bar 3: aizen-detector -->
    <g transform="translate(0, 98)">
      <text x="0" y="12" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="11">aizen-detector</text>
      <text x="520" y="12" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">2</text>
      <!-- Track and Fill -->
      <rect x="0" y="18" width="510" height="7" rx="3.5" fill="#131e36"/>
      <rect x="0" y="18" width="290" height="7" rx="3.5" fill="#247bff"/>
    </g>
  </g>

  <!-- Bottom: Announcement Card matching Reel ("Building scalable software at...") -->
  <g transform="translate(0, 240)">
    <rect width="534" height="64" rx="8" fill="#0c162e" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.4"/>
    <rect x="14" y="14" width="40" height="18" rx="4" fill="#ff354f"/>
    <text x="34" y="26" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="9" font-weight="800">NOW</text>
    
    <text x="64" y="27" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Building scalable software &amp; AI systems</text>
    <text x="14" y="48" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11">Open to high-impact engineering roles, full-stack builds &amp; open source.</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "id-dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(id_dashboard_svg)
print("wrote assets/id-dashboard.svg")

# ---------------------------------------------------------------------------
# 5. assets/connect.svg (Matches Image 3 bottom: "BUILD SOMETHING GREAT.")
# ---------------------------------------------------------------------------
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="320" viewBox="0 0 860 320" fill="none">
<defs>
  <linearGradient id="cn-bg" x1="0" y1="0" x2="860" y2="320" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#050813"/>
    <stop offset="100%" stop-color="#090f1f"/>
  </linearGradient>
  <linearGradient id="cn-border" x1="0" y1="0" x2="860" y2="320" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0.25"/>
  </linearGradient>
  <clipPath id="cn-char-clip">
    <rect x="25" y="20" width="265" height="280" rx="14"/>
  </clipPath>
</defs>

<style>
  @keyframes nudge {{ 0%, 100% {{ transform: translateX(0); }} 50% {{ transform: translateX(6px); }} }}
  .nudge-arrow {{ animation: nudge 1.8s ease-in-out infinite; }}
</style>

<rect width="860" height="320" rx="16" fill="url(#cn-bg)"/>
<rect x="0.5" y="0.5" width="859" height="319" rx="15.5" stroke="url(#cn-border)" stroke-width="1"/>

<!-- Left: Character pointing towards connect buttons -->
<g clip-path="url(#cn-char-clip)">
  <image x="15" y="10" width="280" height="300" href="data:image/png;base64,{char_b64}" preserveAspectRatio="xMidYMid slice"/>
</g>
<rect x="24" y="19" width="267" height="282" rx="14" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.25"/>

<!-- Header matching Reel: "05 / START A CONVERSATION" / "BUILD SOMETHING GREAT." -->
<g transform="translate(320, 32)">
  <text x="0" y="10" fill="#247bff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">05 / START A CONVERSATION</text>
  <text x="0" y="36" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">BUILD SOMETHING GREAT.</text>
  <text x="0" y="56" fill="#64748b" font-family="{FONT_MONO}" font-size="11" font-weight="700">Ideas. Opportunities. Your next move.</text>
</g>

<!-- Social Cards matching Reel -->
<g transform="translate(320, 110)">
  <!-- LinkedIn Card (Primary - Top) -->
  <g transform="translate(0, 0)">
    <rect width="495" height="54" rx="8" fill="#091224" stroke="#0A66C2" stroke-width="1.2"/>
    <rect x="14" y="11" width="32" height="32" rx="6" fill="#0A66C2"/>
    <text x="30" y="32" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="16" font-weight="900">in</text>
    
    <text x="58" y="24" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">LinkedIn Profile</text>
    <text x="58" y="41" fill="#38bdf8" font-family="{FONT_MONO}" font-size="10.5">Mayukh Bhattacharjee · Connect Professionally</text>
    
    <g class="nudge-arrow" transform="translate(458, 32)">
      <text x="0" y="0" fill="#0A66C2" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
    </g>
  </g>

  <!-- GitHub Card (Middle) -->
  <g transform="translate(0, 66)">
    <rect width="495" height="54" rx="8" fill="#091224" stroke="#38bdf8" stroke-width="1"/>
    <rect x="14" y="11" width="32" height="32" rx="6" fill="#1e293b"/>
    <text x="30" y="32" text-anchor="middle" fill="#ffffff" font-size="16">🐙</text>
    
    <text x="58" y="24" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">GitHub Profile</text>
    <text x="58" y="41" fill="#94a3b8" font-family="{FONT_MONO}" font-size="10.5">@mayukhbyte · Repositories, commits &amp; architecture</text>
    
    <g class="nudge-arrow" transform="translate(458, 32)">
      <text x="0" y="0" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
    </g>
  </g>

  <!-- Email Card (Bottom) -->
  <g transform="translate(0, 132)">
    <rect width="495" height="54" rx="8" fill="#091224" stroke="#ff354f" stroke-width="1"/>
    <rect x="14" y="11" width="32" height="32" rx="6" fill="#ff354f"/>
    <text x="30" y="32" text-anchor="middle" fill="#ffffff" font-size="15">✉️</text>
    
    <text x="58" y="24" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">Direct Inquiries</text>
    <text x="58" y="41" fill="#94a3b8" font-family="{FONT_MONO}" font-size="10.5">mayukhbhttchrj@gmail.com · Collaborations</text>
    
    <g class="nudge-arrow" transform="translate(458, 32)">
      <text x="0" y="0" fill="#ff354f" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
    </g>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "connect.svg"), "w", encoding="utf-8") as f:
    f.write(connect_svg)
print("wrote assets/connect.svg")

print("All exact-match Reel SVGs generated successfully!")
