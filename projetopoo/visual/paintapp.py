from tkinter import *
from tkinter import ttk, filedialog, colorchooser, messagebox
from visual.formasDesenhar import *
from visual.formasSelecao import *
from visual.botoesEstados import *

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
        self.estados = Frame(self.frame)
        self.estados.grid(row=0, column=1, padx= 5, pady=5)

        # Ícone e botão para selecionar a ferramenta Seleção.
        self.btn_selecao = BotoesEstados.btn_selecao(self.estados)
        self.btn_selecao.grid(row=0, column=2)

        # Ícone e botão para selecionar a ferramenta Linha.
        self.btn_linha = BotoesEstados.btn_linha(self.estados)
        self.btn_linha.grid(row=0, column=0)
        
        # Ícone e botão para selecionar a ferramenta Rabisco.
        self.btn_rabisco = BotoesEstados.btn_rabisco(self.estados)
        self.btn_rabisco.grid(row=0, column=1)
        
        # Ícone e botão para selecionar a ferramenta Círculo.
        self.btn_circulo = BotoesEstados.btn_circulo(self.estados)
        self.btn_circulo.grid(row=1, column=0)
        
        # Ícone e botão para selecionar a ferramenta Oval.
        self.btn_oval = BotoesEstados.btn_oval(self.estados)
        self.btn_oval.grid(row=1, column=1)
        
        # Ícone e botão para selecionar a ferramenta Retângulo.
        self.btn_retangulo = BotoesEstados.btn_retangulo(self.estados)
        self.btn_retangulo.grid(row=2, column=0)

        # Ícone e botão para selecionar a ferramenta Quadrado.
        self.btn_quadrado = BotoesEstados.btn_quadrado(self.estados)
        self.btn_quadrado.grid(row=2, column=1)
        
        # Ícone e botão para selecionar a ferramenta Triângulo.
        self.btn_triangulo = BotoesEstados.btn_triangulo(self.estados)
        self.btn_triangulo.grid(row=1, column=2)
        
        # Ícone e botão para selecionar a ferramenta Pentágono.
        self.btn_pentagono = BotoesEstados.btn_pentagono(self.estados)
        self.btn_pentagono.grid(row=2, column=2)
        
         # Ícone e botão para selecionar a ferramenta Hexagono.
        self.btn_hexagono = BotoesEstados.btn_hexagono(self.estados)
        self.btn_hexagono.grid(row=3, column=0)
        
        # Amostragem de seleção de cor interna
        self.mostra_cor_int = Label(self.frame, bg="black", width=4, height=2, relief="sunken", bd=2)
        self.mostra_cor_int.grid(row=0, column=2, pady=(70, 0))

        # Amostragem de seleção de cor da linha
        self.mostra_cor_lin = Label(self.frame, bg="black", width=4, height=2, relief="sunken", bd=2)
        self.mostra_cor_lin.grid(row=0, column=3, pady=(70, 0))
        
        # Botão de escolha de cor personalizada para linha
        self.btn_cor_linha = ttk.Button(
            self.frame,
            text="Cor linha",
        )
        self.btn_cor_linha.grid(row=0, column=3, **paddings)

        # Botão de escolha de cor personalizada para preenchimento
        self.btn_cor_interna = ttk.Button(
            self.frame,
            text="Cor interna",
        )
        self.btn_cor_interna.grid(row=0, column=2, **paddings)

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

    def redesenhar(self, figuras, figura_atual=None, figura_selecionada=None):
        self.canvas.delete("all")

        for figura in figuras:
            FormasDesenhar.desenhar(self.canvas, figura)

        if figura_atual:
            FormasDesenhar.desenhar(
                self.canvas,
                figura_atual,
                (4,2)
            )
        
        if figura_selecionada:
            FormasSelecao.desenhar(
                self.canvas,
                figura_selecionada
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