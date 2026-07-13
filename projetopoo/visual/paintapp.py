from tkinter import *
from tkinter import ttk, filedialog, colorchooser, messagebox
from visual.formasDesenhar import *


class PaintApp:
    """
    Classe principal da aplicação Paint.

    Responsável por criar a interface gráfica, configurar os eventos,
    controlar a criação das figuras e gerenciar a interação do usuário. Ou seja, classe principal, responsável por controlar toda a aplicação Paint.
    """
    def __init__(self): # Inicia a janela, a nomeia, cria um atributo para comportar as figuras, inicia o atributo de figura atual e chama métodos
        self.root = Tk() #criando a janela principal
        self.root.title("Paint 2.0") #nomeando a janela

        self.root.bind("<F11>", self.alternar_tela_cheia)
        self.root.bind("<Escape>", self.sair_tela_cheia)
        
        self.root.attributes("-fullscreen", True)

        self.menu = Menu(self.root, bg="gray")

        # Menu Arquivo
        self.menu_arquivo = Menu(self.menu, tearoff=0)
        self.menu_arquivo.add_command(label="Novo")
        self.menu_arquivo.add_command(label="Abrir")
        self.menu_arquivo.add_command(label="Salvar")
        self.menu_arquivo.add_separator()
        self.menu_arquivo.add_command(label="Sair", command=self.root.quit)

        self.menu.add_cascade(label="Arquivo", menu=self.menu_arquivo)   
        self.root.config(menu=self.menu)


        self.criar_interface()

    def criar_interface(self): # Cria todos os componentes da interface gráfica.

        paddings = {'padx': 5, 'pady': 5} 

        self.frame = Frame(self.root) #criando um bloco para organizar widgets
        self.frame.pack(fill="both", expand=True) # sobe para a janela
        
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
        self.formas.grid(row=0, column=1, padx= 5, pady=5)

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
        
        # Ícone e botão para selecionar a ferramenta Triângulo.
        self.triangulo = PhotoImage(file="projetopoo/visual/icones/triangulo.png")
        self.btn_triangulo = ttk.Button(
            self.formas,
            image=self.triangulo,
            width=3
        )
        self.btn_triangulo.grid(row=0, column=3)
        
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
        )

        self.canvas.grid(row=2, column=0, columnspan=4, sticky="nsew")

        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(0, weight=1)
    
    def alternar_tela_cheia(self, event=None):
        atual = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not atual)
    
    def sair_tela_cheia(self, event=None):
        self.root.attributes("-fullscreen", False)

    def redesenhar(self, figuras, figura_atual=None):
        self.canvas.delete("all")

        for figura in figuras:
            FormasDesenhar.desenhar(self.canvas, figura)

        if figura_atual:
            FormasDesenhar.desenhar(
                self.canvas,
                figura_atual,
                (4,2)
            )

    def pedir_arquivo_abrir(self):
        return filedialog.askopenfilename(
            filetypes=[("Arquivos Pickle", "*.pkl")]
        )

    def pedir_arquivo_salvar(self):
        return filedialog.asksaveasfilename(
            defaultextension=".pkl",
            filetypes=[("Arquivos Pickle", "*.pkl")]
        )

    def escolher_cor(self):
        cor = colorchooser.askcolor()
        return cor[1]
    
    def mostrar_info(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def mostrar_erro(self, titulo, mensagem):
        messagebox.showerror(titulo, mensagem)

    def confirmar_novo(self):
        return messagebox.askyesno(
            "Novo desenho",
            "Deseja apagar o desenho atual?"
        )

    def executar(self): # Inicia o loop principal da aplicação.
        self.root.mainloop()