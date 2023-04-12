# Rethinking Objects

Code examples from the presentation **Rethinking Objects** presented at
PyCon 2023 in Salt Lake City.

You can find the (Google) slides for the presentation
[here](https://docs.google.com/presentation/d/1U0Mw4Aaz6mf5KpS-mZqKlK1H2_8JxXO6VF4axk9OPXY/edit?usp=sharing).

After cloning this repo, use `pip` or `pipx` to install the `hatch`
build system. Move to the root directory of the cloned repo. Then
run:
```
hatch shell
```
Which sets up and configures a virtual environment. Now you can run:
```
pytest
ruff check .
mypy .
```
These verify the code.
