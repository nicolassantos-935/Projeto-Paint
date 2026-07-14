from modelo.figuras.figura import Figura
from dataclasses import dataclass

@dataclass

class Oval(Figura):

    ''' 
    Esta classe permite a criacao de figuras no formato oval a partir dos metodos da classe figura
    sendo assim possivel desenhar ovais no canvas, atualizar suas coordenadas(x2,y2) durante a criaçao
    e saber se a figura está imcompleta ou nao, possui tambem o metado metades que retorna os dados necessarios
    para desenhar o oval corretamente
    '''

    x1:int
    y1:int
    x2:int
    y2:int
        
    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y

    def metades(self):
        return (self.x1, self.y1), (self.x2, self.y2)
    
    def incompleta(self):
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return largura <= 5 or altura <= 5