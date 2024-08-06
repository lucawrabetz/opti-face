import datetime
import re
import shutil
import warnings

from optiface.utils import _DATETIME_FORMAT

_SPECIAL_CHAR = "-"
_OPTIFACE_UI_EMOJI = " :-] "
_PRECISION = 2


def blank_line() -> None:
    print()


def separator_line() -> None:
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    num_characters = terminal_width // 2
    separator_line = f"{_SPECIAL_CHAR} " * num_characters + f"{_SPECIAL_CHAR}"
    print(separator_line)


def separator_block() -> None:
    separator_line()
    separator_line()


def format_numbers_in_string(msg: str) -> str:
    if type(msg) != str:
        warnings.warn(
            f"Expected string in format_numbers_in_string, got {type(msg)}. Cannot guarantee proper formatting."
        )
        return msg
    pattern = re.compile(r"(\d+\.\d+)")

    def repl(match):
        return f"{float(match.group()):.{_PRECISION}f}"

    return pattern.sub(repl, msg)


def opti_indentstring(time: bool = True) -> str:
    if time:
        return f"{_OPTIFACE_UI_EMOJI} [{datetime.datetime.now().strftime(_DATETIME_FORMAT)}] "
    return f"{_OPTIFACE_UI_EMOJI} "


def header(msg: str) -> None:
    blank_line()
    separator_block()
    msg = format_numbers_in_string(msg)
    print(f"{opti_indentstring(time=False)}{msg}...")
    separator_block()
    blank_line()


def subheader(msg: str) -> None:
    msg = format_numbers_in_string(msg)
    blank_line()
    print(f"{opti_indentstring(time=False)}{msg}...")
    blank_line()


def special(msg: str) -> None:
    msg = format_numbers_in_string(msg)
    print(f"{opti_indentstring()}--> {msg}! <--")


def body(msg: str) -> None:
    msg = format_numbers_in_string(msg)
    print(f"{opti_indentstring()}-> {msg}.")
