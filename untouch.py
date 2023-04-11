from pathlib import Path
import git

def discard_changes_if_identical_to_previous_commit(file_path: Path) -> None:
    repo = git.Repo(file_path, search_parent_directories=True)
    current_file_content = file_path.read_text()
    prev_commit_content = repo.git.show(f"{repo.head.commit.hexsha}~1:{file_path}")
    if current_file_content == prev_commit_content:
        repo.git.checkout('--', file_path)
        print(f"{file_path} is unchanged and has been restored to its previous state.")
    else:
        print(f"{file_path} has been modified since its previous commit and has not been restored.")

for file_path in Path('.').glob('*.py'):
    discard_changes_if_identical_to_previous_commit(file_path)
