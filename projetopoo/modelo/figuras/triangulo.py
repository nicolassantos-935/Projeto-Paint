from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas


@dataclass
class Triangulo(Figura):
    """
    Representa uma figura do tipo triângulo.

    O triângulo é definido por dois pontos que delimitam
    um retângulo imaginário. A partir desse retângulo são
    calculados os três vértices do triângulo.
    """

    # Coordenadas dos pontos utilizados para construir
    # o triângulo.
    x1: int
    y1: int
    x2: int
    y2: int

    def atualizar(self, x, y):
        """
        Atualiza o segundo ponto do triângulo.
        """

        self.x2 = x
        self.y2 = y

    def topo(self):
        """
        Calcula o vértice superior do triângulo.
        """

        return (
            (self.x1 + self.x2) // 2,
            self.y1
        )

    def bases(self):
        """
        Calcula os dois vértices da base do triângulo.
        """

        base_esquerda = (
            self.x1,
            self.y2
        )

        base_direita = (
            self.x2,
            self.y2
        )

        return (
            base_esquerda,
            base_direita
        )

    def vertices(self):
        """
        Retorna os três vértices do triângulo.
        """

        topo = self.topo()
        base_esquerda, base_direita = self.bases()

        return (
            topo,
            base_esquerda,
            base_direita
        )

    def incompleta(self):
        """
        Verifica se o triângulo possui tamanho suficiente
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
        do triângulo.
        """

        return Formulas.ponto_no_poligono(
            x,
            y,
            self.vertices()
        )

    def ponto_redimensionamento(self):
        """
        Retorna o ponto utilizado para redimensionar
        o triângulo.
        """

        return (
            self.x2,
            self.y2
        )