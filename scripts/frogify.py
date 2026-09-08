from pathlib import Path
import re

svg_path = Path("dist/swamp.svg")
svg = svg_path.read_text(encoding="utf-8")

svg = re.sub(
    r"\.s\{",
    ".s{opacity:0;",
    svg,
    count=1
)

svg = svg.replace(
    ".s.s0{",
    ".s.s0{opacity:1;"
)

svg = re.sub(
    r'<rect class="s s0"([^>]*)/>',
    r'''
<g class="frog s s0">

  <!-- crown -->
  <path
    d="M0 -3 L2 -8 L5 -4 L8 -9 L11 -4 L14 -8 L15 -3 Z"
    fill="#d8b932"
    stroke="#9c8420"
    stroke-width="0.8"
  />

  <!-- head -->
  <ellipse
    cx="7"
    cy="6"
    rx="8"
    ry="6.5"
    fill="#5f9f3d"
    stroke="#2d5f2c"
    stroke-width="1"
  />

  <!-- eye bumps -->
  <circle cx="2" cy="1" r="3.6" fill="#79c94b"/>
  <circle cx="12" cy="1" r="3.6" fill="#79c94b"/>

  <!-- eyes -->
  <circle cx="2" cy="1" r="1.5" fill="#171717"/>
  <circle cx="12" cy="1" r="1.5" fill="#171717"/>

  <!-- highlights -->
  <circle cx="1.5" cy="0.4" r="0.45" fill="#eeeecc"/>
  <circle cx="11.5" cy="0.4" r="0.45" fill="#eeeecc"/>

  <!-- cheeks -->
  <ellipse cx="0" cy="6" rx="2" ry="1.2" fill="#77ad45" opacity="0.7"/>
  <ellipse cx="14" cy="6" rx="2" ry="1.2" fill="#77ad45" opacity="0.7"/>

  <!-- mouth -->
  <path
    d="M2 7.5 Q7 11 12 7.5"
    stroke="#1b321b"
    stroke-width="1.2"
    fill="none"
    stroke-linecap="round"
  />

  <!-- tiny body -->
  <ellipse
    cx="7"
    cy="13"
    rx="5"
    ry="3"
    fill="#4c8736"
  />

  <!-- front legs -->
  <path
    d="M3 11 L0 14"
    stroke="#4c8736"
    stroke-width="2"
    stroke-linecap="round"
  />

  <path
    d="M11 11 L14 14"
    stroke="#4c8736"
    stroke-width="2"
    stroke-linecap="round"
  />

</g>
''',
    svg,
    count=1
)

svg_path.write_text(svg, encoding="utf-8")

print("🐸 crowned frog v2 generated")
