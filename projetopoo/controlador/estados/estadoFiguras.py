from abc import ABC, abstractmethod

class EstadoFiguras(ABC):

    @abstractmethod
    def criar_figura(self, x, y, cor_linha, cor_interna):
        pass