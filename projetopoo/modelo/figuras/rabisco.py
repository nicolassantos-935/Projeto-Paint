from modelo.figuras.figura import Figura
from dataclasses import dataclass

@dataclass
class Rabisco(Figura):

    # Lista que armazena todos os pontos do rabisco.
    pontos: list

    # Desenha o rabisco ligando todos os pontos da lista.
    def desenhar(self, canvas, dash=()):
        canvas.create_line(
            self.pontos,
            fill=self.cor_linha,
            dash=dash
        )

    # Adiciona um novo ponto ao rabisco.
    def atualizar(self, x, y):
        self.pontos.extend([x, y])

    # Um rabisco é considerado incompleto quando possui
    # apenas um ponto (ou nenhum segmento de reta).
    def incompleta(self):
        return len(self.pontos) <= 2
