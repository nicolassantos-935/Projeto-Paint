import pickle


class Desenho:
    """
    Representa o modelo do desenho.

    É responsável por armazenar e gerenciar todas as figuras
    criadas pelo usuário, oferecendo operações de manipulação
    e persistência dos dados.
    """

    def __init__(self):
        # Lista que armazena as figuras do desenho.
        self._figuras = []

    def adicionar(self, figura):
        """
        Adiciona uma figura ao desenho.
        """
        self._figuras.append(figura)

    def remover(self, figura):
        """
        Remove uma figura do desenho.
        """
        if figura in self._figuras:
            self._figuras.remove(figura)

    def limpar(self):
        """
        Remove todas as figuras do desenho.
        """
        self._figuras.clear()

    def listar(self):
        """
        Retorna uma cópia da lista de figuras.
        """

        return self._figuras.copy()

    def selecionar(self, x, y):
        """
        Retorna a figura localizada na posição informada.

        A busca é realizada de trás para frente, pois a última
        figura desenhada é a que aparece sobre as demais.
        """

        for figura in reversed(self._figuras):

            if figura.contem(x, y):
                return figura

        return None

    def salvar(self, caminho):
        """
        Salva o desenho em um arquivo.
        """

        with open(caminho, "wb") as arquivo:
            pickle.dump(self._figuras, arquivo)

    def abrir(self, caminho):
        """
        Carrega um desenho salvo anteriormente.
        """

        with open(caminho, "rb") as arquivo:
            self._figuras = pickle.load(arquivo)