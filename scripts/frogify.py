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

frog_svg = r'''
<g class="frog s s0">

  <!-- body -->
  <ellipse
    cx="7"
    cy="8"
    rx="8"
    ry="6"
    fill="#4f8f38"
    stroke="#244d28"
    stroke-width="1"
  />

  <!-- crown -->
  <path
    d="M2 4 L3 1 L5 3 L7 0 L9 3 L11 1 L12 4 Z"
    fill="#d8b932"
    stroke="#8f7617"
    stroke-width="0.7"
  />

  <!-- eye bumps -->
  <circle cx="2.5" cy="5" r="3.2" fill="#73b64b"/>
  <circle cx="11.5" cy="5" r="3.2" fill="#73b64b"/>

  <!-- eyes -->
  <circle cx="2.5" cy="5" r="1.4" fill="#111111"/>
  <circle cx="11.5" cy="5" r="1.4" fill="#111111"/>

  <!-- eye highlights -->
  <circle cx="2" cy="4.5" r="0.4" fill="#f2f2d5"/>
  <circle cx="11" cy="4.5" r="0.4" fill="#f2f2d5"/>

  <!-- muzzle -->
  <ellipse
    cx="7"
    cy="9"
    rx="5.5"
    ry="3.5"
    fill="#8ebc63"
  />

  <!-- nostrils -->
  <circle cx="5.3" cy="8" r="0.45" fill="#294529"/>
  <circle cx="8.7" cy="8" r="0.45" fill="#294529"/>

  <!-- mouth -->
  <path
    d="M4 10 Q7 12 10 10"
    stroke="#1d2f1b"
    stroke-width="1"
    fill="none"
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

print("🐸 Frog successfully generated")
