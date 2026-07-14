from modelo.desenho import *
from modelo.figuras.circulo import *
from modelo.figuras.linha import *
from modelo.figuras.rabisco import *
from modelo.figuras.retangulo import *
from modelo.figuras.oval import *
from visual.paintapp import *
from visual.formasDesenhar import *
from tkinter import colorchooser, filedialog
from controlador.estados.estadoFiguraLinha import *
from controlador.estados.estadoFiguraRetangulo import *
from controlador.estados.estadoFiguraCirculo import *
from controlador.estados.estadoFiguraRabisco import *
from controlador.estados.estadoFiguraOval import *
from controlador.estados.estadoFiguraQuadrado import *
from controlador.estados.estadoFiguraTriangulo import *
from controlador.estados.estadoFiguraPentagono import *
from controlador.estados.estadoFiguraHexagono import *
import pickle

class ControladorPaint:
        
    def __init__(self, desenho: Desenho, visual: PaintApp):
        self.desenho = desenho
        self.visual = visual
        self.figura_atual = None
        self.estado = EstadoFiguraLinha()

        self.canvas = self.visual.canvas

        self.visual.btn_desfazer.config(command=self.desfazer)
        self.visual.btn_cor_interna.config(command=self.escolher_cor_interna)
        self.visual.btn_cor_linha.config(command=self.escolher_cor_linha)
            
        self.canvas.bind("<ButtonPress-1>", self.iniciar_figura) # CLique do mouse inicia figura
        self.canvas.bind("<B1-Motion>", self.atualizar_figura) # Movimento do mouse, atualiza constantemente a "posição final da figura"
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_figura) # Soltar o botão do mouse, finaliza a figura
        self.visual.root.bind("<Control-z>", self.desfazer) # Comando de desfazer, que apaga a última figura desenhada no momento da chamada, nesse caso, pelo atalho do teclado
        self.visual.root.bind("<Control-s>", self.salvar) # Comando salvar, que possibilita salvar o canvas atual em um arquivo no dispositivo do usuário.
        self.visual.root.bind("<Control-n>", self.novo) # Comando novo, que possibilita limpar o canvas atual.
        self.visual.root.bind("<Control-o>", self.abrir) # Comando abrir, que possibilita abrir um canvas salvo em um arquivo no dispositivo do usuário.

        # Associa cada botão da interface ao estado correspondente,
        # alterando a ferramenta de desenho selecionada.
        self.visual.btn_linha.config(command = lambda: self.alterar_estado(EstadoFiguraLinha()))
        self.visual.btn_rabisco.config(command = lambda: self.alterar_estado(EstadoFiguraRabisco()))
        self.visual.btn_retangulo.config(command = lambda: self.alterar_estado(EstadoFiguraRetangulo()))
        self.visual.btn_oval.config(command = lambda: self.alterar_estado(EstadoFiguraOval()))
        self.visual.btn_circulo.config(command = lambda: self.alterar_estado(EstadoFiguraCirculo()))
        self.visual.btn_quadrado.config(command = lambda: self.alterar_estado(EstadoFiguraQuadrado()))
        self.visual.btn_triangulo.config(command = lambda: self.alterar_estado(EstadoFiguraTriangulo()))
        self.visual.btn_pentagono.config(command = lambda: self.alterar_estado(EstadoFiguraPentagono()))
        self.visual.btn_hexagono.config(command = lambda: self.alterar_estado(EstadoFiguraHexagono()))
        self.visual.menu_arquivo.entryconfigure(
            "Novo",
            command=self.novo)

        self.visual.menu_arquivo.entryconfigure(
            "Abrir",
            command=self.abrir)

        self.visual.menu_arquivo.entryconfigure(
            "Salvar",
            command=self.salvar)
    
    def iniciar_figura(self, event): # Inicia a criação de uma nova figura.
        
        self.figura_atual = self.estado.criar_figura(
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

    def alterar_estado(self, estado):

        self.estado = estado

    def desenhar(self): # Redesenha todas as figuras presentes no canvas.

        self.visual.redesenhar(
        self.desenho.listar(),
        self.figura_atual
    )
            
    def escolher_cor_linha(self): # Permite escolher uma cor personalizada para a linha.

        cor = self.visual.escolher_cor()

        if cor:
            self.visual.cor_linha.set(cor)
            self.visual.mostra_cor_lin.config(bg=cor)

    def escolher_cor_interna(self): # Permite escolher uma cor personalizada para o preenchimento.

        cor = self.visual.escolher_cor()

        if cor:
            self.visual.cor_interna.set(cor)
            self.visual.mostra_cor_int.config(bg=cor)

    def desfazer(self, event=None): # Remove a última figura desenhada.

        self.desenho.desfazer()
        self.desenhar()

    # Comandos que se referem ao manuseio de arquivos
    def novo(self, event=None):
        if self.visual.confirmar_novo():
        
            self.desenho.limpar()
            self.desenhar()

            self.visual.mostrar_info(
                "Novo",
                "Novo desenho criado."
            )

    def salvar(self, event=None):
        caminho = self.visual.pedir_arquivo_salvar()

        if caminho:
            try:
                self.desenho.salvar(caminho)
                self.visual.mostrar_info(
                    "Salvar",
                    "Arquivo salvo com sucesso!"
                )
            except Exception as e:
                self.visual.mostrar_erro(
                    "Erro",
                    f"Não foi possível salvar o arquivo.\n\n{e}"
                )

    def abrir(self, event=None):
        caminho = self.visual.pedir_arquivo_abrir()

        if caminho:
            try:
                self.desenho.abrir(caminho)
                self.desenhar()

                self.visual.mostrar_info(
                "Abrir",
                "Arquivo carregado com sucesso!"
            )
                
            except Exception as e:
                self.visual.mostrar_erro(
                    "Erro",
                    f"Não foi possível abrir o arquivo.\n\n{e}"
            )
    