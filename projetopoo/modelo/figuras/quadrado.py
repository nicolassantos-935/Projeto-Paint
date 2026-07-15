from modelo.figuras.figura import Figura
from dataclasses import dataclass
from modelo.formulas import Formulas

@dataclass
class Quadrado(Figura):
    
    '''
    Esta classe permite a criacao de figuras quadrado a partir dos metodos da classe figura
    sendo assim possivel desenhar quadrados no canvas, atualizar suas coordenadas durante a criaçao
    e saber se a figura está imcompleta ou nao, alem disso, possui o metado lado para para calcular lagura e altura, 
    atributos essenciais para a criacao de quadrados,o metodo direcao para saber a direção do quadrado, 
    se é para cima ou para baixo, esquerda ou direita e o metodo lados_iguais que utiliza dos dois para
    calcular os pontos do quadrado e desenha-lo corretamente
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
        return Formulas.direcao(self.x1, self.y1, self.x2, self.y2)
    
    def lados_iguais(self):
        
        dirx,diry = self.direcao()
        lado = self.lado()
        lados_esq,lados_dir = (self.x1, self.y1),(self.x1 + lado * dirx, self.y1 + lado * diry)
        lados_iguais = (lados_esq, lados_dir)
        
        return lados_iguais

    def incompleta(self):
        
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return (self.x1, self.y1) == (self.x2, self.y2) or largura <= 1 or altura <= 1 
    
    def contem(self, x, y):

        return Formulas.ponto_no_retangulo(
            x,
            y,
            *self.lados_iguais()
        )