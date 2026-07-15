from tkinter import *
from tkinter import ttk
from visual.formasDesenhar import *

class BotoesEstados():

    @staticmethod
    def btn_linha(frame):
        linha = PhotoImage(file="projetopoo/visual/icones/linha.png")
        btn_linha = ttk.Button(
            frame,
            image=linha,
            width=3
        )
        btn_linha.image = linha  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_linha
    
    @staticmethod
    def btn_rabisco(frame):
        rabisco = PhotoImage(file="projetopoo/visual/icones/rabisco.png")
        btn_rabisco = ttk.Button(
            frame,
            image=rabisco,
            width=3
        )
        btn_rabisco.image = rabisco  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_rabisco
    
    @staticmethod
    def btn_circulo(frame):
        circulo = PhotoImage(file="projetopoo/visual/icones/circulo.png")
        btn_circulo = ttk.Button(
            frame,
            image=circulo,
            width=3
        )
        btn_circulo.image = circulo  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_circulo
    
    @staticmethod
    def btn_oval(frame):
        oval = PhotoImage(file="projetopoo/visual/icones/oval.png")
        btn_oval = ttk.Button(
            frame,
            image=oval,
            width=3
        )
        btn_oval.image = oval  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_oval

    @staticmethod
    def btn_retangulo(frame):
        retangulo = PhotoImage(file="projetopoo/visual/icones/retangulo.png")
        btn_retangulo = ttk.Button(
            frame,
            image=retangulo,
            width=3
        )
        btn_retangulo.image = retangulo  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_retangulo    
    
    @staticmethod
    def btn_quadrado(frame):
        quadrado = PhotoImage(file="projetopoo/visual/icones/quadrado.png")
        btn_quadrado = ttk.Button(
            frame,
            image=quadrado,
            width=3
        )
        btn_quadrado.image = quadrado  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_quadrado
    
    @staticmethod
    def btn_triangulo(frame):
        triangulo = PhotoImage(file="projetopoo/visual/icones/triangulo.png")
        btn_triangulo = ttk.Button(
            frame,
            image=triangulo,
            width=3
        )
        btn_triangulo.image = triangulo  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_triangulo
    
    @staticmethod
    def btn_pentagono(frame):   
        pentagono = PhotoImage(file="projetopoo/visual/icones/pentagono.png")
        btn_pentagono = ttk.Button(
            frame,
            image=pentagono,
            width=3
        )
        btn_pentagono.image = pentagono  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_pentagono

    @staticmethod
    def btn_hexagono(frame):   
        hexagono = PhotoImage(file="projetopoo/visual/icones/hexagono.png")
        btn_hexagono = ttk.Button(
            frame,
            image=hexagono,
            width=3
        )
        btn_hexagono.image = hexagono  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_hexagono
    
    @staticmethod
    def btn_selecao(frame):   
        selecao = PhotoImage(file="projetopoo/visual/icones/selecao.png")
        btn_selecao = ttk.Button(
            frame,
            image=selecao,
            width=3
        )
        btn_selecao.image = selecao  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector
        return btn_selecao