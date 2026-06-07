"""getpassword package.

This package exposes a simple helper for obtaining a password from the
user without echoing it to the terminal. It instead echos a '*' character for each character typed, and allows the user to use backspace to correct mistakes.
"""

from getpassword import getpass

__all__ = ["get_password", "__version__"]
__version__ = "0.1.0"


def get_password(prompt: str = "Password: ") -> str:
    """Read a password from stdin without echoing it.

    Args:
        prompt: The prompt text shown to the user.

    Returns:
        The entered password string.
    """
    return getpass(prompt)
