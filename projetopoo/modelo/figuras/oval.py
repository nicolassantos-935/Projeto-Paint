from dataclasses import dataclass
from modelo.figuras.figura import Figura


@dataclass
class Oval(Figura):
    """
    Representa uma figura do tipo oval.

    O oval é definido por dois vértices opostos do retângulo
    que delimita a elipse.
    """

    # Coordenadas dos vértices opostos do retângulo.
    x1: int
    y1: int
    x2: int
    y2: int

    def atualizar(self, x, y):
        """
        Atualiza o segundo vértice da figura.
        """

        self.x2 = x
        self.y2 = y

    def metades(self):
        """
        Retorna os vértices do retângulo que delimita
        a elipse.
        """

        return (
            (self.x1, self.y1),
            (self.x2, self.y2)
        )

    def incompleta(self):
        """
        Verifica se o oval possui tamanho suficiente
        para ser adicionado ao desenho.
        """

        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return largura <= 5 or altura <= 5

    def contem(self, x, y):
        """
        Verifica se um ponto pertence ao interior
        da elipse.
        """

        (x1, y1), (x2, y2) = self.metades()

        centro_x = (x1 + x2) / 2
        centro_y = (y1 + y2) / 2

        semi_eixo_x = abs(x2 - x1) / 2
        semi_eixo_y = abs(y2 - y1) / 2

        if semi_eixo_x == 0 or semi_eixo_y == 0:
            return False

        return (
            ((x - centro_x) / semi_eixo_x) ** 2 +
            ((y - centro_y) / semi_eixo_y) ** 2
        ) <= 1

    def ponto_redimensionamento(self):
        """
        Retorna o ponto utilizado para redimensionar
        o oval.
        """

        return (
            self.x2,
            self.y2
        )