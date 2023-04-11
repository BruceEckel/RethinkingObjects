from typing import List, Optional
from pathlib import Path
import git

def discard_changes_if_identical_to_previous_commit(file_path: Path) -> Optional[str]:
    try:
        repo = git.Repo(".", search_parent_directories=True)
    except git.InvalidGitRepositoryError:
        print("Error: Not inside a Git repository")
        return None

    if file_path.is_absolute():
        file_path = file_path.relative_to(repo.working_dir)

    # check whether the file has been modified
    if repo.is_dirty(file_path):
        # discard changes
        try:
            repo.git.checkout(file_path)
            return f"Discarded changes for {file_path}"
        except git.GitCommandError as e:
            return f"Error discarding changes for {file_path}: {e.stderr.strip()}"
    else:
        return f"{file_path} has not been modified"

if __name__ == '__main__':
    python_files: List[Path] = list(Path(".").glob("*.py"))
    for file_path in python_files:
        discard_changes_if_identical_to_previous_commit(file_path)
