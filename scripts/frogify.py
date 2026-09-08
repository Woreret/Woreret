from pathlib import Path
import re

svg_path = Path("dist/swamp.svg")

svg = svg_path.read_text(encoding="utf-8")

# Скрываем все части змейки кроме головы
svg = re.sub(
    r"\.s\{",
    ".s{opacity:0;",
    svg,
    count=1
)

# Возвращаем голову
svg = svg.replace(
    ".s.s0{",
    ".s.s0{opacity:1;"
)

# Делаем голову круглой и жабьей
svg = re.sub(
    r'<rect class="s s0"([^>]*)/>',
    r'''
<g class="frog s s0">

  <!-- body -->
  <ellipse cx="6" cy="7" rx="7" ry="6" fill="#5f9f3d"/>

  <!-- eyes -->
  <circle cx="2" cy="2" r="3" fill="#79c94b"/>
  <circle cx="10" cy="2" r="3" fill="#79c94b"/>

  <circle cx="2" cy="2" r="1.2" fill="#111"/>
  <circle cx="10" cy="2" r="1.2" fill="#111"/>

  <!-- mouth -->
  <path
    d="M2 8 Q6 11 10 8"
    stroke="#162b1c"
    stroke-width="1"
    fill="none"
    stroke-linecap="round"
  />

</g>
''',
    svg,
    count=1
)

svg_path.write_text(svg, encoding="utf-8")

print("🐸 swamp.svg frogified")
