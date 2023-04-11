"""
Replaces consecutive blank lines with a single one.
Preserves/ensures a blank line at the end of the file.
Only writes file if it is unchanged, to prevent spurious
Github commits by touching the file.
"""
from collections.abc import Iterator
from pathlib import Path

def filter_lines(lines: list[str]) -> Iterator[str]:
    prev_line: str = None
    for line in lines:
        if line.strip() or prev_line.strip():
            yield line
        prev_line = line

current_dir: Path = Path(".")
for file_path in current_dir.glob("*.py"):
    lines: list[str] = (
        file_path.read_text().strip().splitlines()
    )
    new_lines: list[str] = list(filter_lines(lines))
    new_text: str = "\n".join(new_lines) + "\n"
    if new_text != file_path.read_text():
        file_path.write_text(new_text)
