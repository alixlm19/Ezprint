from sys import stdout
from typing import Any

_output_stream = stdout


def set_output_stream(out: Any):
    """
    Takes in an output stream at sets it as the active output stream.
    
    Parameters
    ----------
    out: Any
        Output stream.
    """
    has_write_method = getattr(out, "write", False)
    if not has_write_method:
        raise AttributeError("Passed output stream does not have write method.")

    if not callable(out.write):
        raise AttributeError("Passed output stream does not have write method.")

    _output_stream = out


def reset_style():
    """Resets the active output stream style"""
    _output_stream.write("\033[0m")


def set_decoration(bold: bool = False, underline: bool = False, inverted: bool = False):
    """
    Sets the text decoration of the active output stream

    Parameters
    ----------
    bold: bool
        Sets the text to bold

    underline: bool
        Underlines the text

    inverted: bool
        Inverts the text's color
    """

    decoration = ""
    if bold:
        decoration += "\033[1m"
    if underline:
        decoration += "\033[4m"
    if inverted:
        decoration += "\033[7m"
    _output_stream.write(decoration)


def cprint(
    msg: Any = "",
    *args,
    fcolor: int = 255,
    bcolor: int = 0,
    bold: bool = False,
    underline: bool = False,
    inverted: bool = False,
    reset: bool = True,
):
    """
    Prints to the output stream using the specified colors.

    Parameters
    ----------
    msg: Any
        Object that will be printed to the output stream. 
        `__str__` must be defined

    *args: Any
        Message arguments

    fcolor: int
        Font color (0-255)
    
    bcolor: int
        Background color (0-255)

    bold: bool
        Sets the text to bold

    underline: bool
        Underlines the text

    inverted: bool
        Inverts the texts color
    """

    # Set the text decoration if any style flag was set to true
    if any((bold, underline, inverted)):
        set_decoration(bold, underline, inverted)

    # Add the color codes to the text
    formated_msg = f"\033[38;5;{fcolor}m"
    if bcolor:
        formated_msg += f"\033[48;5;{bcolor}m"

    # Add the message and arguments to the text
    formated_msg += str(msg)
    for arg in args:
        formated_msg += str(arg)

    # If reset flag is set, remove all styling
    if reset:
        formated_msg += "\033[0m"

    _output_stream.write(formated_msg + "\n")
