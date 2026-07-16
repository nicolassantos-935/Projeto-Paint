from controlador.comandos.comando import Comando

class ComandoAlterarCorLinha(Comando):

    def __init__(self, figura, nova_cor):

        self.figura = figura

        # Guarda a cor antiga para o desfazer
        self.cor_antiga = figura.cor_linha

        # Guarda a nova cor escolhida
        self.nova_cor = nova_cor

    def executar(self):
        self.figura.cor_linha = self.nova_cor

    def desfazer(self):
        self.figura.cor_linha = self.cor_antiga