from modelo.figuras.figura import Figura
from dataclasses import dataclass
from modelo.formulas import Formulas

@dataclass

class Pentagono(Figura):
    '''
    Esta classe permite a criacao de figuras pentagono a partir dos metodos da classe figura
    sendo assim possivel desenhar pentagonos no canvas, atualizar suas coordenadas durante a criaçao
    e saber se a figura está imcompleta ou nao, alem disso, possui o metado vertices para para calcular
    os vertices do pentagono, atributos essenciais para a criacao de pentagonos e o metodo direcao para saber a direção do pentagono, 
    se é para cima ou para baixo, esquerda ou direita
    '''

    x1:int
    y1:int
    x2:int
    y2:int

    def atualizar(self,x,y):
        self.x2 = x
        self.y2 = y

    def vertices(self):
     
        return Formulas.vertices(self.x1, self.y1, self.x2, self.y2,5)
    
    def direcao(self):
        return Formulas.direcao(self.x1, self.y1, self.x2, self.y2)

    def incompleta(self):
        
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return (self.x1, self.y1) == (self.x2, self.y2) or largura <= 1 or altura <= 1 
    
    def contem(self, x, y):

        return Formulas.ponto_no_poligono(
            x,
            y,
            self.vertices()
        )