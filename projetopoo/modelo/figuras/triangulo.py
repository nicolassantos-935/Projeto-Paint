from modelo.figuras.figura import Figura
from dataclasses import dataclass

@dataclass

class Triangulo(Figura):
    '''
    Esta classe permite a criacao de figuras triangulo a partir dos metodos da classe figura
    sendo assim possivel desenhar triangulos no canvas, atualizar suas coordenadas durante a criaçao
    e saber se a figura está imcompleta ou nao, alem disso, possui os metodos topo e bases para calcular os pontos do triangulo
    e o metodo partes que une os 2 em mesma tupla para organizar os dados e desenha-lo corretamente
    '''

    x1:int
    y1:int
    x2:int
    y2:int

    def atualizar(self,x,y):
        self.x2 = x
        self.y2 = y

    def topos(self):
        topo_x = (self.x1 + self.x2) //2
        topo_y = self.y1
        
        return (topo_x, topo_y)

    def bases(self):
        
        base_esq_x, base_esq_y = self.x1, self.y2
        base_dir_x, base_dir_y = self.x2, self.y2
        
        return (base_esq_x, base_esq_y), (base_dir_x, base_dir_y)

    def partes(self):
        
        partes = (self.topos(), self.bases())
    
        return partes
    
    def incompleta(self):
        
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return (self.x1, self.y1) == (self.x2, self.y2) or largura <= 1 or altura <= 1 

    