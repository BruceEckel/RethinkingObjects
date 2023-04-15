:: Run all checks; must be in `hatch shell` virtualenv:
black .
python .\remove_blanks.py
ruff check .
pytest
mypy .
