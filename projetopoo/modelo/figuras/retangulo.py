from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas


@dataclass
class Retangulo(Figura):
    """
    Representa uma figura do tipo retângulo.

    Armazena dois vértices opostos do retângulo, permitindo
    atualizar seu tamanho, verificar se está completo,
    testar se um ponto pertence à figura e definir o ponto
    utilizado para redimensionamento.
    """

    # Coordenadas dos vértices opostos do retângulo.
    x1: int
    y1: int
    x2: int
    y2: int

    def atualizar(self, x, y):
        """
        Atualiza o segundo vértice do retângulo.
        """

        self.x2 = x
        self.y2 = y

    def lados(self):
        """
        Retorna os dois vértices opostos do retângulo.
        """

        return (
            (self.x1, self.y1),
            (self.x2, self.y2)
        )

    def incompleta(self):
        """
        Verifica se o retângulo possui tamanho suficiente
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
        Verifica se um ponto pertence ao interior do retângulo.
        """

        return Formulas.ponto_no_retangulo(
            x,
            y,
            *self.lados()
        )

    def ponto_redimensionamento(self):
        """
        Retorna o canto utilizado para redimensionar
        o retângulo.
        """

        return (
            self.x2,
            self.y2
        )