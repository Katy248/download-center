import sys

from .config import APP_ID


def print_error(msg: str):

    print(f"{APP_ID} ERROR: {msg}", file=sys.stderr)


def print_log(msg: str):

    print(f"{APP_ID} LOG: {msg}", file=sys.stderr)
