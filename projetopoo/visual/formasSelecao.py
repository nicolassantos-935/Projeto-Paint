from modelo.figuras.linha import Linha
from modelo.figuras.rabisco import Rabisco
from modelo.figuras.retangulo import Retangulo
from modelo.figuras.oval import Oval
from modelo.figuras.circulo import Circulo
from modelo.figuras.quadrado import Quadrado
from modelo.figuras.triangulo import Triangulo
from modelo.figuras.pentagono import Pentagono
from modelo.figuras.hexagono import Hexagono

class FormasSelecao:

    _desenhadores = {}

    @staticmethod
    def desenhar_rabisco(canvas, rabisco):
    
        canvas.create_line(
            rabisco.pontos,
            fill="red",
            dash = (4, 2),
            width=4
        )

    @staticmethod
    def desenhar_linha(canvas, linha):

        canvas.create_line(
            (linha.x1,linha.y1),
            (linha.x2,linha.y2),
            fill = "red",
            dash = (4, 2),
            width=4
        )
    
    @staticmethod
    def desenhar_oval(canvas, oval):
    
        canvas.create_oval(
            oval.metades(),
            outline = "red",
            fill = "",
            dash = (4, 2),
            width=4
        )

    @staticmethod
    def desenhar_retangulo(canvas, retangulo):

        canvas.create_rectangle(
            retangulo.lados(),
            outline="red",
            fill= "",
            dash = (4, 2),
            width=4
        )
    
    @staticmethod
    def desenhar_circulo(canvas, circulo):

        # Desenha o círculo utilizando o centro e o raio.
        canvas.create_oval(
            Circulo.porcoes(circulo),
            outline="red",
            fill="",
            dash=(4, 2),
            width=4
        )

    @staticmethod
    def desenhar_quadrado(canvas, quadrado):

        #desenha o quadrado utilizando os dados do metodo lados_iguais da classe quadrado
        canvas.create_rectangle(
            quadrado.lados_iguais(),
            outline="red",
            fill= "",
            dash = (4, 2),
            width=4
        )
    
    @staticmethod
    def desenhar_Triangulo(canvas, triangulo):

        #utiliza dos dados calculados no metodo partes da classe triangulo para desenhar o triangulo
        canvas.create_polygon(
            triangulo.vertices(),
            outline="red",
            fill= "",
            dash = (4, 2),
            width=4
        )
    
    @staticmethod
    def desenhar_pentagono(canvas, pentagono):

        vertices = pentagono.vertices()  #chama o metodo vertices da classe pentagono para encontrar estes dados
        
        #utiliza os vertices calculados como pontos para desenhar o pentagono
        canvas.create_polygon( 
            *vertices,
            outline="red",
            fill="",
            dash=(4, 2),
            width=4
        )
    @staticmethod
    def desenhar_hexagono(canvas, hexagono):

        vertices = hexagono.vertices()  #chama o metodo vertices da classe hexagono encontrar estes dados

        #utiliza os vertices calculados como pontos para desenhar o hexagono
        canvas.create_polygon(
            *vertices,
            outline="red",
            fill="",
            dash=(4, 2),
            width=4
        )
    
    @staticmethod
    def desenhar(canvas, figura):

        FormasSelecao._desenhadores[type(figura)](
            canvas,
            figura,
        )
        
FormasSelecao._desenhadores = {
    Linha: FormasSelecao.desenhar_linha,
    Retangulo: FormasSelecao.desenhar_retangulo,
    Circulo: FormasSelecao.desenhar_circulo,
    Oval: FormasSelecao.desenhar_oval,
    Rabisco: FormasSelecao.desenhar_rabisco,
    Quadrado: FormasSelecao.desenhar_quadrado,
    Triangulo: FormasSelecao.desenhar_Triangulo,
    Pentagono: FormasSelecao.desenhar_pentagono,
    Hexagono: FormasSelecao.desenhar_hexagono
   }
        

