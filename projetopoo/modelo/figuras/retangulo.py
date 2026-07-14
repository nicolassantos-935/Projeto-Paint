from modelo.figuras.figura import Figura
from dataclasses import dataclass


@dataclass
class Retangulo(Figura):
    
    '''
    Esta classe permite a criacao de figuras retangulo a partir dos metodos da classe figura
    sendo assim possivel desenhar retangulos no canvas, atualizar suas coordenadas durante a criaçao
    e saber se a figura está imcompleta ou nao
    '''

    x1:int
    y1:int
    x2:int
    y2:int

    def atualizar(self,x,y):
        self.x2 = x
        self.y2 = y
    
    def lados(self):
        
        lados_esq = (self.x1, self.y1)
        lados_dir = (self.x2, self.y2)
        
        return (lados_esq, lados_dir)

    def incompleta(self):
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return (self.x1, self.y1) == (self.x2, self.y2) or largura <= 1 or altura <= 1