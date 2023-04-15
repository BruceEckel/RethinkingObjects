"""
Replaces consecutive blank lines with a single one.
Preserves/ensures a blank line at the end of the file.
Only writes file if it is unchanged.
"""
from collections.abc import Iterator
from pathlib import Path
from typing import Optional

def _clean_multiple_blanks(lines: list[str]) -> Iterator[str]:
    prev_line: str = ""
    for line in lines:
        if line.strip() or prev_line.strip():
            yield line
        prev_line = line

def deduplicate_blanks(text: str) -> str | None:
    lines: list[str] = text.strip().splitlines()
    new_lines: list[str] = list(_clean_multiple_blanks(lines))
    new_text: str = "\n".join(new_lines) + "\n"
    if new_text != text:
        return new_text
    return None

if __name__ == '__main__':        
    for fpath in Path(".").glob("*.py"):
        match deduplicate_blanks(fpath.read_text()):
            case None: continue  # No changes
            case str(text): fpath.write_text(new_text)
        # lines: list[str] = (
        #     fpath.read_text().strip().splitlines()
        # )
        # new_lines: list[str] = list(deduplicate_blanks(lines))
        # new_text: str = "\n".join(new_lines) + "\n"
        # if new_text != fpath.read_text():
        #     fpath.write_text(new_text)
