from figuras.figura import Figura
from dataclasses import dataclass

@dataclass
class Linha(Figura):
    """
    Classe responsável pelo desenho de linhas.

    Contém as coordenadas inicial e final da linha (x1, y1, x2, y2)
    e implementa os métodos necessários para desenhar a figura,
    atualizar suas coordenadas durante o movimento do mouse e
    verificar se a linha está incompleta (quando os dois pontos
    coincidem).
    """
    x1:int
    y1:int
    x2:int
    y2:int

    def desenhar(self, canvas, dash = ()): # Desenha a linha no canvas.
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2,
            dash= dash,
            fill= self.cor_linha
        )

    def atualizar(self, x, y): # Atualiza o ponto final da linha.
        self.x2 = x
        self.y2 = y

    def incompleta(self): # Verifica se a linha possui comprimento zero.
        distancia = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) ** 0.5
        return distancia <= 5