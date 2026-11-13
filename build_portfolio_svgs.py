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

id_b64 = get_b64(os.path.join(ASSETS_DIR, "id.png"), 500)
char_b64 = get_b64(os.path.join(ASSETS_DIR, "right_pointing.png"), 500)

print("Building structured and polished Playbook SVGs...")

# ---------------------------------------------------------------------------
# 1. assets/hero.svg
# ---------------------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="380" viewBox="0 0 860 380" fill="none">
<defs>
  <linearGradient id="h-bg" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#070b16"/>
    <stop offset="50%" stop-color="#0c1322"/>
    <stop offset="100%" stop-color="#070b16"/>
  </linearGradient>
  <linearGradient id="h-border" x1="0" y1="0" x2="860" y2="380" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.6"/>
    <stop offset="50%" stop-color="#ff354f" stop-opacity="0.3"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0.5"/>
  </linearGradient>
  <linearGradient id="h-glow" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#247bff"/>
    <stop offset="100%" stop-color="#ff354f"/>
  </linearGradient>
  <linearGradient id="h-textgrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="50%" stop-color="#93c5fd"/>
    <stop offset="100%" stop-color="#247bff"/>
  </linearGradient>
  <pattern id="h-dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.12"/>
  </pattern>
  <clipPath id="h-name-clip">
    <rect x="50" y="75" width="520" height="65"/>
  </clipPath>
  <clipPath id="h-port-clip">
    <rect x="580" y="35" width="230" height="310" rx="20"/>
  </clipPath>
</defs>
<style>
  @keyframes h-rise {{
    0% {{ transform: translateY(70px); opacity: 0; }}
    100% {{ transform: translateY(0); opacity: 1; }}
  }}
  @keyframes h-blink {{
    0%, 49% {{ opacity: 1; }}
    50%, 100% {{ opacity: 0; }}
  }}
  @keyframes h-role1 {{
    0%, 20% {{ opacity: 1; transform: translateY(0); }}
    25%, 95% {{ opacity: 0; transform: translateY(-12px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
  }}
  @keyframes h-role2 {{
    0%, 20% {{ opacity: 0; transform: translateY(12px); }}
    25%, 45% {{ opacity: 1; transform: translateY(0); }}
    50%, 100% {{ opacity: 0; transform: translateY(-12px); }}
  }}
  @keyframes h-role3 {{
    0%, 45% {{ opacity: 0; transform: translateY(12px); }}
    50%, 70% {{ opacity: 1; transform: translateY(0); }}
    75%, 100% {{ opacity: 0; transform: translateY(-12px); }}
  }}
  @keyframes h-role4 {{
    0%, 70% {{ opacity: 0; transform: translateY(12px); }}
    75%, 95% {{ opacity: 1; transform: translateY(0); }}
    100% {{ opacity: 0; transform: translateY(-12px); }}
  }}
  @keyframes h-float {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-6px); }}
  }}
  .h-name {{ animation: h-rise 1s cubic-bezier(0.16, 1, 0.3, 1) forwards; }}
  .h-cur {{ animation: h-blink 1s infinite; }}
  .h-r1 {{ animation: h-role1 12s infinite; }}
  .h-r2 {{ animation: h-role2 12s infinite; }}
  .h-r3 {{ animation: h-role3 12s infinite; }}
  .h-r4 {{ animation: h-role4 12s infinite; }}
  .h-badge {{ animation: h-float 4s ease-in-out infinite; }}
</style>

<!-- Background -->
<rect width="860" height="380" rx="16" fill="url(#h-bg)"/>
<rect width="860" height="380" rx="16" fill="url(#h-dots)"/>
<rect x="0.5" y="0.5" width="859" height="379" rx="15.5" stroke="url(#h-border)" stroke-width="1"/>

<!-- Top Status Prompt Tag -->
<rect x="50" y="42" width="145" height="26" rx="6" fill="#131d33" stroke="#247bff" stroke-opacity="0.3"/>
<circle cx="62" cy="55" r="4" fill="#247bff"/>
<text x="74" y="59" fill="#94a3b8" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11" font-weight="600" letter-spacing="1">HEY THERE, I'M<tspan class="h-cur" fill="#ff354f">_</tspan></text>

<!-- Rising Mask Name Reveal -->
<g clip-path="url(#h-name-clip)">
  <g class="h-name">
    <text x="50" y="128" fill="url(#h-textgrad)" font-family="system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="42" font-weight="900" letter-spacing="-1">MAYUKH</text>
    <text x="242" y="128" fill="#ffffff" font-family="system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif" font-size="42" font-weight="900" letter-spacing="-1">BHATTACHARJEE</text>
  </g>
</g>

<!-- Cycling Roles (CSS staggered animation) -->
<g transform="translate(50, 168)">
  <rect x="0" y="-18" width="8" height="24" rx="2" fill="#247bff"/>
  <!-- Role 1 -->
  <text class="h-r1" x="18" y="0" fill="#38bdf8" font-family="system-ui,-apple-system,sans-serif" font-size="20" font-weight="700" letter-spacing="0.5">Full-Stack Developer</text>
  <!-- Role 2 -->
  <text class="h-r2" x="18" y="0" fill="#ff354f" font-family="system-ui,-apple-system,sans-serif" font-size="20" font-weight="700" letter-spacing="0.5">AI &amp; Vision Systems Builder</text>
  <!-- Role 3 -->
  <text class="h-r3" x="18" y="0" fill="#a855f7" font-family="system-ui,-apple-system,sans-serif" font-size="20" font-weight="700" letter-spacing="0.5">Fintech &amp; Security Engineer</text>
  <!-- Role 4 -->
  <text class="h-r4" x="18" y="0" fill="#34d399" font-family="system-ui,-apple-system,sans-serif" font-size="20" font-weight="700" letter-spacing="0.5">Open-Source Creator</text>
</g>

<!-- One-line pitch -->
<text x="50" y="218" fill="#94a3b8" font-family="system-ui,-apple-system,sans-serif" font-size="14.5" font-weight="400">
  Architecting intelligent applications, real-time security systems, and autonomous agent workflows.
</text>
<text x="50" y="242" fill="#64748b" font-family="system-ui,-apple-system,sans-serif" font-size="13" font-weight="400">
  Specializing in Go concurrency, Next.js full-stack systems, and practical AI tooling.
</text>

<!-- Location / Info Badges -->
<g transform="translate(50, 288)">
  <!-- Location Pill -->
  <rect x="0" y="0" width="105" height="32" rx="16" fill="#0f172a" stroke="#1e293b"/>
  <text x="14" y="20" font-size="12">📍</text>
  <text x="36" y="20" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="500">India</text>

  <!-- Open to Work Pill -->
  <rect x="115" y="0" width="180" height="32" rx="16" fill="#0f172a" stroke="#247bff" stroke-opacity="0.3"/>
  <circle cx="130" cy="16" r="4" fill="#10b981"/>
  <text x="142" y="20" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="500">Open to Opportunities</text>

  <!-- GitHub Tag -->
  <rect x="305" y="0" width="130" height="32" rx="16" fill="#0f172a" stroke="#1e293b"/>
  <text x="318" y="20" font-size="12">⚡</text>
  <text x="338" y="20" fill="#38bdf8" font-family="ui-monospace,SFMono-Regular,monospace" font-size="12" font-weight="600">@mayukhbyte</text>
</g>

<!-- Portrait Frame (Right) -->
<g>
  <rect x="580" y="35" width="230" height="310" rx="20" fill="#0b1120" stroke="url(#h-glow)" stroke-width="1.5"/>
  <g clip-path="url(#h-port-clip)">
    <image x="580" y="25" width="230" height="320" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
  </g>
  <!-- Inner Rim Light Border -->
  <rect x="580.5" y="35.5" width="229" height="309" rx="19.5" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>
</g>

<!-- Floating Status Badge -->
<g class="h-badge" transform="translate(540, 290)">
  <rect x="0" y="0" width="140" height="38" rx="19" fill="#0d1424" stroke="#247bff" stroke-width="1.2" filter="drop-shadow(0 4px 12px rgba(0,0,0,0.5))"/>
  <circle cx="20" cy="19" r="5" fill="#247bff"/>
  <text x="34" y="23" fill="#f8fafc" font-family="system-ui,-apple-system,sans-serif" font-size="12" font-weight="700">ONLINE NOW</text>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("wrote assets/hero.svg")

# ---------------------------------------------------------------------------
# 2. assets/about-life.svg
# ---------------------------------------------------------------------------
about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="360" viewBox="0 0 860 360" fill="none">
<defs>
  <linearGradient id="ab-bg" x1="0" y1="0" x2="860" y2="360" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#070b16"/>
    <stop offset="100%" stop-color="#0b1220"/>
  </linearGradient>
  <linearGradient id="ab-border" x1="0" y1="0" x2="860" y2="360" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0.2"/>
  </linearGradient>
  <pattern id="ab-dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.1"/>
  </pattern>
</defs>
<style>
  @keyframes ab-bar1 {{
    0% {{ width: 0; }}
    30%, 100% {{ width: 100px; }}
  }}
  @keyframes ab-bar2 {{
    0%, 33% {{ width: 0; }}
    63%, 100% {{ width: 100px; }}
  }}
  @keyframes ab-bar3 {{
    0%, 66% {{ width: 0; }}
    96%, 100% {{ width: 100px; }}
  }}
  @keyframes ab-slide1 {{
    0%, 30% {{ opacity: 1; transform: translateY(0); }}
    34%, 96% {{ opacity: 0; transform: translateY(10px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
  }}
  @keyframes ab-slide2 {{
    0%, 30% {{ opacity: 0; transform: translateY(-10px); }}
    34%, 63% {{ opacity: 1; transform: translateY(0); }}
    67%, 100% {{ opacity: 0; transform: translateY(10px); }}
  }}
  @keyframes ab-slide3 {{
    0%, 63% {{ opacity: 0; transform: translateY(-10px); }}
    67%, 96% {{ opacity: 1; transform: translateY(0); }}
    100% {{ opacity: 0; transform: translateY(10px); }}
  }}
  .bar-fill1 {{ animation: ab-bar1 12s infinite linear; }}
  .bar-fill2 {{ animation: ab-bar2 12s infinite linear; }}
  .bar-fill3 {{ animation: ab-bar3 12s infinite linear; }}
  .s1 {{ animation: ab-slide1 12s infinite; }}
  .s2 {{ animation: ab-slide2 12s infinite; }}
  .s3 {{ animation: ab-slide3 12s infinite; }}
</style>

<rect width="860" height="360" rx="16" fill="url(#ab-bg)"/>
<rect width="860" height="360" rx="16" fill="url(#ab-dots)"/>
<rect x="0.5" y="0.5" width="859" height="359" rx="15.5" stroke="url(#ab-border)" stroke-width="1"/>

<!-- Header -->
<text x="45" y="45" fill="#247bff" font-family="ui-monospace,SFMono-Regular,monospace" font-size="12" font-weight="700" letter-spacing="1.5">ABOUT // 01</text>
<text x="45" y="75" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="24" font-weight="800">Capabilities &amp; Active Explorations</text>

<!-- Left Column: Core Capabilities -->
<g transform="translate(45, 105)">
  <rect width="365" height="215" rx="14" fill="#0d1424" stroke="#1e293b"/>
  
  <!-- Cap 1 -->
  <g transform="translate(20, 20)">
    <rect width="32" height="32" rx="8" fill="#1e293b"/>
    <text x="9" y="21" fill="#38bdf8" font-family="ui-monospace,monospace" font-size="13" font-weight="800">01</text>
    <text x="44" y="16" fill="#f1f5f9" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="700">Full-Stack &amp; Web Platforms</text>
    <text x="44" y="32" fill="#94a3b8" font-family="system-ui,-apple-system,sans-serif" font-size="12">React · Next.js · Node.js · SvelteKit</text>
  </g>

  <!-- Divider -->
  <line x1="20" y1="75" x2="345" y2="75" stroke="#1e293b"/>

  <!-- Cap 2 -->
  <g transform="translate(20, 90)">
    <rect width="32" height="32" rx="8" fill="#1e293b"/>
    <text x="8" y="21" fill="#ff354f" font-family="ui-monospace,monospace" font-size="13" font-weight="800">02</text>
    <text x="44" y="16" fill="#f1f5f9" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="700">AI Education &amp; Vision</text>
    <text x="44" y="32" fill="#94a3b8" font-family="system-ui,-apple-system,sans-serif" font-size="12">GPT-4o · OpenCV · Adaptive Tutoring</text>
  </g>

  <!-- Divider -->
  <line x1="20" y1="145" x2="345" y2="145" stroke="#1e293b"/>

  <!-- Cap 3 -->
  <g transform="translate(20, 160)">
    <rect width="32" height="32" rx="8" fill="#1e293b"/>
    <text x="8" y="21" fill="#34d399" font-family="ui-monospace,monospace" font-size="13" font-weight="800">03</text>
    <text x="44" y="16" fill="#f1f5f9" font-family="system-ui,-apple-system,sans-serif" font-size="14" font-weight="700">Fintech &amp; Security Engineering</text>
    <text x="44" y="32" fill="#94a3b8" font-family="system-ui,-apple-system,sans-serif" font-size="12">Go Concurrency · Phishing Detection</text>
  </g>
</g>

<!-- Right Column: Animated Interests Carousel (4s per slide) -->
<g transform="translate(450, 105)">
  <rect width="365" height="215" rx="14" fill="#0d1424" stroke="#247bff" stroke-opacity="0.3"/>

  <!-- Three Progress Bar Segments -->
  <g transform="translate(25, 20)">
    <!-- Track 1 -->
    <rect x="0" y="0" width="100" height="4" rx="2" fill="#1e293b"/>
    <rect class="bar-fill1" x="0" y="0" width="0" height="4" rx="2" fill="#247bff"/>

    <!-- Track 2 -->
    <rect x="108" y="0" width="100" height="4" rx="2" fill="#1e293b"/>
    <rect class="bar-fill2" x="108" y="0" width="0" height="4" rx="2" fill="#ff354f"/>

    <!-- Track 3 -->
    <rect x="216" y="0" width="100" height="4" rx="2" fill="#1e293b"/>
    <rect class="bar-fill3" x="216" y="0" width="0" height="4" rx="2" fill="#a855f7"/>
  </g>

  <!-- Slide 1 -->
  <g class="s1" transform="translate(25, 55)">
    <text x="0" y="24" font-size="28">🎓</text>
    <text x="42" y="16" fill="#38bdf8" font-family="ui-monospace,monospace" font-size="11" font-weight="700" letter-spacing="1">PROJECT DOMAIN 01</text>
    <text x="42" y="36" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="18" font-weight="800">AI-Assisted Tutoring</text>
    
    <text x="0" y="80" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" font-weight="400">
      Creator of AI-Educator: delivering multi-level doubt
    </text>
    <text x="0" y="102" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" font-weight="400">
      solving, speech explanation, and adaptive quizzes.
    </text>
    <text x="0" y="130" fill="#64748b" font-family="ui-monospace,monospace" font-size="11">
      Stack: React 18 · TypeScript · Vite · OpenAI API
    </text>
  </g>

  <!-- Slide 2 -->
  <g class="s2" transform="translate(25, 55)">
    <text x="0" y="24" font-size="28">🛡️</text>
    <text x="42" y="16" fill="#ff354f" font-family="ui-monospace,monospace" font-size="11" font-weight="700" letter-spacing="1">PROJECT DOMAIN 02</text>
    <text x="42" y="36" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="18" font-weight="800">Aizen URL Safety Engine</text>
    
    <text x="0" y="80" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" font-weight="400">
      Concurrent Go backend with 21 goroutines evaluating
    </text>
    <text x="0" y="102" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" font-weight="400">
      39 security signals for phishing and fraud detection.
    </text>
    <text x="0" y="130" fill="#64748b" font-family="ui-monospace,monospace" font-size="11">
      Stack: Go (Gin) · SvelteKit 5 · Vercel Serverless
    </text>
  </g>

  <!-- Slide 3 -->
  <g class="s3" transform="translate(25, 55)">
    <text x="0" y="24" font-size="28">💳</text>
    <text x="42" y="16" fill="#a855f7" font-family="ui-monospace,monospace" font-size="11" font-weight="700" letter-spacing="1">PROJECT DOMAIN 03</text>
    <text x="42" y="36" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="18" font-weight="800">Paypaal Pro Financials</text>
    
    <text x="0" y="80" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" font-weight="400">
      Autonomous agent treasury platform with AI dispute
    </text>
    <text x="0" y="102" fill="#cbd5e1" font-family="system-ui,-apple-system,sans-serif" font-size="13.5" font-weight="400">
      synthesis, stock liquidation, and escrow payouts.
    </text>
    <text x="0" y="130" fill="#64748b" font-family="ui-monospace,monospace" font-size="11">
      Stack: Node.js · Express · AI Engine · SSE Streams
    </text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "about-life.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)
print("wrote assets/about-life.svg")

# ---------------------------------------------------------------------------
# 3. assets/stack.svg
# ---------------------------------------------------------------------------
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="420" viewBox="0 0 860 420" fill="none">
<defs>
  <linearGradient id="st-bg" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#070b16"/>
    <stop offset="100%" stop-color="#0c1322"/>
  </linearGradient>
  <linearGradient id="st-border" x1="0" y1="0" x2="860" y2="420" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="50%" stop-color="#ff354f" stop-opacity="0.2"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0.4"/>
  </linearGradient>
  <pattern id="st-dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.1"/>
  </pattern>
</defs>
<style>
  @keyframes orb-float1 {{
    0%, 100% {{ transform: translate(0, 0); }}
    50% {{ transform: translate(8px, -5px); }}
  }}
  @keyframes orb-float2 {{
    0%, 100% {{ transform: translate(0, 0); }}
    50% {{ transform: translate(-6px, 8px); }}
  }}
  @keyframes orb-float3 {{
    0%, 100% {{ transform: translate(0, 0); }}
    50% {{ transform: translate(6px, 6px); }}
  }}
  .ob1 {{ animation: orb-float1 6s ease-in-out infinite; }}
  .ob2 {{ animation: orb-float2 7s ease-in-out infinite; }}
  .ob3 {{ animation: orb-float3 8s ease-in-out infinite; }}
</style>

<rect width="860" height="420" rx="16" fill="url(#st-bg)"/>
<rect width="860" height="420" rx="16" fill="url(#st-dots)"/>
<rect x="0.5" y="0.5" width="859" height="419" rx="15.5" stroke="url(#st-border)" stroke-width="1"/>

<!-- Header -->
<text x="45" y="42" fill="#247bff" font-family="ui-monospace,SFMono-Regular,monospace" font-size="12" font-weight="700" letter-spacing="1.5">STACK // 02</text>
<text x="45" y="70" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="24" font-weight="800">Technical Ecosystem &amp; Orbits</text>

<!-- 3 Tilted Elliptical Orbits Area -->
<g transform="translate(430, 160)">
  <!-- Outer Glow -->
  <circle cx="0" cy="0" r="150" fill="#247bff" opacity="0.06" filter="blur(35px)"/>

  <!-- Orbit 1 (Major: 330, Minor: 85, tilt -12deg) -->
  <ellipse cx="0" cy="0" rx="330" ry="85" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="6 4" transform="rotate(-12)"/>
  
  <!-- Orbit 2 (Major: 230, Minor: 65, tilt 14deg) -->
  <ellipse cx="0" cy="0" rx="230" ry="65" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="5 3" transform="rotate(14)"/>

  <!-- Orbit 3 (Major: 135, Minor: 46, tilt -22deg) -->
  <ellipse cx="0" cy="0" rx="135" ry="46" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-opacity="0.4" transform="rotate(-22)"/>

  <!-- Nucleus / Core -->
  <circle cx="0" cy="0" r="28" fill="#0d1424" stroke="#247bff" stroke-width="2"/>
  <circle cx="0" cy="0" r="16" fill="#247bff" opacity="0.25"/>
  <text x="0" y="6" text-anchor="middle" fill="#38bdf8" font-family="ui-monospace,monospace" font-size="14" font-weight="800">&lt;/&gt;</text>

  <!-- Badges on Orbit 1 -->
  <g class="ob1" transform="translate(-280, -35)">
    <rect x="-42" y="-14" width="84" height="28" rx="14" fill="#0f172a" stroke="#3776AB" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="11" font-weight="700">🐍 Python</text>
  </g>
  <g class="ob1" transform="translate(260, 30)">
    <rect x="-44" y="-14" width="88" height="28" rx="14" fill="#0f172a" stroke="#F7DF1E" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="11" font-weight="700">⚡ JavaScript</text>
  </g>

  <!-- Badges on Orbit 2 -->
  <g class="ob2" transform="translate(-180, 50)">
    <rect x="-38" y="-14" width="76" height="28" rx="14" fill="#0f172a" stroke="#61DAFB" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="11" font-weight="700">⚛️ React</text>
  </g>
  <g class="ob2" transform="translate(170, -50)">
    <rect x="-40" y="-14" width="80" height="28" rx="14" fill="#0f172a" stroke="#00ADD8" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="11" font-weight="700">🐹 Go (Golang)</text>
  </g>

  <!-- Badges on Orbit 3 -->
  <g class="ob3" transform="translate(-90, -45)">
    <rect x="-42" y="-14" width="84" height="28" rx="14" fill="#0f172a" stroke="#5C3EE8" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="11" font-weight="700">👁️ OpenCV</text>
  </g>
  <g class="ob3" transform="translate(95, 38)">
    <rect x="-38" y="-14" width="76" height="28" rx="14" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
    <text x="0" y="4" text-anchor="middle" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="11" font-weight="700">▲ Next.js</text>
  </g>
</g>

<!-- Grouped Stack Chips (Bottom Cards) -->
<g transform="translate(45, 275)">
  <!-- Languages -->
  <g transform="translate(0, 0)">
    <rect width="180" height="115" rx="10" fill="#0d1424" stroke="#1e293b"/>
    <text x="14" y="24" fill="#38bdf8" font-family="ui-monospace,monospace" font-size="11" font-weight="700">LANGUAGES</text>
    <g transform="translate(14, 40)">
      <rect x="0" y="0" width="66" height="24" rx="6" fill="#1e293b"/><text x="33" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Python</text>
      <rect x="72" y="0" width="46" height="24" rx="6" fill="#1e293b"/><text x="95" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Go</text>
      <rect x="0" y="32" width="76" height="24" rx="6" fill="#1e293b"/><text x="38" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">JavaScript</text>
      <rect x="82" y="32" width="56" height="24" rx="6" fill="#1e293b"/><text x="110" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">C / C++</text>
    </g>
  </g>

  <!-- Frontend -->
  <g transform="translate(195, 0)">
    <rect width="180" height="115" rx="10" fill="#0d1424" stroke="#1e293b"/>
    <text x="14" y="24" fill="#ff354f" font-family="ui-monospace,monospace" font-size="11" font-weight="700">FRONTEND</text>
    <g transform="translate(14, 40)">
      <rect x="0" y="0" width="60" height="24" rx="6" fill="#1e293b"/><text x="30" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">React</text>
      <rect x="66" y="0" width="68" height="24" rx="6" fill="#1e293b"/><text x="100" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Next.js</text>
      <rect x="0" y="32" width="70" height="24" rx="6" fill="#1e293b"/><text x="35" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">SvelteKit</text>
      <rect x="76" y="32" width="74" height="24" rx="6" fill="#1e293b"/><text x="113" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Tailwind</text>
    </g>
  </g>

  <!-- Backend & DB -->
  <g transform="translate(390, 0)">
    <rect width="185" height="115" rx="10" fill="#0d1424" stroke="#1e293b"/>
    <text x="14" y="24" fill="#a855f7" font-family="ui-monospace,monospace" font-size="11" font-weight="700">BACKEND &amp; DATA</text>
    <g transform="translate(14, 40)">
      <rect x="0" y="0" width="64" height="24" rx="6" fill="#1e293b"/><text x="32" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Node.js</text>
      <rect x="70" y="0" width="64" height="24" rx="6" fill="#1e293b"/><text x="102" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Gin (Go)</text>
      <rect x="0" y="32" width="76" height="24" rx="6" fill="#1e293b"/><text x="38" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Supabase</text>
      <rect x="82" y="32" width="68" height="24" rx="6" fill="#1e293b"/><text x="116" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Firebase</text>
    </g>
  </g>

  <!-- Tools & AI -->
  <g transform="translate(590, 0)">
    <rect width="180" height="115" rx="10" fill="#0d1424" stroke="#1e293b"/>
    <text x="14" y="24" fill="#34d399" font-family="ui-monospace,monospace" font-size="11" font-weight="700">AI &amp; DEVOPS</text>
    <g transform="translate(14, 40)">
      <rect x="0" y="0" width="66" height="24" rx="6" fill="#1e293b"/><text x="33" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">OpenCV</text>
      <rect x="72" y="0" width="50" height="24" rx="6" fill="#1e293b"/><text x="97" y="16" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Git</text>
      <rect x="0" y="32" width="66" height="24" rx="6" fill="#1e293b"/><text x="33" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">GitHub</text>
      <rect x="72" y="32" width="60" height="24" rx="6" fill="#1e293b"/><text x="102" y="48" text-anchor="middle" fill="#e2e8f0" font-family="system-ui" font-size="11">Vercel</text>
    </g>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "stack.svg"), "w", encoding="utf-8") as f:
    f.write(stack_svg)
print("wrote assets/stack.svg")

# ---------------------------------------------------------------------------
# 4. assets/projects.svg (Dedicated Showcase for the 3 Repos!)
# ---------------------------------------------------------------------------
projects_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="340" viewBox="0 0 860 340" fill="none">
<defs>
  <linearGradient id="pj-bg" x1="0" y1="0" x2="860" y2="340" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#070b16"/>
    <stop offset="100%" stop-color="#0b1220"/>
  </linearGradient>
  <linearGradient id="pj-border" x1="0" y1="0" x2="860" y2="340" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="50%" stop-color="#ff354f" stop-opacity="0.25"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0.4"/>
  </linearGradient>
  <pattern id="pj-dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.08"/>
  </pattern>
</defs>

<rect width="860" height="340" rx="16" fill="url(#pj-bg)"/>
<rect width="860" height="340" rx="16" fill="url(#pj-dots)"/>
<rect x="0.5" y="0.5" width="859" height="339" rx="15.5" stroke="url(#pj-border)" stroke-width="1"/>

<!-- Header -->
<text x="45" y="40" fill="#247bff" font-family="ui-monospace,SFMono-Regular,monospace" font-size="12" font-weight="700" letter-spacing="1.5">FEATURED REPOSITORIES // 03</text>
<text x="45" y="68" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="22" font-weight="800">Flagship Engineering Projects</text>

<!-- 3 Structured Repo Cards -->
<g transform="translate(45, 95)">
  <!-- Card 1: Paypaal Pro -->
  <g transform="translate(0, 0)">
    <rect width="245" height="205" rx="12" fill="#0d1424" stroke="#ff354f" stroke-width="1.2"/>
    <rect width="245" height="6" rx="3" fill="#ff354f"/>
    
    <text x="18" y="34" font-size="20">💳</text>
    <text x="48" y="32" fill="#ffffff" font-family="system-ui,sans-serif" font-size="16" font-weight="800">Paypaal-pro</text>
    <text x="18" y="56" fill="#ff354f" font-family="ui-monospace,monospace" font-size="10.5" font-weight="600">FINTECH &amp; TREASURY VAULT</text>
    
    <text x="18" y="82" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      Autonomous agent platform
    </text>
    <text x="18" y="98" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      with AI dispute synthesis, stock
    </text>
    <text x="18" y="114" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      liquidation, &amp; escrow payouts.
    </text>

    <!-- Chips -->
    <g transform="translate(18, 140)">
      <rect x="0" y="0" width="60" height="20" rx="4" fill="#1e293b"/><text x="30" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">Express</text>
      <rect x="66" y="0" width="56" height="20" rx="4" fill="#1e293b"/><text x="94" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">Fintech</text>
      <rect x="128" y="0" width="50" height="20" rx="4" fill="#1e293b"/><text x="153" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">SSE API</text>
    </g>

    <text x="18" y="186" fill="#ff354f" font-family="system-ui" font-size="11" font-weight="700">★ Autonomous Agent Tech</text>
  </g>

  <!-- Card 2: AI Educator -->
  <g transform="translate(262, 0)">
    <rect width="245" height="205" rx="12" fill="#0d1424" stroke="#247bff" stroke-width="1.2"/>
    <rect width="245" height="6" rx="3" fill="#247bff"/>
    
    <text x="18" y="34" font-size="20">🎓</text>
    <text x="48" y="32" fill="#ffffff" font-family="system-ui,sans-serif" font-size="16" font-weight="800">ai-educator</text>
    <text x="18" y="56" fill="#38bdf8" font-family="ui-monospace,monospace" font-size="10.5" font-weight="600">AI TUTOR &amp; QUIZ PLATFORM</text>
    
    <text x="18" y="82" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      Multi-level AI doubt solving,
    </text>
    <text x="18" y="98" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      speech explanations &amp; adaptive
    </text>
    <text x="18" y="114" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      quizzes for student mastery.
    </text>

    <!-- Chips -->
    <g transform="translate(18, 140)">
      <rect x="0" y="0" width="56" height="20" rx="4" fill="#1e293b"/><text x="28" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">React 18</text>
      <rect x="62" y="0" width="50" height="20" rx="4" fill="#1e293b"/><text x="87" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">Node.js</text>
      <rect x="118" y="0" width="60" height="20" rx="4" fill="#1e293b"/><text x="148" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">OpenAI</text>
    </g>

    <text x="18" y="186" fill="#38bdf8" font-family="system-ui" font-size="11" font-weight="700">★ Open Source · MIT</text>
  </g>

  <!-- Card 3: Aizen-detector-url -->
  <g transform="translate(524, 0)">
    <rect width="245" height="205" rx="12" fill="#0d1424" stroke="#34d399" stroke-width="1.2"/>
    <rect width="245" height="6" rx="3" fill="#34d399"/>
    
    <text x="18" y="34" font-size="20">🛡️</text>
    <text x="48" y="32" fill="#ffffff" font-family="system-ui,sans-serif" font-size="16" font-weight="800">Aizen-detector-url</text>
    <text x="18" y="56" fill="#34d399" font-family="ui-monospace,monospace" font-size="10.5" font-weight="600">LIVE SECURITY CRAWLER</text>
    
    <text x="18" y="82" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      21 concurrent Go goroutines
    </text>
    <text x="18" y="98" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      evaluating 39 security signals
    </text>
    <text x="18" y="114" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12" font-weight="400">
      for real-time phishing defense.
    </text>

    <!-- Chips -->
    <g transform="translate(18, 140)">
      <rect x="0" y="0" width="48" height="20" rx="4" fill="#1e293b"/><text x="24" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">Go</text>
      <rect x="54" y="0" width="64" height="20" rx="4" fill="#1e293b"/><text x="86" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">SvelteKit</text>
      <rect x="124" y="0" width="56" height="20" rx="4" fill="#1e293b"/><text x="152" y="14" text-anchor="middle" fill="#94a3b8" font-family="system-ui" font-size="10">Vercel</text>
    </g>

    <text x="18" y="186" fill="#34d399" font-family="system-ui" font-size="11" font-weight="700">★ 21 Concurrent Checks</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "projects.svg"), "w", encoding="utf-8") as f:
    f.write(projects_svg)
print("wrote assets/projects.svg")

# ---------------------------------------------------------------------------
# 5. assets/id-dashboard.svg
# ---------------------------------------------------------------------------
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="400" viewBox="0 0 860 400" fill="none">
<defs>
  <linearGradient id="id-bg" x1="0" y1="0" x2="860" y2="400" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#070b16"/>
    <stop offset="100%" stop-color="#0c1424"/>
  </linearGradient>
  <linearGradient id="id-border" x1="0" y1="0" x2="860" y2="400" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0.25"/>
  </linearGradient>
  <pattern id="id-dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.08"/>
  </pattern>
  <clipPath id="lanyard-port">
    <rect x="20" y="55" width="160" height="150" rx="10"/>
  </clipPath>
  <linearGradient id="foil-sweep" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="45%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="50%" stop-color="#ffffff" stop-opacity="0.35"/>
    <stop offset="55%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
  </linearGradient>
</defs>
<style>
  @keyframes id-swing {{
    0% {{ transform: rotate(0deg); }}
    50% {{ transform: rotate(1.7deg); }}
    100% {{ transform: rotate(-1.7deg); }}
  }}
  @keyframes id-foil {{
    0% {{ transform: translateX(-220px); }}
    40%, 100% {{ transform: translateX(250px); }}
  }}
  .lanyard-card {{
    transform-origin: 145px 0px;
    animation: id-swing 5s ease-in-out infinite alternate;
  }}
  .foil-shine {{
    animation: id-foil 6s infinite ease-in-out;
  }}
</style>

<rect width="860" height="400" rx="16" fill="url(#id-bg)"/>
<rect width="860" height="400" rx="16" fill="url(#id-dots)"/>
<rect x="0.5" y="0.5" width="859" height="399" rx="15.5" stroke="url(#id-border)" stroke-width="1"/>

<!-- Header -->
<text x="45" y="38" fill="#247bff" font-family="ui-monospace,SFMono-Regular,monospace" font-size="12" font-weight="700" letter-spacing="1.5">VERIFIED CREDENTIALS // 04</text>
<text x="45" y="65" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="22" font-weight="800">Lanyard ID &amp; Developer Dashboard</text>

<!-- Hanging Lanyard Assembly (Left) -->
<g class="lanyard-card">
  <!-- Lanyard Strap entering from top -->
  <rect x="135" y="0" width="20" height="28" fill="#1e293b" rx="2"/>
  <line x1="145" y1="0" x2="145" y2="28" stroke="#ff354f" stroke-width="2"/>

  <!-- Metal Clasp -->
  <rect x="130" y="26" width="30" height="12" rx="3" fill="#64748b" stroke="#cbd5e1" stroke-width="0.8"/>
  <circle cx="145" cy="32" r="3" fill="#334155"/>
  <ellipse cx="145" cy="42" rx="6" ry="6" fill="none" stroke="#94a3b8" stroke-width="2.5"/>

  <!-- ID Badge Body (200 x 310) -->
  <g transform="translate(45, 48)">
    <rect width="200" height="310" rx="14" fill="#0d1424" stroke="#247bff" stroke-width="1.5"/>
    <rect width="200" height="310" rx="14" fill="#111c33" opacity="0.6"/>

    <!-- ID Header Bar -->
    <rect width="200" height="36" rx="14" fill="#247bff"/>
    <rect y="22" width="200" height="14" fill="#247bff"/>
    <text x="100" y="24" text-anchor="middle" fill="#ffffff" font-family="system-ui" font-size="11" font-weight="800" letter-spacing="1.5">DEVELOPER PASS</text>

    <!-- Portrait Window -->
    <rect x="20" y="55" width="160" height="150" rx="10" fill="#090d16" stroke="#1e293b"/>
    <g clip-path="url(#lanyard-port)">
      <image x="20" y="50" width="160" height="160" href="data:image/png;base64,{id_b64}" preserveAspectRatio="xMidYMid slice"/>
    </g>
    <rect x="20" y="55" width="160" height="150" rx="10" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>

    <!-- Foil Light Sweep across portrait -->
    <g clip-path="url(#lanyard-port)">
      <rect class="foil-shine" x="0" y="55" width="100" height="150" fill="url(#foil-sweep)"/>
    </g>

    <!-- Details -->
    <text x="22" y="224" fill="#ffffff" font-family="system-ui" font-size="14" font-weight="800">MAYUKH B.</text>
    <text x="22" y="240" fill="#38bdf8" font-family="ui-monospace,monospace" font-size="10" font-weight="600">ID: MB-2026-DEV</text>
    <text x="22" y="254" fill="#94a3b8" font-family="system-ui" font-size="10">AUTH: GITHUB // MAYUKHBYTE</text>

    <!-- Barcode simulation -->
    <g transform="translate(22, 266)">
      <rect x="0" y="0" width="2" height="24" fill="#e2e8f0"/>
      <rect x="4" y="0" width="4" height="24" fill="#e2e8f0"/>
      <rect x="10" y="0" width="1" height="24" fill="#e2e8f0"/>
      <rect x="13" y="0" width="3" height="24" fill="#e2e8f0"/>
      <rect x="18" y="0" width="1" height="24" fill="#e2e8f0"/>
      <rect x="21" y="0" width="5" height="24" fill="#e2e8f0"/>
      <rect x="28" y="0" width="2" height="24" fill="#e2e8f0"/>
      <rect x="33" y="0" width="3" height="24" fill="#e2e8f0"/>
      <rect x="38" y="0" width="2" height="24" fill="#e2e8f0"/>
      <rect x="43" y="0" width="4" height="24" fill="#e2e8f0"/>
      <rect x="50" y="0" width="1" height="24" fill="#e2e8f0"/>
      <rect x="53" y="0" width="4" height="24" fill="#e2e8f0"/>
      <rect x="60" y="0" width="2" height="24" fill="#e2e8f0"/>
      <rect x="65" y="0" width="3" height="24" fill="#e2e8f0"/>
      <rect x="71" y="0" width="1" height="24" fill="#e2e8f0"/>
      <rect x="75" y="0" width="5" height="24" fill="#e2e8f0"/>
      <rect x="83" y="0" width="2" height="24" fill="#e2e8f0"/>
      <rect x="88" y="0" width="4" height="24" fill="#e2e8f0"/>
      <rect x="95" y="0" width="1" height="24" fill="#e2e8f0"/>
      <rect x="99" y="0" width="3" height="24" fill="#e2e8f0"/>
      <rect x="105" y="0" width="4" height="24" fill="#e2e8f0"/>
      <rect x="112" y="0" width="2" height="24" fill="#e2e8f0"/>
      <rect x="117" y="0" width="3" height="24" fill="#e2e8f0"/>
      <rect x="123" y="0" width="5" height="24" fill="#e2e8f0"/>
      <rect x="131" y="0" width="1" height="24" fill="#e2e8f0"/>
      <rect x="135" y="0" width="4" height="24" fill="#e2e8f0"/>
      <rect x="142" y="0" width="2" height="24" fill="#e2e8f0"/>
      <rect x="147" y="0" width="4" height="24" fill="#e2e8f0"/>
      <rect x="153" y="0" width="2" height="24" fill="#e2e8f0"/>
    </g>
    <text x="100" y="300" text-anchor="middle" fill="#64748b" font-family="ui-monospace,monospace" font-size="8" letter-spacing="2">9 8 2 7 1 4 0 6 3 2 1</text>
  </g>
</g>

<!-- Dashboard Grid (Right) -->
<g transform="translate(285, 85)">
  <!-- Tile 1: Repositories -->
  <g transform="translate(0, 0)">
    <rect width="250" height="120" rx="12" fill="#0d1424" stroke="#1e293b"/>
    <text x="20" y="32" fill="#94a3b8" font-family="ui-monospace,monospace" font-size="11" font-weight="700">PUBLIC REPOSITORIES</text>
    <text x="20" y="75" fill="#38bdf8" font-family="system-ui" font-size="36" font-weight="900">12+</text>
    <text x="20" y="100" fill="#64748b" font-family="system-ui" font-size="12">AI apps, utilities &amp; platforms</text>
  </g>

  <!-- Tile 2: Contributions -->
  <g transform="translate(270, 0)">
    <rect width="250" height="120" rx="12" fill="#0d1424" stroke="#1e293b"/>
    <text x="20" y="32" fill="#94a3b8" font-family="ui-monospace,monospace" font-size="11" font-weight="700">ANNUAL CONTRIBUTIONS</text>
    <text x="20" y="75" fill="#ff354f" font-family="system-ui" font-size="36" font-weight="900">64+</text>
    <text x="20" y="100" fill="#64748b" font-family="system-ui" font-size="12">Verified GitHub Activity</text>
  </g>

  <!-- Tile 3: Focus -->
  <g transform="translate(0, 140)">
    <rect width="250" height="120" rx="12" fill="#0d1424" stroke="#1e293b"/>
    <text x="20" y="32" fill="#94a3b8" font-family="ui-monospace,monospace" font-size="11" font-weight="700">FLAGSHIP REPOSITORIES</text>
    <text x="20" y="68" fill="#ffffff" font-family="system-ui" font-size="17" font-weight="800">ai-educator · Paypaal</text>
    <text x="20" y="96" fill="#34d399" font-family="system-ui" font-size="12" font-weight="600">● aizen-detector</text>
  </g>

  <!-- Tile 4: Status -->
  <g transform="translate(270, 140)">
    <rect width="250" height="120" rx="12" fill="#0d1424" stroke="#247bff" stroke-opacity="0.3"/>
    <text x="20" y="32" fill="#94a3b8" font-family="ui-monospace,monospace" font-size="11" font-weight="700">COLLABORATION STATUS</text>
    <text x="20" y="68" fill="#f8fafc" font-family="system-ui" font-size="20" font-weight="800">Open to Projects</text>
    <text x="20" y="96" fill="#38bdf8" font-family="system-ui" font-size="12" font-weight="500">Freelance · Full-Time · AI Systems</text>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "id-dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(id_dashboard_svg)
print("wrote assets/id-dashboard.svg")

# ---------------------------------------------------------------------------
# 6. assets/connect.svg
# ---------------------------------------------------------------------------
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="320" viewBox="0 0 860 320" fill="none">
<defs>
  <linearGradient id="cn-bg" x1="0" y1="0" x2="860" y2="320" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#070b16"/>
    <stop offset="100%" stop-color="#0c1322"/>
  </linearGradient>
  <linearGradient id="cn-border" x1="0" y1="0" x2="860" y2="320" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#247bff" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0.2"/>
  </linearGradient>
  <pattern id="cn-dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.1"/>
  </pattern>
  <clipPath id="cn-char-clip">
    <rect x="30" y="20" width="260" height="280" rx="16"/>
  </clipPath>
</defs>
<style>
  @keyframes cn-nudge {{
    0%, 100% {{ transform: translateX(0); }}
    50% {{ transform: translateX(6px); }}
  }}
  .nudge-arrow {{
    animation: cn-nudge 1.8s ease-in-out infinite;
  }}
</style>

<rect width="860" height="320" rx="16" fill="url(#cn-bg)"/>
<rect width="860" height="320" rx="16" fill="url(#cn-dots)"/>
<rect x="0.5" y="0.5" width="859" height="319" rx="15.5" stroke="url(#cn-border)" stroke-width="1"/>

<!-- Pointing Character on Left -->
<g clip-path="url(#cn-char-clip)">
  <image x="20" y="10" width="270" height="300" href="data:image/png;base64,{char_b64}" preserveAspectRatio="xMidYMid slice"/>
</g>
<!-- Subtle accent frame around character area -->
<rect x="29" y="19" width="262" height="282" rx="16" fill="none" stroke="#247bff" stroke-width="1" stroke-opacity="0.25"/>

<!-- Header / Prompt (Right side) -->
<g transform="translate(320, 35)">
  <text x="0" y="12" fill="#247bff" font-family="ui-monospace,SFMono-Regular,monospace" font-size="12" font-weight="700" letter-spacing="1.5">CONNECT // 05</text>
  <text x="0" y="38" fill="#ffffff" font-family="system-ui,-apple-system,sans-serif" font-size="24" font-weight="800">Let's Connect &amp; Collaborate</text>
  <text x="0" y="60" fill="#94a3b8" font-family="system-ui,-apple-system,sans-serif" font-size="13">Have an idea, engineering opportunity, or project? Reach out directly:</text>
</g>

<!-- Generously Spaced Social Cards (Right Side) -->
<g transform="translate(320, 115)">
  <!-- LinkedIn Card (Top - Featured prominently) -->
  <g transform="translate(0, 0)">
    <rect width="495" height="52" rx="10" fill="#0d1424" stroke="#0A66C2" stroke-width="1.4"/>
    <!-- LinkedIn Icon -->
    <rect x="14" y="11" width="30" height="30" rx="6" fill="#0A66C2"/>
    <text x="29" y="31" text-anchor="middle" fill="#ffffff" font-family="system-ui" font-size="16" font-weight="900">in</text>
    
    <text x="56" y="24" fill="#f8fafc" font-family="system-ui" font-size="13.5" font-weight="700">LinkedIn Profile</text>
    <text x="56" y="40" fill="#38bdf8" font-family="system-ui" font-size="11">Mayukh Bhattacharjee · Professional Network</text>
    
    <g class="nudge-arrow" transform="translate(455, 30)">
      <text x="0" y="0" fill="#0A66C2" font-family="system-ui" font-size="18" font-weight="800">→</text>
    </g>
  </g>

  <!-- GitHub Card (Middle) -->
  <g transform="translate(0, 64)">
    <rect width="495" height="52" rx="10" fill="#0d1424" stroke="#38bdf8" stroke-width="1"/>
    <!-- GitHub Icon -->
    <rect x="14" y="11" width="30" height="30" rx="6" fill="#1e293b"/>
    <text x="29" y="31" text-anchor="middle" fill="#ffffff" font-size="16">🐙</text>
    
    <text x="56" y="24" fill="#f8fafc" font-family="system-ui" font-size="13.5" font-weight="700">GitHub Profile</text>
    <text x="56" y="40" fill="#94a3b8" font-family="system-ui" font-size="11">@mayukhbyte · Repositories, commits &amp; code</text>
    
    <g class="nudge-arrow" transform="translate(455, 30)">
      <text x="0" y="0" fill="#38bdf8" font-family="system-ui" font-size="18" font-weight="800">→</text>
    </g>
  </g>

  <!-- Email Card (Bottom) -->
  <g transform="translate(0, 128)">
    <rect width="495" height="52" rx="10" fill="#0d1424" stroke="#ff354f" stroke-width="1"/>
    <!-- Email Icon -->
    <rect x="14" y="11" width="30" height="30" rx="6" fill="#ff354f"/>
    <text x="29" y="31" text-anchor="middle" fill="#ffffff" font-size="14">✉️</text>
    
    <text x="56" y="24" fill="#f8fafc" font-family="system-ui" font-size="13.5" font-weight="700">Direct Inquiries</text>
    <text x="56" y="40" fill="#94a3b8" font-family="system-ui" font-size="11">mayukhbhttchrj@gmail.com · Collaborations &amp; Opportunities</text>
    
    <g class="nudge-arrow" transform="translate(455, 30)">
      <text x="0" y="0" fill="#ff354f" font-family="system-ui" font-size="18" font-weight="800">→</text>
    </g>
  </g>
</g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "connect.svg"), "w", encoding="utf-8") as f:
    f.write(connect_svg)
print("wrote assets/connect.svg")
print("All 6 cards generated successfully!")
