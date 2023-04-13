# Rethinking Objects

Code examples from my ***Rethinking Objects*** presentation at
PyCon 2023 in Salt Lake City.

The (Google) slides for the presentation are
[here](https://docs.google.com/presentation/d/1U0Mw4Aaz6mf5KpS-mZqKlK1H2_8JxXO6VF4axk9OPXY/edit?usp=sharing).

The examples in this repository assume you have Python 3.11 installed.

## Setup

After cloning this repo, use `pip` or `pipx` to (globally) install the `hatch`
build system.

Move to the root directory of the cloned repo and run:

```
hatch shell
```

This configures and enters a virtual environment. Now you can run:

```
pytest
ruff check .
mypy .
```

These verify the examples.
