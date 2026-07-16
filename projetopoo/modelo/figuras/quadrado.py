from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas


@dataclass
class Quadrado(Figura):
    """
    Representa uma figura do tipo quadrado.

    O quadrado é definido por um ponto inicial e um segundo
    ponto utilizado para determinar o tamanho da figura.
    Durante a criação, a largura e a altura são ajustadas
    automaticamente para permanecerem iguais.
    """

    # Coordenadas do ponto inicial e do ponto utilizado
    # para calcular o tamanho do quadrado.
    x1: int
    y1: int
    x2: int
    y2: int

    def atualizar(self, x, y):
        """
        Atualiza o segundo ponto do quadrado.
        """

        self.x2 = x
        self.y2 = y

    def lado(self):
        """
        Calcula o comprimento do lado do quadrado.
        """

        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return min(largura, altura)

    def direcao(self):
        """
        Retorna a direção em que o quadrado está sendo
        desenhado.
        """

        return Formulas.direcao(
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )

    def lados_iguais(self):
        """
        Calcula os dois vértices opostos do quadrado,
        garantindo que todos os lados tenham o mesmo
        comprimento.
        """

        dir_x, dir_y = self.direcao()

        lado = self.lado()

        canto_superior = (
            self.x1,
            self.y1
        )

        canto_inferior = (
            self.x1 + lado * dir_x,
            self.y1 + lado * dir_y
        )

        return (
            canto_superior,
            canto_inferior
        )

    def incompleta(self):
        """
        Verifica se o quadrado possui tamanho suficiente
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
        do quadrado.
        """

        return Formulas.ponto_no_retangulo(
            x,
            y,
            *self.lados_iguais()
        )

    def ponto_redimensionamento(self):
        """
        Retorna o canto utilizado para redimensionar
        o quadrado.
        """

        _, canto = self.lados_iguais()

        return canto