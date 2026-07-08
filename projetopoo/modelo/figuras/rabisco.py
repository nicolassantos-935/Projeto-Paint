from modelo.figuras.figura import Figura
from dataclasses import dataclass

@dataclass
class Rabisco(Figura):

    # Lista que armazena todos os pontos do rabisco.
    pontos: list

    # Adiciona um novo ponto ao rabisco.
    def atualizar(self, x, y):
        self.pontos.extend([x, y])

    # Um rabisco é considerado incompleto quando possui
    # apenas um ponto (ou nenhum segmento de reta).
    def incompleta(self):
        return len(self.pontos) <= 2
