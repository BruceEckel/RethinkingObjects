:: Run all checks; requires pip-installation of these programs:
black .
python .\remove_blanks.py
pytest
ruff check .
mypy .
