from modelo.figuras.linha import Linha
from modelo.figuras.rabisco import Rabisco
from modelo.figuras.retangulo import Retangulo
from modelo.figuras.oval import Oval
from modelo.figuras.circulo import Circulo
from modelo.figuras.quadrado import Quadrado
from modelo.figuras.triangulo import Triangulo
from modelo.figuras.pentagono import Pentagono
from modelo.figuras.hexagono import Hexagono
from modelo.formulas import Formulas

    

class FormasDesenhar:

    _desenhadores = {}

    @staticmethod
    def desenhar_rabisco(canvas, rabisco, dash = ()):
    
        canvas.create_line(
            rabisco.pontos,
            fill=rabisco.cor_linha,
            dash = dash
        )

    @staticmethod
    def desenhar_linha(canvas, linha, dash = ()):

        canvas.create_line(
            (linha.x1,linha.y1),
            (linha.x2,linha.y2),
            fill = linha.cor_linha,
            dash = dash
        )
    
    @staticmethod
    def desenhar_oval(canvas, oval, dash = ()):

        fill = "" if oval.cor_interna == "Sem cor" else oval.cor_interna
    
        canvas.create_oval(
            (oval.x1,oval.y1),
            (oval.x2,oval.y2),
            outline = oval.cor_linha,
            fill = fill,
            dash = dash
        )

    @staticmethod
    def desenhar_retangulo(canvas, retangulo, dash = ()):
        
        fill = "" if retangulo.cor_interna == "Sem cor" else retangulo.cor_interna

        canvas.create_rectangle(
            (retangulo.x1, retangulo.y1),
            (retangulo.x2, retangulo.y2),
            outline=retangulo.cor_linha,
            fill= fill,
            dash = dash
        )
    
    @staticmethod
    def desenhar_circulo(canvas, circulo, dash = ()):

        raio = Formulas.raio(circulo.x1, circulo.y1, circulo.x2, circulo.y2)

        # Trata a cor interna "Sem cor"
        fill = "" if circulo.cor_interna == "Sem cor" else circulo.cor_interna
        # Desenha o círculo utilizando o centro e o raio.
        canvas.create_oval(
            (circulo.x1 - raio,circulo.y1 - raio),
            (circulo.x1 + raio,circulo.y1 + raio),
            outline=circulo.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_quadrado(canvas, quadrado, dash = ()):
        
        #possibilita fazer quadrados para ambas direçõoes
        dirx = quadrado.direcao()[0]
        diry = quadrado.direcao()[1]
        lado = quadrado.lado()

        fill = "" if quadrado.cor_interna == "Sem cor" else quadrado.cor_interna

        #desenha o quadrado utilizando o lado e a direção para garantir um uso suave e
        #quadrados perfeitos
        canvas.create_rectangle(
            (quadrado.x1, quadrado.y1),
            (quadrado.x1 + lado * dirx, quadrado.y1 + lado * diry),
            outline=quadrado.cor_linha,
            fill= fill,
            dash = dash
        )
    
    @staticmethod
    def desenhar_Triangulo(canvas, triangulo, dash = ()):
        
        #calcula todas as porçoes do triangulo para desenha-lo corretamente
        topo_x, topo_y = triangulo.topos()
        base_esq_x, base_esq_y = triangulo.bases()[0]
        base_dir_x, base_dir_y = triangulo.bases()[1]

        fill = "" if triangulo.cor_interna == "Sem cor" else triangulo.cor_interna

        #utiliza dos dados calculados anteriormente para desenhar o triangulo 
        canvas.create_polygon(
            (topo_x, topo_y), 
            (base_esq_x, base_esq_y), 
            (base_dir_x, base_dir_y),
            outline=triangulo.cor_linha,
            fill= fill,
            dash = dash
        )
    
    @staticmethod
    def desenhar_pentagono(canvas, pentagono, dash=()):

        fill = "" if pentagono.cor_interna == "Sem cor" else pentagono.cor_interna
        vertices = pentagono.vertices()  

        canvas.create_polygon(
            vertices[0],
            vertices[1],
            vertices[2],
            vertices[3],
            vertices[4],
            outline=pentagono.cor_linha,
            fill=fill,
            dash=dash
        )
    @staticmethod
    def desenhar_hexagono(canvas, hexagono, dash=()):

        fill = "" if hexagono.cor_interna == "Sem cor" else hexagono.cor_interna
        vertices = hexagono.vertices()  

        canvas.create_polygon(
            vertices[0],
            vertices[1],
            vertices[2],
            vertices[3],
            vertices[4],
            vertices[5],
            outline=hexagono.cor_linha,
            fill=fill,
            dash=dash
        )
    
    @staticmethod
    def desenhar(canvas, figura, dash = ()):

        FormasDesenhar._desenhadores[type(figura)](
            canvas,
            figura,
            dash
        )
        
FormasDesenhar._desenhadores = {
    Linha: FormasDesenhar.desenhar_linha,
    Retangulo: FormasDesenhar.desenhar_retangulo,
    Circulo: FormasDesenhar.desenhar_circulo,
    Oval: FormasDesenhar.desenhar_oval,
    Rabisco: FormasDesenhar.desenhar_rabisco,
    Quadrado: FormasDesenhar.desenhar_quadrado,
    Triangulo: FormasDesenhar.desenhar_Triangulo,
    Pentagono: FormasDesenhar.desenhar_pentagono,
    Hexagono: FormasDesenhar.desenhar_hexagono
   }
        

