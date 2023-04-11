"""
Skips consecutive blank lines.
Preserves/ensures a blank line at the end of the file.
"""
from pathlib import Path

current_dir = Path('.')
for file_path in current_dir.glob('*.py'):
    lines = file_path.read_text().splitlines()
    new_lines = []
    for i, line in enumerate(lines):
        if i < len(lines) - 2 and not line.strip() and not lines[i + 1].strip():
            continue
        new_lines.append(line)
    if lines[-1].strip() and (len(lines) == 1 or lines[-2].strip()):
        new_lines.append(lines[-1])
    file_path.write_text('\n'.join(new_lines))
