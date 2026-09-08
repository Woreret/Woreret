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
    cy="10.2"
    rx="10.2"
    ry="7.5"
    fill="#5aaa3d"
    stroke="#234827"
    stroke-width="1.45"
  />

  <!-- eye bumps -->
  <circle cx="1.9" cy="6.3" r="4" fill="#85cf5f"/>
  <circle cx="12.1" cy="6.3" r="4" fill="#85cf5f"/>

  <!-- pupils -->
  <circle cx="1.9" cy="6.3" r="1.7" fill="#111111"/>
  <circle cx="12.1" cy="6.3" r="1.7" fill="#111111"/>

  <!-- highlights -->
  <circle cx="1.3" cy="5.7" r="0.45" fill="#f6f7db"/>
  <circle cx="11.5" cy="5.7" r="0.45" fill="#f6f7db"/>

  <!-- face -->
  <ellipse
    cx="7"
    cy="11.5"
    rx="6.5"
    ry="4.4"
    fill="#aedc84"
    opacity="0.98"
  />

  <!-- nostrils -->
  <circle cx="5" cy="10.2" r="0.45" fill="#294529"/>
  <circle cx="9" cy="10.2" r="0.45" fill="#294529"/>

  <!-- smile -->
  <path
    d="M4.2 12.2 Q7 14.7 9.8 12.2"
    stroke="#1b2c1a"
    stroke-width="1.15"
    fill="none"
    stroke-linecap="round"
  />

  <!-- cheeks -->
  <circle cx="4.1" cy="12" r="0.32" fill="#72ae50"/>
  <circle cx="9.9" cy="12" r="0.32" fill="#72ae50"/>

  <!-- front feet -->
  <path
    d="M3.2 16 L1.2 17.8"
    stroke="#3c7d31"
    stroke-width="1.9"
    stroke-linecap="round"
  />
  <path
    d="M10.8 16 L12.8 17.8"
    stroke="#3c7d31"
    stroke-width="1.9"
    stroke-linecap="round"
  />

  <!-- crown -->
  <g class="frog-crown">
    <path
      d="M1 1.5
         L4 3.8
         L7 0.7
         L10 3.8
         L13 1.5
         L11.3 6
         L2.7 6
         Z"
      fill="#ffd84d"
      stroke="#785000"
      stroke-width="0.8"
      stroke-linejoin="round"
    />

    <!-- bright bottom band -->
    <path
      d="M3.2 5.2 H10.8"
      stroke="#fff2a1"
      stroke-width="0.8"
      stroke-linecap="round"
    />

    <!-- central jewel -->
    <circle
      cx="7"
      cy="3.8"
      r="0.9"
      fill="#e94343"
      stroke="#963020"
      stroke-width="0.3"
    />
  </g>

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

print("🐸 Frog with crown generated")
