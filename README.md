# getpassword

A small Python utility for reading masked password input from the terminal.

This project provides a simple `get_password()` helper that accepts user input one character at a time, prints `*` for each keystroke, and supports backspace editing.

## Features

- Reads a password from the terminal without showing the raw characters
- Displays `*` for each character typed
- Supports backspace to correct mistakes
- Minimal dependency footprint

## Installation

This project includes packaging metadata in `pyproject.toml`, so it can be installed with:

```bash
pip install getpassword
```

For local development from the repository, install in editable mode:

```bash
python -m pip install -e .
```

If you prefer a normal local install:

```bash
python -m pip install .
```

The package dependency `readchar` will be installed automatically.

## Usage

```python
from getpassword import get_password

password = get_password("Password: ")
print("You entered", password)
```

You can also run the script directly from the repository:

```bash
python src/getpassword/getpassword.py
```

## Project structure

- `src/getpassword/getpassword.py` - core password input implementation
- `src/getpassword/__init__.py` - package entrypoint exposing `get_password`

## Dependency

- `readchar`

## Notes

This package is intended for simple console-based password entry. It does not provide advanced terminal handling or cross-platform terminal abstraction beyond the `readchar` dependency.
