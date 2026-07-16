from modelo.desenho import *
from modelo.figuras.circulo import *
from modelo.figuras.linha import *
from modelo.figuras.rabisco import *
from modelo.figuras.retangulo import *
from modelo.figuras.oval import *
from visual.paintapp import *
from visual.formasDesenhar import *
from controlador.estados.criacaodefiguras.estadoFiguraLinha import *
from controlador.estados.criacaodefiguras.estadoFiguraRetangulo import *
from controlador.estados.criacaodefiguras.estadoFiguraCirculo import *
from controlador.estados.criacaodefiguras.estadoFiguraRabisco import *
from controlador.estados.criacaodefiguras.estadoFiguraOval import *
from controlador.estados.criacaodefiguras.estadoFiguraQuadrado import *
from controlador.estados.criacaodefiguras.estadoFiguraTriangulo import *
from controlador.estados.criacaodefiguras.estadoFiguraPentagono import *
from controlador.estados.criacaodefiguras.estadoFiguraHexagono import *
from controlador.estados.estadoSelecao import *
from controlador.comandos.ComandoAdicionarFigura import * 
from controlador.comandos.ComandoRemoverFigura import * 
from controlador.comandos.ComandoAlterarCorInterna import * 
from controlador.comandos.ComandoAlterarCorLinha import * 
from controlador.comandos.ComandoRedimensionarFigura import * 
from controlador.comandos.ComandoMoverFigura import * 

class ControladorPaint:
        
    def __init__(self, desenho: Desenho, visual: PaintApp):
        self.desenho = desenho
        self.visual = visual
        self.figura_atual = None
        self.estado = EstadoFiguraLinha()
        self.figura_selecionada = None
        self.historico = []

        self.mouse_x = 0
        self.mouse_y = 0

        self.estado_inicial = None

        self.redimensionando = False

        self.canvas = self.visual.canvas

        self.visual.btn_remover.config(command=self.remover_figura)
        self.visual.btn_cor_interna.config(command=self.escolher_cor_interna)
        self.visual.btn_cor_linha.config(command=self.escolher_cor_linha)
            
        self.canvas.bind("<ButtonPress-1>", self.clicar) # CLique do mouse inicia figura
        self.canvas.bind("<B1-Motion>", self.arrastar) # Movimento do mouse, atualiza constantemente a "posição final da figura"
        self.canvas.bind("<ButtonRelease-1>", self.soltar) # Soltar o botão do mouse, finaliza a figura
        self.canvas.bind("<ButtonPress-3>", self.clicar_direito)
        self.canvas.bind("<B3-Motion>", self.arrastar_direito)
        self.canvas.bind("<ButtonRelease-3>", self.soltar_direito)
        self.visual.root.bind("<Delete>", self.remover_figura) # Comando de deletar, que apaga a figura selecionada
        self.visual.root.bind("<Control-s>", self.salvar) # Comando salvar, que possibilita salvar o canvas atual em um arquivo no dispositivo do usuário.
        self.visual.root.bind("<Control-n>", self.novo) # Comando novo, que possibilita limpar o canvas atual.
        self.visual.root.bind("<Control-o>", self.abrir) # Comando abrir, que possibilita abrir um canvas salvo em um arquivo no dispositivo do usuário.
        self.visual.root.bind("<Control-z>", self.desfazer)

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
        self.visual.btn_selecao.config(command=lambda: self.alterar_estado(EstadoSelecao()))

        self.visual.menu_arquivo.entryconfigure(
            "Novo",
            command=self.novo)

        self.visual.menu_arquivo.entryconfigure(
            "Abrir",
            command=self.abrir)

        self.visual.menu_arquivo.entryconfigure(
            "Salvar",
            command=self.salvar)
    
    def clicar(self, event):
        self.estado.clicar(self, event)

    def arrastar(self, event):
        self.estado.arrastar(self, event)

    def soltar(self, event):
        self.estado.soltar(self, event)

    def clicar_direito(self, event):
        self.estado.clicar_direito(self, event)

    def arrastar_direito(self, event):
        self.estado.arrastar_direito(self, event)

    def soltar_direito(self, event):
        self.estado.soltar_direito(self, event)

    def alterar_estado(self, estado):

        self.estado = estado
        self.figura_selecionada = None
        self.desenhar()
        
    def desenhar(self): # Redesenha todas as figuras presentes no canvas.

        self.visual.redesenhar(
        self.desenho.listar(),
        self.figura_atual,
        self.figura_selecionada
    )
            
    def escolher_cor_linha(self):

        cor = self.visual.escolher_cor()

        if cor is None:
            return

        if self.figura_selecionada:
            comando = ComandoAlterarCorLinha(
                self.figura_selecionada,
                cor
            )

            self.executar_comando(comando)

        else:
            self.visual.cor_linha.set(cor)

        self.visual.mostra_cor_lin.config(bg=cor)

    def escolher_cor_interna(self):

        cor = self.visual.escolher_cor()

        if cor is None:
            return

        if self.figura_selecionada:
            comando = ComandoAlterarCorInterna(
                self.figura_selecionada,
                cor
            )

            self.executar_comando(comando)

        else:
            self.visual.cor_interna.set(cor)
        
        self.visual.mostra_cor_int.config(bg=cor)

    # controlador.Comandos que se referem ao manuseio de arquivos
    def novo(self, event=None):
        if self.visual.confirmar_novo():
        
            self.desenho.limpar()
            self.historico.clear()
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
                self.figura_selecionada = None
                self.figura_atual = None
                self.historico.clear()
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

    def remover_figura(self, event=None):

        if self.figura_selecionada is None:
            return

        figura = self.figura_selecionada

        self.figura_selecionada = None

        comando = ComandoRemoverFigura(
            self.desenho,
            figura
        )

        self.executar_comando(comando)

        self.visual.atualizar_cores(
            "black",
            "white"
        )
        self.figura_selecionada = None

    def executar_comando(self, comando):

        comando.executar()
        self.historico.append(comando)
        self.desenhar()
        
    def desfazer(self, event=None):

        if self.historico:

            comando = self.historico.pop()
            comando.desfazer()
            self.desenhar()