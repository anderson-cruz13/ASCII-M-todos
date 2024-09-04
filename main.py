"""
Módulo que define as classes para uso de aplicações no método ASCII.

Classes:
    AsciiMeta: Classe abstrata que define os métodos.
    StyleAscii: Classe concreta que aplica os métodos herdados de
        AsciiMeta.

Importações:
    abc: usar o decorador de abstração e a classe abstrata herdar de ABC.
    ASCII_Codes.color: módulo com os codes das cores ascii.
    ASCII_Codes.negative: módulo com o valor unitário da cor.

Executável:
    Quando o módulo é executado diretamente, ele demonstra a funcionalidade
    da classe `StyleAscii` aplicando diferentes estilos de formatação (cor,
    negrito, sublinhado e negativo) ao texto "Anderson" e exibindo o resultado.
"""
from abc import ABC, abstractmethod
from ascii_codes.color import color_ascii
from ascii_codes.negative import color_ascii_negative


class AsciiMeta(ABC):
    """Class abstrata que define os métodos."""
    @abstractmethod
    def color_ascii(self, color: str, text: str) -> None:
        """Retorna o código ASCII de cor especificado."""

    @abstractmethod
    def bold_ascii(self) -> None:
        """Retorna o código ASCII de uma cor especificada em negrito."""

    @abstractmethod
    def underline_ascii(self) -> None:
        """Retorna o código ASCII de uma cor especificada em underline."""

    @abstractmethod
    def negative_ascii(self) -> None:
        """Retorna o código ASCII de uma cor especificada em negativo."""


class StyleAscii(AsciiMeta):
    """Class concreta que usa os métodos."""
    def __init__(self) -> None:
        self.text_formated = ""
        self.color = ""
        self.color_negative = color_ascii_negative.get(
            self.color, color_ascii_negative["white"]
        )

    def color_ascii(self, color: str, text: str) -> None:
        self.color = color_ascii.get(color, color_ascii["white"])
        self.text_formated = f"{self.color}{text}\033[0m"

    def bold_ascii(self) -> None:
        self.text_formated = f"\033[1m{self.text_formated}\033[m"

    def underline_ascii(self) -> None:
        self.text_formated = f"\033[4m{self.text_formated}\033[m"

    def negative_ascii(self) -> None:
        self.text_formated = f"\
\033[7;{self.color_negative};{self.color_negative}m{self.text_formated}\033[m"

    def __str__(self) -> str:
        return self.text_formated


if __name__ == "__main__":
    name = StyleAscii()
    name.color_ascii("red", "Anderson")
    print(name)
    name.bold_ascii()
    print(name)
    name.underline_ascii()
    print(name)
    name.negative_ascii()
    print(name)
