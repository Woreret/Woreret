from pathlib import Path
import re

svg_path = Path("dist/swamp.svg")

if not svg_path.exists():
    raise FileNotFoundError("dist/swamp.svg not found")

svg = svg_path.read_text(encoding="utf-8")

svg, hidden_count = re.subn(
    r"\.s\{",
    ".s{opacity:0;",
    svg,
    count=1,
)

if hidden_count == 0:
    raise RuntimeError("Could not find .s CSS rule")

svg, head_css_count = re.subn(
    r"\.s\.s0\{",
    ".s.s0{opacity:1;",
    svg,
    count=1,
)

if head_css_count == 0:
    raise RuntimeError("Could not find .s.s0 CSS rule")

# 3. Новая жаба
frog_svg = r'''
<g class="frog s s0">

  <!-- crown -->
  <path
    d="M1.5 4.2 L3 1.4 L5.2 3.7 L7 0.8 L8.8 3.7 L11 1.4 L12.5 4.2 Z"
    fill="#d8b932"
    stroke="#8f7617"
    stroke-width="0.8"
    stroke-linejoin="round"
  />

  <!-- body -->
  <ellipse
    cx="7"
    cy="9"
    rx="9"
    ry="6.8"
    fill="#56a03d"
    stroke="#244d28"
    stroke-width="1.3"
  />

  <!-- eye bumps -->
  <circle cx="2.2" cy="5.6" r="3.6" fill="#7dc457"/>
  <circle cx="11.8" cy="5.6" r="3.6" fill="#7dc457"/>

  <!-- pupils -->
  <circle cx="2.2" cy="5.6" r="1.55" fill="#111111"/>
  <circle cx="11.8" cy="5.6" r="1.55" fill="#111111"/>

  <!-- highlights -->
  <circle cx="1.7" cy="5.1" r="0.42" fill="#f3f4d7"/>
  <circle cx="11.3" cy="5.1" r="0.42" fill="#f3f4d7"/>

  <!-- face -->
  <ellipse
    cx="7"
    cy="10.1"
    rx="5.9"
    ry="3.9"
    fill="#a4d179"
    opacity="0.98"
  />

  <!-- nostrils -->
  <circle cx="5.2" cy="9.1" r="0.42" fill="#294529"/>
  <circle cx="8.8" cy="9.1" r="0.42" fill="#294529"/>

  <!-- smile -->
  <path
    d="M4.2 10.9 Q7 13.1 9.8 10.9"
    stroke="#1d2f1b"
    stroke-width="1.05"
    fill="none"
    stroke-linecap="round"
  />

  <!-- tiny cheeks -->
  <circle cx="4.1" cy="10.7" r="0.28" fill="#6fa94d" opacity="0.85"/>
  <circle cx="9.9" cy="10.7" r="0.28" fill="#6fa94d" opacity="0.85"/>

  <!-- front feet -->
  <path
    d="M3.2 14.2 L1.4 15.8"
    stroke="#3c7d31"
    stroke-width="1.7"
    stroke-linecap="round"
  />
  <path
    d="M10.8 14.2 L12.6 15.8"
    stroke="#3c7d31"
    stroke-width="1.7"
    stroke-linecap="round"
  />

</g>
'''

svg, frog_count = re.subn(
    r'<rect class="s s0"[^>]*/>',
    frog_svg,
    svg,
    count=1,
)

if frog_count == 0:
    raise RuntimeError('Could not find <rect class="s s0" ... />')

svg_path.write_text(svg, encoding="utf-8")

print("🐸 Frog v4 generated")
