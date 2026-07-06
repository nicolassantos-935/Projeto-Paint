from tkinter import *
from tkinter import ttk, colorchooser

from fabrica import FabricaFiguras
from desenho import Desenho


class PaintApp:
    """
    Classe principal da aplicação Paint.

    Responsável por criar a interface gráfica, configurar os eventos,
    controlar a criação das figuras e gerenciar a interação do usuário. Ou seja, classe principal, responsável por controlar toda a aplicação Paint.
    """
    def __init__(self): # Inicia a janela, a nomeia, cria um atributo para comportar as figuras, inicia o atributo de figura atual e chama métodos
        self.root = Tk() #criando a janela principal
        self.root.title("Paint 2.0") #nomeando a janela

        self.historico = Desenho() # Todas as figuras desenhadas
        self.figura_atual = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

        self.criar_interface()
        self.configurar_eventos()

    def criar_interface(self): # Cria todos os componentes da interface gráfica.

        paddings = {'padx': 5, 'pady': 5} 

        self.frame = Frame(self.root) #criando um bloco para organizar widgets
        self.frame.pack() # sobe para a janela
        
        # criando variáveis e iniciando valores
        self.tipo_figura = StringVar(value="Linha") 
        self.cor_linha = StringVar(value="black")
        self.cor_interna = StringVar(value="Sem cor")

        # Cria mensagem instrucional
        ttk.Label(
            self.frame,
            text="Selecione a forma, cor interna e cor da linha:"
        ).grid(row=0, column=0, sticky= W, **paddings)

        # Menu de seleção de formas
        self.formas = Frame(self.frame)
        self.formas.grid(row=0, column=1, **paddings)


        self.linha = PhotoImage(file="icones/linha.png")
        ttk.Button(self.formas,
               image=self.linha,
               command= lambda: self.tipo_figura.set("Linha"),
                width=3
               ).grid(row=0, column=0)
        
        self.rabisco = PhotoImage(file="icones/rabisco.png")
        ttk.Button(self.formas,
               image=self.rabisco,
               command= lambda: self.tipo_figura.set("Rabisco"),
                width=3
               ).grid(row=0, column=1)
        
        self.circulo = PhotoImage(file="icones/circulo.png")
        ttk.Button(self.formas,
               image=self.circulo,
               command= lambda: self.tipo_figura.set("Circulo"),
                width=3
               ).grid(row=1, column=1)
        
        self.oval = PhotoImage(file="icones/oval.png")
        ttk.Button(self.formas,
               image=self.oval,
               command= lambda: self.tipo_figura.set("Ovais"),
                width=3
               ).grid(row=1, column=0)
        
        self.retangulo = PhotoImage(file="icones/retangulo.png")
        ttk.Button(self.formas,
               image=self.retangulo,
               command= lambda: self.tipo_figura.set("Retangulo"),
                width=3
               ).grid(row=0, column=3)
        """ttk.OptionMenu(
            self.frame,
            self.tipo_figura,
            "Linha",
            "Linha",
            "Rabisco",
            "Ovais",
            "Retangulo",
            "Circulo"
        ).grid(row=0, column=1, **paddings)"""

        # Menu de seleção de cor de preenchimento
        ttk.OptionMenu(
            self.frame,
            self.cor_interna,
            "Sem cor",
            "Sem cor",
            "white",
            "black",
            "red",
            "blue",
            "green",
            "yellow"
        ).grid(row=0, column=2, **paddings)

        # Menu de seleção de cor externa
        ttk.OptionMenu(
            self.frame,
            self.cor_linha,
            "black",
            "black",
            "white",
            "red",
            "blue",
            "green",
            "yellow"
        ).grid(row=0, column=3, **paddings)
        
        # Botão de escolha de cor personalizada para linha
        ttk.Button(
            self.frame,
            text="Cor linha",
            command=self.escolher_cor_linha
        ).grid(row=1, column=3, **paddings)

        # Botão de escolha de cor personalizada para preenchimento
        ttk.Button(
            self.frame,
            text="Cor interna",
            command=self.escolher_cor_interna
        ).grid(row=1, column=2, **paddings)

        # Botão de desfazer
        ttk.Button(
            self.frame,
            text="Desfazer",
            command=self.desfazer
        ).grid(row=1, column=0, sticky= W, **paddings)

        # Criação do Canvas
        self.canvas = Canvas(
            self.frame,
            bg="white",
            width=1000,
            height=800
        )

        self.canvas.grid(row=2, column=0, columnspan=4)

    def configurar_eventos(self): # Associa os eventos do mouse e teclado aos seus respectivos métodos.

        self.canvas.bind("<ButtonPress-1>", self.iniciar_figura) # CLique do mouse inicia figura

        self.canvas.bind("<B1-Motion>", self.atualizar_figura) # Movimento do mouse, atualiza constantemente a "posição final da figura"

        self.canvas.bind("<ButtonRelease-1>", self.finalizar_figura) # Soltar o botão do mouse, finaliza a figura

        self.root.bind("<Control-z>", self.desfazer) # Comando de desfazer, que apaga a última figura desenhada no momento da chamada, nesse caso, pelo atalho do teclado

    def iniciar_figura(self, event): # Inicia a criação de uma nova figura.
        
        self.figura_atual = FabricaFiguras.criar(
            self.tipo_figura.get(),
            event.x,
            event.y,
            self.cor_linha.get(),
            self.cor_interna.get()
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
            self.historico.adicionar(self.figura_atual)

        self.figura_atual = None

        self.desenhar()

    def desenhar(self): # Redesenha todas as figuras presentes no canvas.

        self.canvas.delete("all")

        for figura in self.historico.listar():
            figura.desenhar(self.canvas)

        if self.figura_atual:
            self.figura_atual.desenhar(
                                self.canvas,
                                dash=(4,2)
                                    )

    def desfazer(self, event=None): # Remove a última figura desenhada.

        self.historico.desfazer()
        self.desenhar()

    def escolher_cor_linha(self): # Permite escolher uma cor personalizada para a linha.

        cor = colorchooser.askcolor()

        if cor[1]:
            self.cor_linha.set(cor[1])

    def escolher_cor_interna(self): # Permite escolher uma cor personalizada para o preenchimento.

        cor = colorchooser.askcolor()

        if cor[1]:
            self.cor_interna.set(cor[1])

    def executar(self): # Inicia o loop principal da aplicação.
        self.root.mainloop()