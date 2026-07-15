from modelo.figuras.figura import Figura
from dataclasses import dataclass
from modelo.formulas import *

@dataclass
class Rabisco(Figura):

    # Lista que armazena todos os pontos do rabisco.
    pontos: list

    # Adiciona um novo ponto ao rabisco.
    def atualizar(self, x, y):
        self.pontos.append((x, y))

    # Um rabisco é considerado incompleto quando possui
    # apenas um ponto (ou nenhum segmento de reta).
    def incompleta(self):
        return len(self.pontos) <= 2

    def contem(self, x, y):

        for i in range(len(self.pontos) - 1):

            x1, y1 = self.pontos[i]
            x2, y2 = self.pontos[i + 1]

            if Formulas.distancia_ponto_segmento(
                x, y,
                x1, y1,
                x2, y2
            ) <= 5:
                return True

        return False