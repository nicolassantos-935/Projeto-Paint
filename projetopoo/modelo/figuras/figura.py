from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Figura(ABC):
    """
    Classe abstrata que representa uma figura do desenho.

    Todas as figuras possuem cor da linha e cor de preenchimento,
    além de métodos comuns para movimentação, restauração de estado
    e identificação do ponto utilizado para redimensionamento.
    """

    # Cor da borda da figura.
    cor_linha: str

    # Cor do preenchimento da figura.
    cor_interna: str

    @abstractmethod
    def atualizar(self, x, y):
        """
        Atualiza as coordenadas da figura durante sua criação
        ou redimensionamento.
        """
        pass

    @abstractmethod
    def incompleta(self):
        """
        Verifica se a figura possui tamanho suficiente
        para ser adicionada ao desenho.
        """
        pass

    @abstractmethod
    def contem(self, x, y):
        """
        Verifica se um ponto pertence à figura.
        """
        pass

    @abstractmethod
    def ponto_redimensionamento(self):
        """
        Retorna o ponto utilizado para redimensionar a figura.

        Cada figura implementa esse método de acordo com sua geometria.
        """
        pass

    def no_canto(self, x, y):
        """
        Verifica se o clique ocorreu próximo ao ponto
        de redimensionamento.
        """

        ponto = self.ponto_redimensionamento()

        if ponto is None:
            return False

        px, py = ponto

        return (
            abs(x - px) <= 8 and
            abs(y - py) <= 8
        )

    def mover(self, dx, dy):
        """
        Move a figura deslocando todas as suas coordenadas.
        """

        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def obter_estado(self):
        """
        Retorna o estado atual da figura.

        Esse estado é utilizado pelos comandos de mover,
        redimensionar e desfazer.
        """

        return (
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )

    def restaurar_estado(self, estado):
        """
        Restaura um estado salvo anteriormente.
        """

        (
            self.x1,
            self.y1,
            self.x2,
            self.y2
        ) = estado