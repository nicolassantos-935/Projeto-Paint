from controlador.comandos.comando import Comando

class ComandoAlterarCorInterna(Comando):

    def __init__(self, figura, nova_cor):

        self.figura = figura

        # Guarda a cor interna anterior
        self.cor_antiga = figura.cor_interna

        # Guarda a nova cor escolhida
        self.nova_cor = nova_cor

    def executar(self):
        self.figura.cor_interna = self.nova_cor

    def desfazer(self):
        self.figura.cor_interna = self.cor_antiga