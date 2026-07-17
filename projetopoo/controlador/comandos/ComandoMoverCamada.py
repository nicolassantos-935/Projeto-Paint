from controlador.comandos.comando import Comando

class ComandoMoverCamada(Comando):

    def __init__(self, desenho, figura, indice_final):

        self.desenho = desenho
        self.figura = figura

        self.indice_inicial = desenho.indice_da_figura(figura)
        self.indice_final = indice_final

    def executar(self):

        self.desenho.mover_para_indice(
            self.figura,
            self.indice_final
        )

    def desfazer(self):

        self.desenho.mover_para_indice(
            self.figura,
            self.indice_inicial
        )