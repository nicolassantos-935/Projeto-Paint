import pickle

class Desenho:
    """
    Gerencia todas as figuras criadas pelo usuário.

    Armazena as figuras em uma lista e oferece métodos para
    adicionar, desfazer e redesenhar o conteúdo do canvas.
    """

    def __init__(self):
        # Lista que armazena todas as figuras do desenho.
        self._figuras = []

    def adicionar(self, figura):
        # Adiciona uma nova figura ao final da lista.
        self._figuras.append(figura)

    def desfazer(self):
        # Remove a última figura desenhada, caso exista alguma.
        if self._figuras:
            self._figuras.pop()

    def limpar(self):
        # apaga todas as figuras desenhas.
        self._figuras.clear()

    def listar(self):
        # Retorna a lista de figuras armazenadas.
        return self._figuras

    def salvar(self, caminho):
        with open(caminho, "wb") as arquivo:
            pickle.dump(self._figuras, arquivo)

    def abrir(self, caminho):
        with open(caminho, "rb") as arquivo:
            self._figuras = pickle.load(arquivo)