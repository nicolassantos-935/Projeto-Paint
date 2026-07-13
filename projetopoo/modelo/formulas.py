from math import *
from math import pi,cos,sin

class Formulas():

    '''
    Esta classe contem formulas matematicas utilizadas para calcular figuras geometricas
    como exemplo o metodo raio que calcula o raio de um circulo a partir de dois pontos e
    o metodo vertices que calcula os vertices de um poligono regular a partir do centro e do raio
    '''


    def __init__(self):
        pass
    
    @staticmethod
    def raio(x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @staticmethod
    def direcao(x1, y1, x2, y2):
        dirx = 1 if x2 >= x1 else -1
        diry = 1 if y2 >= y1 else -1

        return dirx, diry
    
    @staticmethod
    def vertices(x1, y1, x2, y2, quantia_lados):
        
        dirx,diry = Formulas.direcao(x1, y1, x2, y2)
        #raio = Formulas.raio(x1, y1, x2, y2)
        raio_x = abs(x2 - x1)  
        raio_y = abs(y2 - y1)  
        
        vertices = []
        
        for i in range(quantia_lados):
            angulo = 2 * pi * i / quantia_lados - pi / 2
            x = x1 + raio_x * cos(angulo) * dirx
            y = y1 + raio_y * sin(angulo) * diry
            
            vertices.append((x, y))
        
        return vertices
    
