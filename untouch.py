from typing import List
import git
from pathlib import Path


def discard_changes_if_identical_to_previous_commit(file_path: Path) -> None:
    repo = git.Repo(file_path, search_parent_directories=True)
    current_file_content = file_path.read_text().strip()
    previous_file_content = repo.git.show(f"{repo.head.commit.hexsha}:{file_path}")
    previous_file_content = previous_file_content.strip()
    if current_file_content == previous_file_content:
        print(f"{file_path} has not been modified since the last commit.")
    else:
        print(f"{file_path} has been modified since the last commit. Discarding changes...")
        repo.git.checkout("--", str(file_path))


if __name__ == '__main__':
    python_files: List[Path] = list(Path(".").glob("*.py"))
    for file_path in python_files:
        discard_changes_if_identical_to_previous_commit(file_path)
