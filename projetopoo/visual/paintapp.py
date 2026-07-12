from tkinter import *
from tkinter import ttk



class PaintApp:
    """
    Classe principal da aplicação Paint.

    Responsável por criar a interface gráfica, configurar os eventos,
    controlar a criação das figuras e gerenciar a interação do usuário. Ou seja, classe principal, responsável por controlar toda a aplicação Paint.
    """
    def __init__(self): # Inicia a janela, a nomeia, cria um atributo para comportar as figuras, inicia o atributo de figura atual e chama métodos
        self.root = Tk() #criando a janela principal
        self.root.title("Paint 2.0") #nomeando a janela


        self.criar_interface()

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
        self.formas.grid(row=0, column=1, padx= 5)

        # Ícone e botão para selecionar a ferramenta Linha.
        self.linha = PhotoImage(file="projetopoo/visual/icones/linha.png")
        self.btn_linha = ttk.Button(
            self.formas,
            image=self.linha,
            width=3
        )
        self.btn_linha.grid(row=0, column=0)
        
        # Ícone e botão para selecionar a ferramenta Rabisco.
        self.rabisco = PhotoImage(file="projetopoo/visual/icones/rabisco.png")
        self.btn_rabisco = ttk.Button(
            self.formas,
            image=self.rabisco,
            width=3
        )
        self.btn_rabisco.grid(row=0, column=1)
        
        # Ícone e botão para selecionar a ferramenta Círculo.
        self.circulo = PhotoImage(file="projetopoo/visual/icones/circulo.png")
        self.btn_circulo = ttk.Button(
            self.formas,
            image=self.circulo,
            width=3
        )
        self.btn_circulo.grid(row=1, column=1)
        
        # Ícone e botão para selecionar a ferramenta Oval.
        self.oval = PhotoImage(file="projetopoo/visual/icones/oval.png")
        self.btn_oval = ttk.Button(
            self.formas,
            image=self.oval,
            width=3
        )
        self.btn_oval.grid(row=1, column=0)
        
        # Ícone e botão para selecionar a ferramenta Retângulo.
        self.retangulo = PhotoImage(file="projetopoo/visual/icones/retangulo.png")
        self.btn_retangulo = ttk.Button(
            self.formas,
            image=self.retangulo,
            width=3
        )
        self.btn_retangulo.grid(row=0, column=2)

        # Ícone e botão para selecionar a ferramenta Quadrado.
        self.quadrado = PhotoImage(file="projetopoo/visual/icones/quadrado.png")
        self.btn_quadrado = ttk.Button(
            self.formas,
            image=self.quadrado,
            width=3
        )
        self.btn_quadrado.grid(row=1, column=2)

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
        self.btn_cor_linha = ttk.Button(
            self.frame,
            text="Cor linha",
        )
        self.btn_cor_linha.grid(row=1, column=3, **paddings)

        # Botão de escolha de cor personalizada para preenchimento
        self.btn_cor_interna = ttk.Button(
            self.frame,
            text="Cor interna",
        )
        self.btn_cor_interna.grid(row=1, column=2, **paddings)

        # Botão de desfazer
        self.btn_desfazer =ttk.Button(
            self.frame,
            text="Desfazer",
        )
        self.btn_desfazer.grid(row=1, column=0, sticky= W, **paddings)

        # Criação do Canvas
        self.canvas = Canvas(
            self.frame,
            bg="white",
            width=1000,
            height=800
        )

        self.canvas.grid(row=2, column=0, columnspan=4)

    def executar(self): # Inicia o loop principal da aplicação.
        self.root.mainloop()