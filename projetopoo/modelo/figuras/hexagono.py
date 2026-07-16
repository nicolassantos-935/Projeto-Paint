from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas


@dataclass
class Hexagono(Figura):
    """
    Representa uma figura do tipo hexágono.

    O hexágono é definido por dois pontos que delimitam
    a região onde seus seis vértices serão calculados.
    """

    # Coordenadas dos pontos utilizados para construir
    # o hexágono.
    x1: int
    y1: int
    x2: int
    y2: int

    def atualizar(self, x, y):
        """
        Atualiza o segundo ponto do hexágono.
        """

        self.x2 = x
        self.y2 = y

    def vertices(self):
        """
        Calcula os seis vértices do hexágono.
        """

        return Formulas.vertices(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            6
        )

    def direcao(self):
        """
        Retorna a direção em que o hexágono está sendo
        desenhado.
        """

        return Formulas.direcao(
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )

    def incompleta(self):
        """
        Verifica se o hexágono possui tamanho suficiente
        para ser adicionado ao desenho.
        """

        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return (
            (self.x1, self.y1) == (self.x2, self.y2)
            or largura <= 1
            or altura <= 1
        )

    def contem(self, x, y):
        """
        Verifica se um ponto pertence ao interior
        do hexágono.
        """

        return Formulas.ponto_no_poligono(
            x,
            y,
            self.vertices()
        )

    def ponto_redimensionamento(self):
        """
        Retorna o ponto utilizado para redimensionar
        o hexágono.
        """

        return (
            self.x2,
            self.y2
        )