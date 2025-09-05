import re
import sys

if len(sys.argv) < 2:
    print("Usage: python increment_headers.py <file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# On commence par les niveaux les plus hauts pour éviter les collisions
max_part = 0

for line in content.splitlines():
    match = re.match(r'^#\s+(\d+)', line)
    if match:
        level = int(match.group(1))
        max_part = max(max_part, level)

for part in range(max_part + 1):
    content = re.sub(rf'^#\s+{part}', f'# {part+1}', content, flags=re.MULTILINE)

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
