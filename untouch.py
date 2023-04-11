import git
import pathlib

def discard_changes_if_identical_to_previous_commit(file_path):
    repo = git.Repo(search_parent_directories=True)
    prev_commit = repo.head.commit.parents[0]

    # Get the contents of the target file in the current and previous commits
    current_file_content = repo.git.show(f"{repo.head.commit.hexsha}:{file_path}")
    prev_file_content = repo.git.show(f"{prev_commit.hexsha}:{file_path}")

    # Check if the contents of the file have changed in the current commit
    if current_file_content != prev_file_content:
        print(f"The file {file_path} has been modified in the current commit")
        return

    # Discard any changes and restore the file to the previous commit version
    repo.git.checkout(str(prev_commit), "--", file_path)
    print(f"The file {file_path} has been restored to its previous commit version")

# Get the current directory as a Path object
current_dir = pathlib.Path().resolve()

# Find all Python files in the current directory and its subdirectories
python_files = current_dir.glob("**/*.py")

# Check each Python file and discard changes if they are identical to their previous commit
for file_path in python_files:
    discard_changes_if_identical_to_previous_commit(str(file_path))
