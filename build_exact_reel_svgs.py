import os
import base64
import io
from PIL import Image, ImageFilter

ASSETS_DIR = r"C:\Users\meyon moyukh\.gemini\antigravity\scratch\mayukhbyte\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Prepare char_sticker.png with 4px white outline and high resolution
char_raw = Image.open(os.path.join(ASSETS_DIR, "right_pointing.png")).convert("RGBA")
alpha = char_raw.split()[3]
dilated = alpha.filter(ImageFilter.MaxFilter(9))
white_outline = Image.new("RGBA", char_raw.size, (255, 255, 255, 255))
white_outline.putalpha(dilated)
sticker = Image.alpha_composite(white_outline, char_raw)
bbox = sticker.getbbox()
if bbox:
    sticker = sticker.crop(bbox)
sticker.save(os.path.join(ASSETS_DIR, "char_sticker.png"))

# 2. Prepare id_pass_photo.png (Mayukh's head & shoulders with dark cyber background)
id_raw = Image.open(os.path.join(ASSETS_DIR, "id.png")).convert("RGBA")
w, h = id_raw.size
id_crop = id_raw.crop((int(w * 0.1), int(h * 0.22), int(w * 0.9), int(h * 0.85)))
bg = Image.new("RGBA", id_crop.size, (9, 19, 39, 255))
id_pass_photo = Image.alpha_composite(bg, id_crop)
id_pass_photo.save(os.path.join(ASSETS_DIR, "id_pass_photo.png"))

def get_b64(path, max_dim=540):
    im = Image.open(path)
    ratio = max_dim / max(im.size)
    if ratio < 1.0:
        im = im.resize((int(im.width * ratio), int(im.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

hero_id_b64 = get_b64(os.path.join(ASSETS_DIR, "id.png"), 540)
id_pass_b64 = get_b64(os.path.join(ASSETS_DIR, "id_pass_photo.png"), 520)
sticker_b64 = get_b64(os.path.join(ASSETS_DIR, "char_sticker.png"), 520)

FONT_DISPLAY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"

print("Assets prepared. Generating refined SVGs...")

# ==============================================================================
# 1. hero.svg (14 Public Repos, top projects, Mayukh cutout)
# ==============================================================================
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="860" height="400" viewBox="0 0 860 400" fill="none">
<defs>
  <linearGradient id="h-bg" x1="0" y1="0" x2="860" y2="400" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="40%" stop-color="#050a18"/>
    <stop offset="80%" stop-color="#081026"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="h-border" x1="0" y1="0" x2="860" y2="400" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9"/>
    <stop offset="45%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="75%" stop-color="#ff0055" stop-opacity="0.6"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.8"/>
  </linearGradient>
  <radialGradient id="h-glow-cyan" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.32"/>
    <stop offset="50%" stop-color="#00d2ff" stop-opacity="0.12"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="h-glow-crimson" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff0055" stop-opacity="0.28"/>
    <stop offset="60%" stop-color="#ff0055" stop-opacity="0.06"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0"/>
  </radialGradient>
  <pattern id="h-grid" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#00f0ff" fill-opacity="0.13"/>
  </pattern>
  <clipPath id="h-port-clip">
    <rect x="560" y="20" width="268" height="358" rx="18"/>
  </clipPath>
</defs>

<rect width="860" height="400" rx="16" fill="url(#h-bg)"/>
<rect width="860" height="400" rx="16" fill="url(#h-grid)"/>

<circle cx="680" cy="195" r="200" fill="url(#h-glow-cyan)"/>
<circle cx="750" cy="250" r="170" fill="url(#h-glow-crimson)"/>

<rect x="0.5" y="0.5" width="859" height="399" rx="15.5" stroke="url(#h-border)" stroke-width="1.2"/>

<!-- LEFT COLUMN -->
<!-- Status Pill -->
<g transform="translate(48, 36)">
  <rect width="186" height="28" rx="14" fill="#030b1c" stroke="#00f0ff" stroke-width="1.2"/>
  <circle cx="16" cy="14" r="4.5" fill="#00f0ff"/>
  <text x="28" y="18" fill="#00f0ff" font-family="{FONT_MONO}" font-size="11" font-weight="700" letter-spacing="1.5">PORTFOLIO // 2026</text>
</g>

<!-- Big Name Heading -->
<g transform="translate(48, 126)">
  <text x="0" y="0" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="64" font-weight="900" letter-spacing="-1">MAYUKH</text>
  <!-- Red accent stripes -->
  <g transform="translate(325, -42)">
    <line x1="0" y1="26" x2="7" y2="4" stroke="#ff0055" stroke-width="4.5" stroke-linecap="round"/>
    <line x1="9" y1="26" x2="16" y2="4" stroke="#ff0055" stroke-width="4.5" stroke-linecap="round"/>
    <line x1="18" y1="26" x2="25" y2="4" stroke="#ff0055" stroke-width="4.5" stroke-linecap="round"/>
    <text x="36" y="12" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="1">BUILD.</text>
    <text x="36" y="25" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="1">BEYOND.</text>
  </g>
  <text x="0" y="66" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="58" font-weight="900" letter-spacing="-1">BHATTACHARJEE</text>
</g>

<!-- Subtitle Role -->
<text x="48" y="234" fill="#00f0ff" font-family="{FONT_MONO}" font-size="12.5" font-weight="800" letter-spacing="2">FULL-STACK DEVELOPER &amp; AI BUILDER</text>

<!-- Bio -->
<text x="48" y="265" fill="#e2e8f0" font-family="{FONT_DISPLAY}" font-size="15" font-weight="500">Building scalable software, intelligent AI systems &amp; web apps.</text>
<text x="48" y="290" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="500">Creator of <tspan fill="#ffffff" font-weight="700">Paypaal-pro</tspan>, <tspan fill="#ffffff" font-weight="700">ai-educator</tspan> &amp; <tspan fill="#ffffff" font-weight="700">Aizen-detector-url</tspan>.</text>

<!-- Quick Stats Badges: 14 Public Repos -->
<g transform="translate(48, 324)">
  <rect x="0" y="0" width="105" height="34" rx="8" fill="#050d22" stroke="#1e293b"/>
  <text x="52" y="22" text-anchor="middle" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="12" font-weight="600">India</text>

  <rect x="117" y="0" width="168" height="34" rx="8" fill="#050d22" stroke="#00f0ff" stroke-opacity="0.4"/>
  <text x="201" y="22" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="12" font-weight="700">14 Public Repos</text>

  <rect x="297" y="0" width="180" height="34" rx="8" fill="#050d22" stroke="#10b981" stroke-opacity="0.5"/>
  <circle cx="317" cy="17" r="4" fill="#10b981"/>
  <text x="394" y="22" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="600">Open to Projects</text>
</g>

<!-- RIGHT COLUMN: Photo Card -->
<g clip-path="url(#h-port-clip)">
  <image x="560" y="10" width="268" height="370" href="data:image/png;base64,{hero_id_b64}" xlink:href="data:image/png;base64,{hero_id_b64}" preserveAspectRatio="xMidYMid slice"/>
</g>
<rect x="560" y="20" width="268" height="358" rx="18" fill="none" stroke="#00f0ff" stroke-width="1.2" stroke-opacity="0.6"/>

<!-- Pill Badge over Photo -->
<g transform="translate(605, 335)">
  <rect width="180" height="32" rx="16" fill="#030816" stroke="#00f0ff" stroke-width="1.2"/>
  <text x="90" y="20" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="10.5" font-weight="800" letter-spacing="1">FULL-STACK / AI</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("wrote hero.svg")

# ==============================================================================
# 2. about-life.svg (Built Different & Life Outside Commit)
# ==============================================================================
about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="860" height="390" viewBox="0 0 860 390" fill="none">
<defs>
  <linearGradient id="ab-bg" x1="0" y1="0" x2="860" y2="390" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#050c1e"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="ab-border" x1="0" y1="0" x2="860" y2="390" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#ff0055" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.6"/>
  </linearGradient>
  <clipPath id="ab-photo-clip">
    <rect x="0" y="0" width="140" height="150" rx="10"/>
  </clipPath>
</defs>

<rect width="860" height="390" rx="16" fill="url(#ab-bg)"/>
<rect x="0.5" y="0.5" width="859" height="389" rx="15.5" stroke="url(#ab-border)" stroke-width="1.2"/>

<!-- LEFT COLUMN (Built Different) -->
<g transform="translate(32, 28)">
  <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">01 / PHILOSOPHY</text>
  <text x="0" y="36" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">BUILT DIFFERENT.</text>

  <!-- Shell terminal container -->
  <g transform="translate(0, 52)">
    <rect width="375" height="110" rx="8" fill="#040915" stroke="#1e293b"/>
    <text x="14" y="24" fill="#64748b" font-family="{FONT_MONO}" font-size="10">mayukh@dev:~$ ./build</text>
    <text x="14" y="44" fill="#00f0ff" font-family="{FONT_MONO}" font-size="11" font-weight="700">curiosity_into_impact() &#123;</text>
    
    <!-- 3 Pipeline Step Boxes -->
    <g transform="translate(14, 56)">
      <rect x="0" y="0" width="80" height="36" rx="6" fill="#07152d" stroke="#00f0ff" stroke-width="0.8"/>
      <text x="40" y="16" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9" font-weight="800">01</text>
      <text x="40" y="28" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="8.5" font-weight="700">DISCOVER</text>
      
      <text x="88" y="22" fill="#64748b" font-family="{FONT_MONO}" font-size="12">→</text>
      
      <rect x="105" y="0" width="80" height="36" rx="6" fill="#07152d" stroke="#00f0ff" stroke-width="0.8"/>
      <text x="145" y="16" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9" font-weight="800">02</text>
      <text x="145" y="28" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="8.5" font-weight="700">ENGINEER</text>
      
      <text x="193" y="22" fill="#64748b" font-family="{FONT_MONO}" font-size="12">→</text>
      
      <rect x="210" y="0" width="80" height="36" rx="6" fill="#1c0715" stroke="#ff0055" stroke-width="1"/>
      <text x="250" y="16" text-anchor="middle" fill="#ff0055" font-family="{FONT_MONO}" font-size="9" font-weight="800">03</text>
      <text x="250" y="28" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="8.5" font-weight="700">SHIP</text>
    </g>
  </g>

  <!-- 3 Focus Pillars -->
  <g transform="translate(0, 180)">
    <g transform="translate(0, 0)">
      <text x="0" y="14" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">— Modern Web &amp; App Dev</text>
      <text x="14" y="32" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">From first interaction to resilient production code.</text>
    </g>
    <g transform="translate(0, 48)">
      <text x="0" y="14" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">— AI &amp; Intelligent Systems</text>
      <text x="14" y="32" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">Agent financial ops, automated crawlers &amp; LLMs.</text>
    </g>
    <g transform="translate(0, 96)">
      <text x="0" y="14" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13.5" font-weight="800">— Open Source Engineering</text>
      <text x="14" y="32" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">Building high-impact public tools and frameworks.</text>
    </g>
  </g>
</g>

<!-- VERTICAL DIVIDER -->
<line x1="430" y1="28" x2="430" y2="362" stroke="#1e293b" stroke-width="1"/>

<!-- RIGHT COLUMN (Life Outside the Commit) -->
<g transform="translate(452, 28)">
  <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">02 / LIFE OUTSIDE THE COMMIT</text>
  <text x="0" y="36" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">MORE THAN A JOB TITLE.</text>
  
  <!-- Red & Blue underline accents -->
  <rect x="0" y="44" width="80" height="3" fill="#00f0ff" rx="1.5"/>
  <rect x="85" y="44" width="40" height="3" fill="#ff0055" rx="1.5"/>

  <!-- Card with photo & 3 steps -->
  <g transform="translate(0, 60)">
    <rect width="375" height="190" rx="10" fill="#040915" stroke="#1e293b"/>
    
    <!-- Photo Box -->
    <g transform="translate(16, 20)">
      <g clip-path="url(#ab-photo-clip)">
        <image x="0" y="-10" width="140" height="170" href="data:image/png;base64,{id_pass_b64}" xlink:href="data:image/png;base64,{id_pass_b64}" preserveAspectRatio="xMidYMid slice"/>
      </g>
      <rect width="140" height="150" rx="10" fill="none" stroke="#00f0ff" stroke-width="0.8" stroke-opacity="0.4"/>
      <rect x="15" y="122" width="110" height="20" rx="10" fill="#030816" stroke="#00f0ff" stroke-width="0.8"/>
      <text x="70" y="136" text-anchor="middle" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8" font-weight="800">MAYUKH / BUILDER</text>
    </g>

    <!-- 3 Action Steps matching reel -->
    <g transform="translate(175, 25)">
      <g transform="translate(0, 0)">
        <text x="0" y="14" fill="#ff0055" font-family="{FONT_MONO}" font-size="10.5" font-weight="800">01</text>
        <text x="26" y="14" fill="#ffffff" font-family="{FONT_MONO}" font-size="10" font-weight="700">FIND THE GAP</text>
        <line x1="0" y1="24" x2="180" y2="24" stroke="#1e293b"/>
      </g>
      <g transform="translate(0, 44)">
        <text x="0" y="14" fill="#ff0055" font-family="{FONT_MONO}" font-size="10.5" font-weight="800">02</text>
        <text x="26" y="14" fill="#ffffff" font-family="{FONT_MONO}" font-size="10" font-weight="700">BUILD YOUR PLAN</text>
        <line x1="0" y1="24" x2="180" y2="24" stroke="#1e293b"/>
      </g>
      <g transform="translate(0, 88)">
        <text x="0" y="14" fill="#ff0055" font-family="{FONT_MONO}" font-size="10.5" font-weight="800">03</text>
        <text x="26" y="14" fill="#ffffff" font-family="{FONT_MONO}" font-size="10" font-weight="700">TAKE THE LEAP</text>
        <line x1="0" y1="24" x2="180" y2="24" stroke="#1e293b"/>
      </g>
    </g>
  </g>

  <!-- Bottom Tagline -->
  <g transform="translate(0, 270)">
    <text x="0" y="10" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700" letter-spacing="1">MAKE THE NEXT MOVE.</text>
    <text x="0" y="32" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="16" font-weight="800">Building With Intent &amp; Impact</text>
    <text x="0" y="48" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11.5">Autonomous fintech, intelligent education tools &amp; web infrastructure.</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "about-life.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)
print("wrote about-life.svg")

# ==============================================================================
# 3. stack.svg (Real tech from Mayukh's actual work: TS, JS, Py, Go, React, Next, Supabase, Express, MCP)
# ==============================================================================
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="860" height="420" viewBox="0 0 860 420" fill="none">
<defs>
  <linearGradient id="st-bg" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060e22"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="st-border" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#247bff" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0.6"/>
  </linearGradient>
  <radialGradient id="st-glow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.25"/>
    <stop offset="60%" stop-color="#247bff" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
  </radialGradient>
</defs>

<rect width="860" height="420" rx="16" fill="url(#st-bg)"/>
<rect x="0.5" y="0.5" width="859" height="419" rx="15.5" stroke="url(#st-border)" stroke-width="1.2"/>

<!-- Header -->
<g transform="translate(36, 28)">
  <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">03 / MY ENGINE ROOM</text>
  <text x="0" y="38" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="25" font-weight="900" letter-spacing="0.5">TOOLS CHANGE. CURIOSITY DOESN'T.</text>
  <text x="0" y="58" fill="#64748b" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">LANGUAGES / SYSTEMS / INTELLIGENCE</text>
</g>

<!-- LEFT: 3D Constellation Orbit Diagram (Mayukh's Stack) -->
<g transform="translate(40, 110)">
  <circle cx="170" cy="120" r="130" fill="url(#st-glow)"/>

  <!-- Orbits -->
  <ellipse cx="170" cy="120" rx="140" ry="55" fill="none" stroke="#00f0ff" stroke-width="1.2" stroke-opacity="0.4" transform="rotate(-25 170 120)"/>
  <ellipse cx="170" cy="120" rx="140" ry="55" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.4" transform="rotate(35 170 120)"/>
  <ellipse cx="170" cy="120" rx="130" ry="50" fill="none" stroke="#ff0055" stroke-width="1" stroke-opacity="0.3" transform="rotate(85 170 120)"/>

  <!-- Center Isometric 3D Cube (MB) -->
  <g transform="translate(170, 120)">
    <!-- Top Face -->
    <polygon points="0,-28 24,-14 0,0 -24,-14" fill="#0c2d64" stroke="#00f0ff" stroke-width="1.2"/>
    <!-- Left Face -->
    <polygon points="-24,-14 0,0 0,28 -24,14" fill="#081d42" stroke="#00f0ff" stroke-width="1.2"/>
    <!-- Right Face -->
    <polygon points="0,0 24,-14 24,14 0,28" fill="#061633" stroke="#00f0ff" stroke-width="1.2"/>
    <!-- MB Monogram -->
    <text x="0" y="7" text-anchor="middle" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="1">MB</text>
  </g>

  <!-- Constellation Nodes (From Mayukh's actual repos) -->
  <!-- Top: Python -->
  <g transform="translate(170, 30)">
    <circle cx="0" cy="0" r="18" fill="#0a1a36" stroke="#fbbf24" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#fbbf24" font-family="{FONT_MONO}" font-size="9" font-weight="800">Python</text>
  </g>

  <!-- Left: TypeScript -->
  <g transform="translate(50, 110)">
    <circle cx="0" cy="0" r="18" fill="#0a1a36" stroke="#3178c6" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#3178c6" font-family="{FONT_MONO}" font-size="10" font-weight="900">TS</text>
  </g>

  <!-- Right: Go (from Aizen-detector-url) -->
  <g transform="translate(290, 110)">
    <circle cx="0" cy="0" r="18" fill="#0a1a36" stroke="#00add8" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#00add8" font-family="{FONT_MONO}" font-size="10" font-weight="900">Go</text>
  </g>

  <!-- Bottom-Left: React -->
  <g transform="translate(90, 185)">
    <circle cx="0" cy="0" r="18" fill="#0a1a36" stroke="#61dafb" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#61dafb" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">React</text>
  </g>

  <!-- Bottom-Right: Node / Supabase -->
  <g transform="translate(250, 185)">
    <circle cx="0" cy="0" r="18" fill="#0a1a36" stroke="#3ecf8e" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#3ecf8e" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">Node</text>
  </g>

  <!-- Connecting Rays -->
  <line x1="170" y1="48" x2="170" y2="92" stroke="#fbbf24" stroke-width="0.8" stroke-dasharray="3,3"/>
  <line x1="68" y1="110" x2="146" y2="120" stroke="#3178c6" stroke-width="0.8" stroke-dasharray="3,3"/>
  <line x1="272" y1="110" x2="194" y2="120" stroke="#00add8" stroke-width="0.8" stroke-dasharray="3,3"/>
  <line x1="108" y1="185" x2="155" y2="135" stroke="#61dafb" stroke-width="0.8" stroke-dasharray="3,3"/>
  <line x1="232" y1="185" x2="185" y2="135" stroke="#3ecf8e" stroke-width="0.8" stroke-dasharray="3,3"/>

  <!-- Orbiting Satellite Particle -->
  <circle cx="310" cy="70" r="5" fill="#ff0055"/>
  <circle cx="310" cy="70" r="10" fill="#ff0055" fill-opacity="0.3"/>

  <text x="170" y="245" text-anchor="middle" fill="#64748b" font-family="{FONT_MONO}" font-size="9" font-weight="700" letter-spacing="1">CODE IS THE TOOL. IMPACT IS THE POINT.</text>
</g>

<!-- RIGHT: Real Categorized Tech Cards (From Mayukh's actual repos) -->
<g transform="translate(420, 100)">
  <!-- 01 / LANGUAGES -->
  <g transform="translate(0, 0)">
    <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">01 / LANGUAGES</text>
    <g transform="translate(0, 18)">
      <!-- TypeScript -->
      <rect x="0" y="0" width="95" height="42" rx="6" fill="#061226" stroke="#1e293b"/>
      <rect x="8" y="11" width="20" height="20" rx="3" fill="#3178c6"/>
      <text x="18" y="25" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="10" font-weight="900">TS</text>
      <text x="34" y="20" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="700">TypeScript</text>
      <text x="34" y="31" fill="#64748b" font-family="{FONT_MONO}" font-size="7.5">TYPED RUNTIME</text>

      <!-- JavaScript -->
      <rect x="105" y="0" width="95" height="42" rx="6" fill="#061226" stroke="#1e293b"/>
      <rect x="113" y="11" width="20" height="20" rx="3" fill="#f7df1e"/>
      <text x="123" y="25" text-anchor="middle" fill="#000000" font-family="{FONT_MONO}" font-size="10" font-weight="900">JS</text>
      <text x="139" y="20" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="700">JavaScript</text>
      <text x="139" y="31" fill="#64748b" font-family="{FONT_MONO}" font-size="7.5">MODERN ES6+</text>

      <!-- Python -->
      <rect x="210" y="0" width="95" height="42" rx="6" fill="#061226" stroke="#1e293b"/>
      <rect x="218" y="11" width="20" height="20" rx="3" fill="#3776ab"/>
      <text x="228" y="25" text-anchor="middle" fill="#ffd343" font-family="{FONT_MONO}" font-size="10" font-weight="900">Py</text>
      <text x="244" y="20" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="700">Python</text>
      <text x="244" y="31" fill="#64748b" font-family="{FONT_MONO}" font-size="7.5">SCRIPTS &amp; AI</text>

      <!-- Go -->
      <rect x="315" y="0" width="85" height="42" rx="6" fill="#061226" stroke="#1e293b"/>
      <rect x="323" y="11" width="20" height="20" rx="3" fill="#00add8"/>
      <text x="333" y="25" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="9" font-weight="900">GO</text>
      <text x="349" y="20" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="10.5" font-weight="700">Golang</text>
      <text x="349" y="31" fill="#64748b" font-family="{FONT_MONO}" font-size="7.5">FAST CRAWLER</text>
    </g>
  </g>

  <!-- 02 / FRONTEND -->
  <g transform="translate(0, 80)">
    <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">02 / FRONTEND</text>
    <g transform="translate(0, 18)">
      <!-- React -->
      <rect x="0" y="0" width="125" height="44" rx="6" fill="#061226" stroke="#1e293b"/>
      <text x="14" y="22" fill="#61dafb" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800">React</text>
      <text x="14" y="35" fill="#64748b" font-family="{FONT_MONO}" font-size="8">INTERACTIVE SPA</text>

      <!-- Next.js -->
      <rect x="135" y="0" width="125" height="44" rx="6" fill="#061226" stroke="#1e293b"/>
      <text x="14" y="22" transform="translate(135,0)" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800">Next.js</text>
      <text x="14" y="35" transform="translate(135,0)" fill="#64748b" font-family="{FONT_MONO}" font-size="8">SSR PLATFORMS</text>

      <!-- Tailwind / Framer -->
      <rect x="270" y="0" width="130" height="44" rx="6" fill="#061226" stroke="#1e293b"/>
      <text x="14" y="22" transform="translate(270,0)" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800">Tailwind &amp; UI</text>
      <text x="14" y="35" transform="translate(270,0)" fill="#64748b" font-family="{FONT_MONO}" font-size="8">3D &amp; MOTION UI</text>
    </g>
  </g>

  <!-- 03 / BACKEND -->
  <g transform="translate(0, 162)">
    <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">03 / BACKEND</text>
    <g transform="translate(0, 18)">
      <!-- Node & Express -->
      <rect x="0" y="0" width="125" height="44" rx="6" fill="#061226" stroke="#1e293b"/>
      <text x="14" y="22" fill="#22c55e" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800">Node &amp; Express</text>
      <text x="14" y="35" fill="#64748b" font-family="{FONT_MONO}" font-size="8">REST &amp; AGENT APIS</text>

      <!-- Supabase & Firebase -->
      <rect x="135" y="0" width="125" height="44" rx="6" fill="#061226" stroke="#1e293b"/>
      <text x="14" y="22" transform="translate(135,0)" fill="#3ecf8e" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800">Supabase &amp; Auth</text>
      <text x="14" y="35" transform="translate(135,0)" fill="#64748b" font-family="{FONT_MONO}" font-size="8">FIREBASE &amp; PG</text>

      <!-- MCP & AI APIs -->
      <rect x="270" y="0" width="130" height="44" rx="6" fill="#061226" stroke="#ff0055" stroke-opacity="0.4"/>
      <text x="14" y="22" transform="translate(270,0)" fill="#ff0055" font-family="{FONT_DISPLAY}" font-size="12" font-weight="800">MCP &amp; LLM APIs</text>
      <text x="14" y="35" transform="translate(270,0)" fill="#64748b" font-family="{FONT_MONO}" font-size="8">AUTONOMOUS AGENTS</text>
    </g>
  </g>

  <!-- Bottom Tagline -->
  <text x="0" y="255" fill="#64748b" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">BUILD / MENTOR / CREATE / REPEAT</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "stack.svg"), "w", encoding="utf-8") as f:
    f.write(stack_svg)
print("wrote stack.svg")

# ==============================================================================
# 4. projects-table.svg (Clean Grid Table matching Image 1: Things I've built)
# ==============================================================================
projects_table_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="235" viewBox="0 0 860 235" fill="none">
<defs>
  <linearGradient id="pt-bg" x1="0" y1="0" x2="860" y2="235" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060e22"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="pt-border" x1="0" y1="0" x2="860" y2="235" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#247bff" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#ff0055" stop-opacity="0.6"/>
  </linearGradient>
</defs>

<rect width="860" height="235" rx="14" fill="url(#pt-bg)"/>
<rect x="0.5" y="0.5" width="859" height="234" rx="13.5" stroke="url(#pt-border)" stroke-width="1.2"/>

<!-- Section Title matching Image 1: Things I've built -->
<g transform="translate(25, 20)">
  <text x="0" y="8" fill="#00f0ff" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="1">03 / FEATURED REPOSITORIES</text>
  <text x="0" y="28" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="20" font-weight="900" letter-spacing="0.5">Things I've built</text>
</g>

<!-- Clean Dark Grid Table matching Image 1 -->
<g transform="translate(25, 60)">
  <!-- Table Header -->
  <rect x="0" y="0" width="810" height="32" fill="#08142c" stroke="#1e293b"/>
  <text x="20" y="20" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11" font-weight="700">Project</text>
  <text x="200" y="20" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11" font-weight="700">What it does</text>
  <text x="670" y="20" fill="#94a3b8" font-family="{FONT_MONO}" font-size="11" font-weight="700">Focus</text>

  <!-- Row 1: Paypaal-pro -->
  <rect x="0" y="32" width="810" height="42" fill="#040915" stroke="#1e293b"/>
  <text x="20" y="58" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Paypaal-pro</text>
  <text x="200" y="58" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="12">Autonomous agent financial operations engine with AI dispute synthesis</text>
  <text x="670" y="58" fill="#ff0055" font-family="{FONT_MONO}" font-size="11" font-weight="700">Fintech + Agents</text>

  <!-- Row 2: ai-educator -->
  <rect x="0" y="74" width="810" height="42" fill="#040915" stroke="#1e293b"/>
  <text x="20" y="100" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">ai-educator</text>
  <text x="200" y="100" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="12">AI tutoring system with multi-level doubt solving &amp; adaptive quizzes</text>
  <text x="670" y="100" fill="#00f0ff" font-family="{FONT_MONO}" font-size="11" font-weight="700">AI + Learning</text>

  <!-- Row 3: Aizen-detector-url -->
  <rect x="0" y="116" width="810" height="42" fill="#040915" stroke="#1e293b"/>
  <text x="20" y="142" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Aizen-detector-url</text>
  <text x="200" y="142" fill="#cbd5e1" font-family="{FONT_DISPLAY}" font-size="12">Real-time URL threat crawler with 21 concurrent Go goroutines &amp; 39 signals</text>
  <text x="670" y="142" fill="#34d399" font-family="{FONT_MONO}" font-size="11" font-weight="700">Security + Go</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "projects-table.svg"), "w", encoding="utf-8") as f:
    f.write(projects_table_svg)
print("wrote projects-table.svg")

# ==============================================================================
# 5. id-dashboard.svg (NO stars, 75 contributions in last year, 14 repos, authentic lanyard pass)
# ==============================================================================
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="860" height="450" viewBox="0 0 860 450" fill="none">
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
  <clipPath id="pass-photo-clip">
    <rect x="12" y="28" width="192" height="172" rx="8"/>
  </clipPath>
</defs>

<rect width="860" height="450" rx="16" fill="url(#id-bg)"/>
<rect x="0.5" y="0.5" width="859" height="449" rx="15.5" stroke="url(#id-border)" stroke-width="1.2"/>

<!-- Ambient background text behind Lanyard matching Image 1: THE -->
<text x="25" y="140" fill="#081836" font-family="{FONT_DISPLAY}" font-size="64" font-weight="900">THE</text>

<!-- ============================================================ -->
<!-- LEFT: Hanging Builder Lanyard Pass matching Image 1          -->
<!-- ============================================================ -->
<g transform="translate(30, 0)">
  <!-- Blue Lanyard Ribbon coming straight down from top -->
  <rect x="94" y="0" width="34" height="68" fill="#1d4ed8"/>
  <rect x="94" y="0" width="34" height="68" fill="#000000" fill-opacity="0.1"/>
  <!-- White text on ribbon -->
  <text x="111" y="42" text-anchor="middle" fill="#ffffff" font-family="{FONT_MONO}" font-size="8" font-weight="800" transform="rotate(-90 111 42)" letter-spacing="1">MB0510 // BUILDER</text>

  <!-- Metallic Buckle / Clasp Ring -->
  <g transform="translate(94, 62)">
    <rect x="-1" y="0" width="36" height="16" rx="4" fill="url(#metal-clamp)" stroke="#64748b" stroke-width="0.8"/>
    <rect x="8" y="4" width="18" height="8" rx="2" fill="#0a1224"/>
  </g>

  <!-- The ID Pass Card (x=3, y=74, width=216, height=316) -->
  <g transform="translate(3, 74)">
    <!-- Base Card Body -->
    <rect width="216" height="316" rx="12" fill="#091428" stroke="#1e293b" stroke-width="1.2"/>
    <!-- Top red accent line matching Image 1 -->
    <line x1="16" y1="2" x2="200" y2="2" stroke="#ff0055" stroke-width="2.5" stroke-linecap="round"/>

    <!-- Header Row -->
    <text x="14" y="19" fill="#ffffff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800" letter-spacing="0.5">MB / BUILDER PASS</text>
    <text x="202" y="19" text-anchor="end" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="800">0510</text>

    <!-- Photo Frame & Mayukh's Photo -->
    <rect x="12" y="28" width="192" height="172" rx="8" fill="#050c1c" stroke="#1e293b"/>
    <g clip-path="url(#pass-photo-clip)">
      <image x="12" y="28" width="192" height="172" href="data:image/png;base64,{id_pass_b64}" xlink:href="data:image/png;base64,{id_pass_b64}" preserveAspectRatio="xMidYMid slice"/>
    </g>
    <rect x="12" y="28" width="192" height="172" rx="8" fill="none" stroke="#00f0ff" stroke-width="0.8" stroke-opacity="0.4"/>

    <!-- Bright Blue Pill Badge on Photo matching Image 1 -->
    <g transform="translate(18, 168)">
      <rect width="112" height="22" rx="11" fill="#0066ff" stroke="#38bdf8" stroke-width="0.8"/>
      <circle cx="12" cy="11" r="3.5" fill="#ffffff"/>
      <text x="22" y="15" fill="#ffffff" font-family="{FONT_MONO}" font-size="9" font-weight="800" letter-spacing="0.5">FULL-STACK / AI</text>
    </g>

    <!-- Name & Details Below Photo -->
    <text x="14" y="222" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="12" font-weight="900" letter-spacing="0.5">MAYUKH BHATTACHARJEE</text>
    <text x="14" y="236" fill="#00f0ff" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" letter-spacing="0.5">INDIA // DEVELOPER</text>

    <!-- Golden SIM Smart Chip matching Image 1 -->
    <g transform="translate(166, 212)">
      <rect width="36" height="26" rx="4" fill="url(#gold-chip)" stroke="#b45309" stroke-width="0.6"/>
      <!-- Etched chip contacts -->
      <line x1="0" y1="13" x2="36" y2="13" stroke="#92400e" stroke-width="0.8"/>
      <line x1="18" y1="0" x2="18" y2="26" stroke="#92400e" stroke-width="0.8"/>
      <rect x="11" y="7" width="14" height="12" rx="2" fill="none" stroke="#92400e" stroke-width="0.8"/>
    </g>

    <!-- Crisp Authentic Barcode matching Image 1 -->
    <g transform="translate(14, 250)">
      <rect x="0" y="0" width="2" height="24" fill="#cbd5e1"/>
      <rect x="4" y="0" width="4" height="24" fill="#cbd5e1"/>
      <rect x="11" y="0" width="1.5" height="24" fill="#cbd5e1"/>
      <rect x="15" y="0" width="3" height="24" fill="#cbd5e1"/>
      <rect x="21" y="0" width="5" height="24" fill="#cbd5e1"/>
      <rect x="29" y="0" width="1.5" height="24" fill="#cbd5e1"/>
      <rect x="33" y="0" width="3" height="24" fill="#cbd5e1"/>
      <rect x="38" y="0" width="4.5" height="24" fill="#cbd5e1"/>
      <rect x="45" y="0" width="2" height="24" fill="#cbd5e1"/>
      <rect x="49" y="0" width="6" height="24" fill="#cbd5e1"/>
      <rect x="58" y="0" width="1.5" height="24" fill="#cbd5e1"/>
      <rect x="62" y="0" width="3.5" height="24" fill="#cbd5e1"/>
      <rect x="68" y="0" width="2" height="24" fill="#cbd5e1"/>
      <rect x="73" y="0" width="5" height="24" fill="#cbd5e1"/>
      <rect x="81" y="0" width="2" height="24" fill="#cbd5e1"/>
      <rect x="85" y="0" width="4" height="24" fill="#cbd5e1"/>
      <rect x="92" y="0" width="1.5" height="24" fill="#cbd5e1"/>
      <rect x="96" y="0" width="3" height="24" fill="#cbd5e1"/>
      <rect x="101" y="0" width="6" height="24" fill="#cbd5e1"/>
      <rect x="110" y="0" width="2" height="24" fill="#cbd5e1"/>
      <rect x="114" y="0" width="4" height="24" fill="#cbd5e1"/>
      <rect x="121" y="0" width="1.5" height="24" fill="#cbd5e1"/>
      <rect x="125" y="0" width="5" height="24" fill="#cbd5e1"/>
      <rect x="133" y="0" width="2.5" height="24" fill="#cbd5e1"/>
      <rect x="138" y="0" width="4" height="24" fill="#cbd5e1"/>
      <rect x="145" y="0" width="2" height="24" fill="#cbd5e1"/>
      <rect x="150" y="0" width="6" height="24" fill="#cbd5e1"/>
      <rect x="159" y="0" width="1.5" height="24" fill="#cbd5e1"/>
      <rect x="163" y="0" width="3.5" height="24" fill="#cbd5e1"/>
      <rect x="169" y="0" width="4" height="24" fill="#cbd5e1"/>
      <rect x="176" y="0" width="2" height="24" fill="#cbd5e1"/>
      <rect x="181" y="0" width="5" height="24" fill="#cbd5e1"/>
    </g>

    <!-- Footer label -->
    <text x="108" y="292" text-anchor="middle" fill="#64748b" font-family="{FONT_MONO}" font-size="7.5" letter-spacing="1">INDEPENDENT CREATOR ID - MB0510</text>
  </g>

  <!-- BEHIND THE CODE. text directly below the card matching Image 1 -->
  <text x="111" y="420" text-anchor="middle" fill="#38bdf8" font-family="{FONT_DISPLAY}" font-size="21" font-weight="900" letter-spacing="1.5">BEHIND THE CODE.</text>
</g>

<!-- ============================================================ -->
<!-- RIGHT: Dashboard (NO stars, 75 contributions, 14 repos)     -->
<!-- ============================================================ -->
<g transform="translate(285, 30)">
  <!-- Section Title -->
  <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">04 / BUILDER CREDENTIALS</text>
  <text x="0" y="36" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">REAL WORK. REAL IMPACT.</text>
  <text x="0" y="54" fill="#64748b" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">PUBLIC SNAPSHOT // 2026</text>

  <!-- 2 Metric Boxes: 75 CONTRIBUTIONS & 14 REPOSITORIES (NO REPO STARS) -->
  <g transform="translate(0, 70)">
    <!-- Box 1: Contributions: 75 -->
    <g transform="translate(0, 0)">
      <rect width="260" height="82" rx="8" fill="#08142c" stroke="#ff0055" stroke-width="1.2" stroke-opacity="0.6"/>
      <text x="18" y="24" fill="#ff0055" font-family="{FONT_MONO}" font-size="10" font-weight="800" letter-spacing="1">CONTRIBUTIONS</text>
      <text x="18" y="58" fill="#ff0055" font-family="{FONT_DISPLAY}" font-size="36" font-weight="900">75</text>
      <text x="18" y="72" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">IN LAST YEAR</text>
    </g>

    <!-- Box 2: Repositories: 14 -->
    <g transform="translate(275, 0)">
      <rect width="260" height="82" rx="8" fill="#08142c" stroke="#00f0ff" stroke-width="1.2" stroke-opacity="0.6"/>
      <text x="18" y="24" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10" font-weight="800" letter-spacing="1">REPOSITORIES</text>
      <text x="18" y="58" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="36" font-weight="900">14</text>
      <text x="18" y="72" fill="#94a3b8" font-family="{FONT_MONO}" font-size="8.5">PUBLIC GITHUB</text>
    </g>
  </g>

  <!-- Repositories List with solid glowing blue progress bars (NO stars) -->
  <g transform="translate(0, 172)">
    <text x="0" y="14" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">MOST-STARRED / PUBLIC REPOSITORIES</text>

    <!-- Bar 1: Paypaal-pro -->
    <g transform="translate(0, 26)">
      <text x="0" y="12" fill="#ffffff" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">Paypaal-pro</text>
      <rect x="0" y="18" width="535" height="9" rx="4.5" fill="#0c1832"/>
      <rect x="0" y="18" width="510" height="9" rx="4.5" fill="#0070f3"/>
    </g>

    <!-- Bar 2: ai-educator -->
    <g transform="translate(0, 64)">
      <text x="0" y="12" fill="#ffffff" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">ai-educator</text>
      <rect x="0" y="18" width="535" height="9" rx="4.5" fill="#0c1832"/>
      <rect x="0" y="18" width="410" height="9" rx="4.5" fill="#0070f3"/>
    </g>

    <!-- Bar 3: Aizen-detector-url -->
    <g transform="translate(0, 102)">
      <text x="0" y="12" fill="#ffffff" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">Aizen-detector-url</text>
      <rect x="0" y="18" width="535" height="9" rx="4.5" fill="#0c1832"/>
      <rect x="0" y="18" width="310" height="9" rx="4.5" fill="#0070f3"/>
    </g>
  </g>

  <!-- Bottom: Announcement Card matching Image 1 -->
  <g transform="translate(0, 318)">
    <rect width="535" height="66" rx="8" fill="#08142c" stroke="#1e293b" stroke-width="1"/>
    <!-- Red NOW Pill -->
    <rect x="14" y="14" width="38" height="18" rx="4" fill="#ff0055"/>
    <text x="33" y="26" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="9" font-weight="800">NOW</text>
    
    <text x="60" y="27" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="13" font-weight="800">Building scalable software &amp; AI systems</text>
    <text x="14" y="48" fill="#94a3b8" font-family="{FONT_DISPLAY}" font-size="11">Creator of Paypaal-pro, ai-educator &amp; Aizen-detector-url.</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "id-dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(id_dashboard_svg)
print("wrote id-dashboard.svg")

# ==============================================================================
# 6. connect.svg (ONLY LinkedIn, GitHub, Instagram - NO YouTube, NO 1:1 Mentorship)
# ==============================================================================
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="860" height="380" viewBox="0 0 860 380" fill="none">
<defs>
  <linearGradient id="cn-bg" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#02040a"/>
    <stop offset="50%" stop-color="#060e22"/>
    <stop offset="100%" stop-color="#02040a"/>
  </linearGradient>
  <linearGradient id="cn-border" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#ff0055" stop-opacity="0.4"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.6"/>
  </linearGradient>
  <linearGradient id="insta-grad" x1="0" y1="1" x2="1" y2="0">
    <stop offset="0%" stop-color="#f58529"/>
    <stop offset="35%" stop-color="#dd2a7b"/>
    <stop offset="70%" stop-color="#8134af"/>
    <stop offset="100%" stop-color="#515bd4"/>
  </linearGradient>
</defs>

<rect width="860" height="380" rx="16" fill="url(#cn-bg)"/>
<rect x="0.5" y="0.5" width="859" height="379" rx="15.5" stroke="url(#cn-border)" stroke-width="1.2"/>

<!-- Left Background Ambient Typography: "LET'S CONNECT." matching Image 2 -->
<g transform="translate(30, 0)">
  <text x="0" y="130" fill="#0d2248" font-family="{FONT_DISPLAY}" font-size="64" font-weight="900" letter-spacing="-1">LET'S</text>
  <text x="0" y="195" fill="#091836" font-family="{FONT_DISPLAY}" font-size="54" font-weight="900" letter-spacing="-1">CONNECT.</text>
</g>

<!-- Left: Mayukh's Cutout with Crisp White Glowing Sticker Outline matching Image 2 -->
<image x="15" y="45" width="280" height="325" href="data:image/png;base64,{sticker_b64}" xlink:href="data:image/png;base64,{sticker_b64}" preserveAspectRatio="xMidYMid meet"/>

<!-- RIGHT: Header matching Image 2 -->
<g transform="translate(330, 26)">
  <text x="0" y="10" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5" font-weight="700" letter-spacing="1.5">05 / START A CONVERSATION</text>
  <text x="0" y="36" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="24" font-weight="900" letter-spacing="0.5">BUILD SOMETHING GREAT.</text>
  <text x="0" y="56" fill="#64748b" font-family="{FONT_MONO}" font-size="11" font-weight="700">Ideas. Opportunities. Your next move.</text>
  
  <!-- Red slashes on far right matching Image 2 -->
  <text x="490" y="36" text-anchor="end" fill="#ff0055" font-family="{FONT_DISPLAY}" font-size="22" font-weight="900">///</text>
</g>

<!-- 3 Stacked Cards (ONLY LinkedIn, GitHub, Instagram - NO YouTube, NO 1:1 Mentorship) -->
<g transform="translate(330, 96)">
  <!-- Card 1: LinkedIn -->
  <g transform="translate(0, 0)">
    <rect width="490" height="58" rx="8" fill="#061226" stroke="#0A66C2" stroke-width="1.2"/>
    <rect x="14" y="12" width="34" height="34" rx="6" fill="#0A66C2"/>
    <text x="31" y="34" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="18" font-weight="900">in</text>
    
    <text x="60" y="26" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="14" font-weight="800">LinkedIn</text>
    <text x="60" y="44" fill="#00f0ff" font-family="{FONT_MONO}" font-size="10.5">Connect &amp; exchange ideas</text>
    
    <text x="468" y="35" text-anchor="middle" fill="#00f0ff" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
  </g>

  <!-- Card 2: GitHub -->
  <g transform="translate(0, 72)">
    <rect width="490" height="58" rx="8" fill="#061226" stroke="#475569" stroke-width="1.2"/>
    <rect x="14" y="12" width="34" height="34" rx="6" fill="#181717" stroke="#334155" stroke-width="0.8"/>
    <!-- GitHub SVG Icon -->
    <path transform="translate(21, 19) scale(0.85)" fill="#ffffff" d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
    
    <text x="60" y="26" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="14" font-weight="800">GitHub</text>
    <text x="60" y="44" fill="#cbd5e1" font-family="{FONT_MONO}" font-size="10.5">@mayukhbyte · Repositories &amp; code</text>
    
    <text x="468" y="35" text-anchor="middle" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
  </g>

  <!-- Card 3: Instagram -->
  <g transform="translate(0, 144)">
    <rect width="490" height="58" rx="8" fill="#061226" stroke="#E1306C" stroke-width="1.2"/>
    <rect x="14" y="12" width="34" height="34" rx="6" fill="url(#insta-grad)"/>
    <!-- Instagram camera icon -->
    <circle cx="31" cy="29" r="6" fill="none" stroke="#ffffff" stroke-width="1.8"/>
    <circle cx="37" cy="22" r="1.5" fill="#ffffff"/>
    <rect x="22" y="20" width="18" height="18" rx="4" fill="none" stroke="#ffffff" stroke-width="1.8"/>
    
    <text x="60" y="26" fill="#ffffff" font-family="{FONT_DISPLAY}" font-size="14" font-weight="800">Instagram</text>
    <text x="60" y="44" fill="#e2e8f0" font-family="{FONT_MONO}" font-size="10.5">@mayukhbyte · Builder updates &amp; life outside commit</text>
    
    <text x="468" y="35" text-anchor="middle" fill="#ff0055" font-family="{FONT_DISPLAY}" font-size="18" font-weight="800">→</text>
  </g>

  <!-- Footer Tagline matching Image 2 -->
  <text x="0" y="235" fill="#64748b" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="1">GOOD PEOPLE. GOOD IDEAS. LET'S TALK.</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "connect.svg"), "w", encoding="utf-8") as f:
    f.write(connect_svg)
print("wrote connect.svg")

print("All SVGs compiled successfully!")
