from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas


@dataclass
class Rabisco(Figura):
    """
    Representa uma figura do tipo rabisco.

    O rabisco é composto por uma sequência de pontos ligados
    entre si, formando uma linha livre desenhada pelo usuário.
    """

    # Lista de pontos do rabisco.
    pontos: list

    def atualizar(self, x, y):
        """
        Adiciona um novo ponto ao rabisco.
        """

        self.pontos.append((x, y))

    def incompleta(self):
        """
        Verifica se o rabisco possui pontos suficientes
        para ser adicionado ao desenho.
        """

        return len(self.pontos) <= 2

    def contem(self, x, y):
        """
        Verifica se um ponto está próximo de algum segmento
        do rabisco.
        """

        for i in range(len(self.pontos) - 1):

            x1, y1 = self.pontos[i]
            x2, y2 = self.pontos[i + 1]

            if Formulas.distancia_ponto_segmento(
                x,
                y,
                x1,
                y1,
                x2,
                y2
            ) <= 5:

                return True

        return False

    def ponto_redimensionamento(self):
        """
        Rabiscos não possuem ponto específico
        para redimensionamento.
        """

        return None

    def mover(self, dx, dy):
        """
        Move todos os pontos do rabisco.
        """

        novos_pontos = []

        for x, y in self.pontos:

            novos_pontos.append(
                (
                    x + dx,
                    y + dy
                )
            )

        self.pontos = novos_pontos

    def obter_estado(self):
        """
        Retorna uma cópia dos pontos do rabisco.
        """

        return self.pontos.copy()

    def restaurar_estado(self, estado):
        """
        Restaura os pontos do rabisco.
        """

        self.pontos = estado.copy()