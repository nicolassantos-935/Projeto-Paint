from controlador.comandos.comando import Comando

class ComandoRedimensionarFigura(Comando):

    def __init__(self, figura, estado_antigo, estado_novo):

        self.figura = figura

        self.estado_antigo = estado_antigo
        self.estado_novo = estado_novo

    def executar(self):

        self.figura.restaurar_estado(
            self.estado_novo
        )

    def desfazer(self):

        self.figura.restaurar_estado(
            self.estado_antigo
        )