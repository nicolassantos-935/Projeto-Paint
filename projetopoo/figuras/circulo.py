from dataclasses import dataclass
from figuras.figura import Figura

@dataclass
class Circulo(Figura):

    # Centro do círculo
    x1: int
    y1: int

    # Ponto usado para calcular o raio
    x2: int
    y2: int

    # Calcula o raio utilizando a distância entre o centro
    # e o segundo ponto informado.
    @staticmethod
    def calcular_raio(x1, y1, x2, y2):
        return int((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)

    # Desenha o círculo no canvas.
    def desenhar(self, canvas, dash=()):

        # Calcula o raio do círculo.
        raio = Circulo.calcular_raio(
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )
        # Trata a cor interna "Sem cor"
        if self.cor_interna=="Sem cor":
            self.cor_interna = ""
        # Desenha o círculo utilizando o centro e o raio.
        canvas.create_oval(
            self.x1 - raio,
            self.y1 - raio,
            self.x1 + raio,
            self.y1 + raio,
            outline=self.cor_linha,
            fill=self.cor_interna,
            dash=dash
        )

    # Atualiza o segundo ponto utilizado para calcular o raio.
    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y

    # O círculo é considerado incompleto se o centro
    # coincidir com o segundo ponto.
    def incompleta(self):
        return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2) ** 0.5) <= 3
