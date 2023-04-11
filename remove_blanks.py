"""
Skips consecutive blank lines.
Preserves/ensures a blank line at the end of the file.
Only writes file if it is unchanged, to prevent spurious
Github commits from touching the file.
"""
from pathlib import Path

def filter_lines(lines):
    prev_line = None
    for line in lines:
        if line.strip() or prev_line.strip():
            yield line
        prev_line = line

current_dir = Path('.')
for file_path in current_dir.glob('*.py'):
    lines = file_path.read_text().strip().splitlines()
    new_lines = list(filter_lines(lines))
    new_text = '\n'.join(new_lines) + '\n'
    if new_text != file_path.read_text():
        file_path.write_text(new_text)
