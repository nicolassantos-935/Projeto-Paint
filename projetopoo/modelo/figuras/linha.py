from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas


@dataclass
class Linha(Figura):
    """
    Representa uma figura do tipo linha.

    Armazena as coordenadas dos pontos inicial e final da linha,
    permitindo atualizar seu tamanho, verificar se está completa,
    testar se um ponto pertence ao segmento e definir o ponto
    utilizado para redimensionamento.
    """

    # Coordenadas dos pontos inicial e final da linha.
    x1: int
    y1: int
    x2: int
    y2: int

    def atualizar(self, x, y):
        """
        Atualiza o ponto final da linha.
        """

        self.x2 = x
        self.y2 = y

    def pontos(self):
        """
        Retorna os pontos inicial e final da linha.
        """

        return (
            (self.x1, self.y1),
            (self.x2, self.y2)
        )

    def incompleta(self):
        """
        Verifica se a linha possui comprimento suficiente
        para ser adicionada ao desenho.
        """

        distancia = (
            (self.x2 - self.x1) ** 2 +
            (self.y2 - self.y1) ** 2
        ) ** 0.5

        return distancia <= 5

    def contem(self, x, y):
        """
        Verifica se um ponto está suficientemente próximo
        do segmento de reta.
        """

        p1, p2 = self.pontos()

        return (
            Formulas.distancia_ponto_segmento(
                x,
                y,
                *p1,
                *p2
            ) <= 5
        )

    def ponto_redimensionamento(self):
        """
        Retorna o ponto utilizado para redimensionar a linha.
        """

        return (
            self.x2,
            self.y2
        )