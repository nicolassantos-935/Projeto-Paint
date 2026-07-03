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

    def desenhar(self, canvas):
        # Limpa o canvas para evitar desenhos duplicados.
        canvas.delete("all")

        # Redesenha todas as figuras armazenadas.
        for figura in self._figuras:
            figura.desenhar(canvas)

    def listar(self):
        # Retorna a lista de figuras armazenadas.
        return self._figuras
