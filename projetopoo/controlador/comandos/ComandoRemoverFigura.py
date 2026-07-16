from controlador.comandos.comando import Comando
from modelo.desenho import Desenho

class ComandoRemoverFigura(Comando):
    """
    Comando responsável por remover uma figura do desenho.
    """

    def __init__(self, desenho: Desenho, figura):
        self.desenho = desenho
        self.figura = figura

    def executar(self):
        self.desenho.remover(self.figura)

    def desfazer(self):
        self.desenho.adicionar(self.figura)