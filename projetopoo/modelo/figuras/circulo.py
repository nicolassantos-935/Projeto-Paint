from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas


@dataclass
class Circulo(Figura):
    """
    Representa uma figura do tipo círculo.

    O círculo é definido pelo seu centro e por um segundo
    ponto utilizado para calcular o raio.
    """

    # Centro do círculo.
    x1: int
    y1: int

    # Ponto utilizado para calcular o raio.
    x2: int
    y2: int

    def atualizar(self, x, y):
        """
        Atualiza o ponto utilizado para calcular o raio.
        """

        self.x2 = x
        self.y2 = y

    def raio(self):
        """
        Calcula o raio do círculo.
        """

        return Formulas.raio(
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )

    def porcoes(self):
        """
        Retorna os vértices do retângulo que delimita
        o círculo.
        """

        raio = self.raio()

        canto_superior = (
            self.x1 - raio,
            self.y1 - raio
        )

        canto_inferior = (
            self.x1 + raio,
            self.y1 + raio
        )

        return (
            canto_superior,
            canto_inferior
        )

    def incompleta(self):
        """
        Verifica se o círculo possui raio suficiente
        para ser adicionado ao desenho.
        """

        return self.raio() <= 3

    def contem(self, x, y):
        """
        Verifica se um ponto pertence ao interior
        do círculo.
        """

        raio = self.raio()

        return (
            (x - self.x1) ** 2 +
            (y - self.y1) ** 2
        ) <= raio ** 2

    def ponto_redimensionamento(self):
        """
        Retorna o ponto utilizado para redimensionar
        o círculo.
        """

        return (
            self.x2,
            self.y2
        )