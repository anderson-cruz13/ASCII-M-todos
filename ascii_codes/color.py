"""
    Módulo que me traz as cores dos códigos ascii.

    Importações: Typing para tipar o dicionário.

    Dicionário: Dicionário com os valores das cores em código ascii.
"""

from typing import Dict


color_ascii: Dict[str, str] = {
    "white": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "pink": "\033[35m",
    "oceanic": "\033[36m",
    "gray": "\033[37m",
}
