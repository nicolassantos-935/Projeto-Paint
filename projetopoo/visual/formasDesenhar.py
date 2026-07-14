from modelo.figuras.linha import Linha
from modelo.figuras.rabisco import Rabisco
from modelo.figuras.retangulo import Retangulo
from modelo.figuras.oval import Oval
from modelo.figuras.circulo import Circulo
from modelo.figuras.quadrado import Quadrado
from modelo.figuras.triangulo import Triangulo
from modelo.figuras.pentagono import Pentagono
from modelo.figuras.hexagono import Hexagono

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
            oval.metades(),
            outline = oval.cor_linha,
            fill = fill,
            dash = dash
        )

    @staticmethod
    def desenhar_retangulo(canvas, retangulo, dash = ()):
        
        fill = "" if retangulo.cor_interna == "Sem cor" else retangulo.cor_interna

        canvas.create_rectangle(
            retangulo.lados(),
            outline=retangulo.cor_linha,
            fill= fill,
            dash = dash
        )
    
    @staticmethod
    def desenhar_circulo(canvas, circulo, dash = ()):

        # Trata a cor interna "Sem cor"
        fill = "" if circulo.cor_interna == "Sem cor" else circulo.cor_interna
        # Desenha o círculo utilizando o centro e o raio.
        canvas.create_oval(
            Circulo.porcoes(circulo),
            outline=circulo.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_quadrado(canvas, quadrado, dash = ()):

        fill = "" if quadrado.cor_interna == "Sem cor" else quadrado.cor_interna

        #desenha o quadrado utilizando os dados do metodo lados_iguais da classe quadrado
        canvas.create_rectangle(
            quadrado.lados_iguais(),
            outline=quadrado.cor_linha,
            fill= fill,
            dash = dash
        )
    
    @staticmethod
    def desenhar_Triangulo(canvas, triangulo, dash = ()):
        
        fill = "" if triangulo.cor_interna == "Sem cor" else triangulo.cor_interna

        #utiliza dos dados calculados no metodo partes da classe triangulo para desenhar o triangulo
        canvas.create_polygon(
            triangulo.partes(),
            outline=triangulo.cor_linha,
            fill= fill,
            dash = dash
        )
    
    @staticmethod
    def desenhar_pentagono(canvas, pentagono, dash=()):

        fill = "" if pentagono.cor_interna == "Sem cor" else pentagono.cor_interna
        vertices = pentagono.vertices()  #chama o metodo vertices da classe pentagono para encontrar estes dados
        
        #utiliza os vertices calculados como pontos para desenhar o pentagono
        canvas.create_polygon( 
            *vertices,
            outline=pentagono.cor_linha,
            fill=fill,
            dash=dash
        )
    @staticmethod
    def desenhar_hexagono(canvas, hexagono, dash=()):

        fill = "" if hexagono.cor_interna == "Sem cor" else hexagono.cor_interna
        vertices = hexagono.vertices()  #chama o metodo vertices da classe hexagono encontrar estes dados

        #utiliza os vertices calculados como pontos para desenhar o hexagono
        canvas.create_polygon(
            *vertices,
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
        

