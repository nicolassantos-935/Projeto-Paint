from controlador.comandos.comando import Comando
from modelo.desenho import Desenho

class ComandoAdicionarFigura(Comando):
    """
    Comando responsável por adicionar uma figura ao desenho.
    """

    def __init__(self, desenho: Desenho, figura):
        self.desenho = desenho
        self.figura = figura

    def executar(self):
        self.desenho.adicionar(self.figura)

    def desfazer(self):
        self.desenho.remover(self.figura)