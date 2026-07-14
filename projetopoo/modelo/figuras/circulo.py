from dataclasses import dataclass
from modelo.figuras.figura import Figura
from modelo.formulas import Formulas
@dataclass
class Circulo(Figura):

    # Centro do círculo
    x1: int
    y1: int

    # Ponto usado para calcular o raio
    x2: int
    y2: int
    
    # Atualiza o segundo ponto utilizado para calcular o raio.
    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y

    # Calcula as porçoes do círculo utilizando o centro e o raio.
    def porcoes(self):
        
        raio = Formulas.raio(self.x1, self.y1, self.x2, self.y2)

        metade1 = (self.x1 - raio, self.y1 - raio)
        metade2 = (self.x1 + raio, self.y1 + raio)
        
        return (metade1, metade2)

    # O círculo é considerado incompleto se o centro
    # coincidir com o segundo ponto.
    def incompleta(self):
        return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2) ** 0.5) <= 3
