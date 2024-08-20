import os
import datetime

PURPLE = '\033[95m'
CYAN = '\033[96m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


def error(msg: str, indent=2) -> None:
    log_entry = f'{" " * indent}{_get_time()} ❌ {msg}'
    print(log_entry)


def success(msg: str, indent=2) -> None:
    log_entry = f'{" " * indent}{_get_time()} ✅ {msg}'
    print(log_entry)


def warning(msg: str, indent=2) -> None:
    log_entry = f'{" " * indent}{_get_time()} ⚠️  {msg}'
    print(log_entry)


def headline(msg: str, indent=0) -> None:
    log_entry = f'{os.linesep}{" " * indent}➜ {BOLD}{msg}{END}'
    print(log_entry)


def info(msg: str, indent=0) -> None:
    log_entry = f'{" " * indent}{_get_time()} {msg}'
    print(log_entry)

def _get_time() -> str:
    return str(datetime.datetime.now(datetime.UTC).isoformat("T") + "Z")