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
    def desenhar_rabisco(canvas, rabisco, dash=()):

        canvas.create_line(
            rabisco.pontos,
            fill=rabisco.cor_linha,
            dash=dash
        )

    @staticmethod
    def desenhar_linha(canvas, linha, dash=()):

        canvas.create_line(
            *linha.pontos(),
            fill=linha.cor_linha,
            dash=dash
        )

    @staticmethod
    def desenhar_retangulo(canvas, retangulo, dash=()):

        fill = "" if retangulo.cor_interna == "Sem cor" else retangulo.cor_interna

        canvas.create_rectangle(
            *retangulo.lados(),
            outline=retangulo.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_oval(canvas, oval, dash=()):

        fill = "" if oval.cor_interna == "Sem cor" else oval.cor_interna

        canvas.create_oval(
            *oval.metades(),
            outline=oval.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_circulo(canvas, circulo, dash=()):

        fill = "" if circulo.cor_interna == "Sem cor" else circulo.cor_interna

        canvas.create_oval(
            *circulo.porcoes(),
            outline=circulo.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_quadrado(canvas, quadrado, dash=()):

        fill = "" if quadrado.cor_interna == "Sem cor" else quadrado.cor_interna

        canvas.create_rectangle(
            *quadrado.lados_iguais(),
            outline=quadrado.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_triangulo(canvas, triangulo, dash=()):

        fill = "" if triangulo.cor_interna == "Sem cor" else triangulo.cor_interna

        canvas.create_polygon(
            *triangulo.vertices(),   # <-- CORRIGIDO
            outline=triangulo.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_pentagono(canvas, pentagono, dash=()):

        fill = "" if pentagono.cor_interna == "Sem cor" else pentagono.cor_interna

        canvas.create_polygon(
            *pentagono.vertices(),
            outline=pentagono.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar_hexagono(canvas, hexagono, dash=()):

        fill = "" if hexagono.cor_interna == "Sem cor" else hexagono.cor_interna

        canvas.create_polygon(
            *hexagono.vertices(),
            outline=hexagono.cor_linha,
            fill=fill,
            dash=dash
        )

    @staticmethod
    def desenhar(canvas, figura, dash=()):

        FormasDesenhar._desenhadores[type(figura)](
            canvas,
            figura,
            dash
        )

FormasDesenhar._desenhadores = {
    Linha: FormasDesenhar.desenhar_linha,
    Rabisco: FormasDesenhar.desenhar_rabisco,
    Retangulo: FormasDesenhar.desenhar_retangulo,
    Oval: FormasDesenhar.desenhar_oval,
    Circulo: FormasDesenhar.desenhar_circulo,
    Quadrado: FormasDesenhar.desenhar_quadrado,
    Triangulo: FormasDesenhar.desenhar_triangulo,
    Pentagono: FormasDesenhar.desenhar_pentagono,
    Hexagono: FormasDesenhar.desenhar_hexagono
}