"""Additional utility functions"""

import contextlib
import functools
import gzip
import re
import typing
import warnings
from pathlib import Path

from spellchecker.info import __version__

KeyT = str | bytes
PathOrStr = Path | str


def fail_after(version: str) -> typing.Callable:
    """Decorator to add to tests to ensure that they fail if a deprecated
    feature is not removed before the specified version

    Args:
        version (str): The version to check against"""
    pass


def deprecated(message: str = "") -> typing.Callable:
    """A simplistic decorator to mark functions as deprecated. The function
    will pass a message to the user on the first use of the function

    Args:
        message (str): The message to display if the function is deprecated
    """
    pass


def ensure_unicode(value: KeyT, encoding: str = "utf-8") -> str:
    """Simplify checking if passed in data are bytes or a string and decode
    bytes into unicode.

    Args:
        value (str): The input string (possibly bytes)
        encoding (str): The encoding to use if input is bytes
    Returns:
        str: The encoded string
    """
    pass


@contextlib.contextmanager
def __gzip_read(filename: PathOrStr, mode: str = "rb", encoding: str = "UTF-8") -> typing.Generator[KeyT, None, None]:
    """Context manager to correctly handle the decoding of the output of the gzip file

    Args:
        filename (str): The filename to open
        mode (str): The mode to read the data
        encoding (str): The file encoding to use
    Yields:
        str: The string data from the gzip file read
    """
    pass


@contextlib.contextmanager
def load_file(filename: PathOrStr, encoding: str) -> typing.Generator[KeyT, None, None]:
    """Context manager to handle opening a gzip or text file correctly and
    reading all the data

    Args:
        filename (str): The filename to open
        encoding (str): The file encoding to use
    Yields:
        str: The string data from the file read
    """
    pass


def write_file(filepath: PathOrStr, encoding: str, gzipped: bool, data: str) -> None:
    """Write the data to file either as a gzip file or text based on the
    gzipped parameter

    Args:
        filepath (str): The filename to open
        encoding (str): The file encoding to use
        gzipped (bool): Whether the file should be gzipped or not
        data (str): The data to be written out
    """
    pass


def _parse_into_words(text: str) -> typing.Iterable[str]:
    """Parse the text into words; currently removes punctuation except for
    apostrophizes.

    Args:
        text (str): The text to split into words
    """
    pass
