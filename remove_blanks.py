"""
For presentations only, where multiple blank lines use
up valuable screen real estate. Cleans up after running Black.

Replaces consecutive blank lines with a single one.
Ensures a single blank line at the end of the file.
Strips blanks at the beginning of the file.
Only writes file if it is unchanged.
"""
from collections.abc import Generator
from pathlib import Path

def _clean_multiple_blanks(lines: list[str]) -> Generator[str, None, None]:
    prev_line: str = ""
    for line in lines:
        if line.strip() or prev_line.strip():
            yield line
        prev_line = line

def deduplicate_blanks(original: str) -> str | None:
    lines: list[str] = original.strip().splitlines()
    new_lines: list[str] = list(_clean_multiple_blanks(lines))
    new_text: str = "\n".join(new_lines) + "\n"
    if new_text != original:
        return new_text
    return None

if __name__ == "__main__":
    for fpath in Path(".").glob("*.py"):
        match deduplicate_blanks(fpath.read_text()):
            case None:
                continue  # No changes
            case str(text):
                fpath.write_text(text)
