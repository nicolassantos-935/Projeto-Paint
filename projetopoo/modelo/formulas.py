from math import *
from math import pi,cos,sin

class Formulas():

    '''
    Esta classe contem formulas matematicas utilizadas para calcular figuras geometricas
    como exemplo o metodo raio que calcula o raio de um circulo a partir de dois pontos e
    o metodo vertices que calcula os vertices de um poligono regular a partir do centro, do raio e de trigonometria
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
        raio_x = abs(x2 - x1)  
        raio_y = abs(y2 - y1)  
        
        vertices = []
        
        for i in range(quantia_lados): 
            angulo = 2 * pi * i / quantia_lados - pi / 2
            x = x1 + raio_x * cos(angulo) * dirx
            y = y1 + raio_y * sin(angulo) * diry
            
            vertices.append((x, y))
        
        return vertices
    
    @staticmethod
    def distancia_ponto_segmento(px, py, x1, y1, x2, y2):

        dx = x2 - x1
        dy = y2 - y1

        # segmento degenerado
        if dx == 0 and dy == 0:
            return sqrt((px-x1)**2 + (py-y1)**2)

        # projeção do ponto sobre a reta
        t = (
            (px-x1)*dx +
            (py-y1)*dy
        ) / (dx*dx + dy*dy)

        # limita ao segmento
        t = max(0, min(1, t))

        # ponto mais próximo
        projx = x1 + t*dx
        projy = y1 + t*dy

        return sqrt(
            (px-projx)**2 +
            (py-projy)**2
        )
    
    @staticmethod
    def ponto_no_poligono(x, y, vertices):

        dentro = False

        n = len(vertices)

        j = n - 1

        for i in range(n):

            xi, yi = vertices[i]
            xj, yj = vertices[j]

            if ((yi > y) != (yj > y)):

                intersecao = (
                    (xj - xi) *
                    (y - yi) /
                    (yj - yi)
                ) + xi

                if x < intersecao:
                    dentro = not dentro

            j = i

        return dentro
    
    @staticmethod
    def ponto_no_retangulo(x, y, p1, p2):

        x_min = min(p1[0], p2[0])
        x_max = max(p1[0], p2[0])

        y_min = min(p1[1], p2[1])
        y_max = max(p1[1], p2[1])

        return (
            x_min <= x <= x_max and
            y_min <= y <= y_max
        )