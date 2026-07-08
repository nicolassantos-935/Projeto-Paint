from modelo.desenho import *
from modelo.figuras.circulo import *
from modelo.figuras.linha import *
from modelo.figuras.rabisco import *
from modelo.figuras.retangulo import *
from modelo.figuras.oval import *
from visual.paintapp import *
from visual.formasDesenhar import *
from controlador.fabrica import FabricaFiguras
from tkinter import colorchooser

class ControladorPaint:
        
    def __init__(self, desenho: Desenho, visual: PaintApp):
        self.desenho = desenho
        self.visual = visual
        self.figura_atual = None

        self.canvas = self.visual.canvas

        self.visual.btn_desfazer.config(command=self.desfazer)
        self.visual.btn_cor_interna.config(command=self.escolher_cor_interna)
        self.visual.btn_cor_linha.config(command=self.escolher_cor_linha)
            
        self.canvas.bind("<ButtonPress-1>", self.iniciar_figura) # CLique do mouse inicia figura
        self.canvas.bind("<B1-Motion>", self.atualizar_figura) # Movimento do mouse, atualiza constantemente a "posição final da figura"
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_figura) # Soltar o botão do mouse, finaliza a figura
        self.visual.root.bind("<Control-z>", self.desfazer) # Comando de desfazer, que apaga a última figura desenhada no momento da chamada, nesse caso, pelo atalho do teclado

    def iniciar_figura(self, event): # Inicia a criação de uma nova figura.
        
        self.figura_atual = FabricaFiguras.criar(
            self.visual.tipo_figura.get(),
            event.x,
            event.y,
            self.visual.cor_linha.get(),
            self.visual.cor_interna.get(),
        )

    def atualizar_figura(self, event): # Atualiza a figura enquanto o mouse é arrastado.

        if self.figura_atual is None:
            return
        
        self.figura_atual.atualizar(event.x, event.y)

        self.desenhar()

    def finalizar_figura(self, event): # Finaliza a figura e a adiciona ao desenho.

        if self.figura_atual is None:
            return

        if not self.figura_atual.incompleta():
            self.desenho.adicionar(self.figura_atual)

        self.figura_atual = None

        self.desenhar()

    def desenhar(self): # Redesenha todas as figuras presentes no canvas.

        self.canvas.delete("all")

        for figura in self.desenho.listar():
            FormasDesenhar.desenhar(self.canvas, figura)

        if self.figura_atual:
            FormasDesenhar.desenhar(self.canvas, self.figura_atual, (4,2))
                                
            
    def escolher_cor_linha(self): # Permite escolher uma cor personalizada para a linha.

        cor = colorchooser.askcolor()

        if cor[1]:
            self.visual.cor_linha.set(cor[1])

    def escolher_cor_interna(self): # Permite escolher uma cor personalizada para o preenchimento.

        cor = colorchooser.askcolor()

        if cor[1]:
            self.visual.cor_interna.set(cor[1])

    def desfazer(self, event=None): # Remove a última figura desenhada.

        self.desenho.desfazer()
        self.desenhar()


    