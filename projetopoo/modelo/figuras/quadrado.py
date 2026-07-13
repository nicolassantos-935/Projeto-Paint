from modelo.figuras.figura import Figura
from dataclasses import dataclass
@dataclass
class Quadrado(Figura):
    
    '''
    Esta classe permite a criacao de figuras quadrado a partir dos metodos da classe figura
    sendo assim possivel desenhar quadrados no canvas, atualizar suas coordenadas durante a criaçao
    e saber se a figura está imcompleta ou nao, alem disso, possui oo metado lado para para calcular lagura e altura, 
    atributos essenciais para a criacao de quadrados e o metodo direcao para saber a direção do quadrado, 
    se é para cima ou para baixo, esquerda ou direita
    '''

    x1:int
    y1:int
    x2:int
    y2:int

    def atualizar(self,x,y):
        self.x2 = x
        self.y2 = y


    def lado(self):
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return min(largura,altura)
    
    def direcao(self):
        dirx = 1 if self.x2 >= self.x1 else -1
        diry = 1 if self.y2 >= self.y1 else -1

        return dirx, diry

    def incompleta(self):
        
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return (self.x1, self.y1) == (self.x2, self.y2) or largura <= 1 or altura <= 1 