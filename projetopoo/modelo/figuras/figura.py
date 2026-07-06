from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Figura(ABC):
    """
    Classe abstrata que representa uma figura geométrica do Paint.

    Define os atributos e métodos comuns a todas as figuras da aplicação,
    servindo como base para as classes concretas (Linha, Retângulo,
    Círculo, Oval e Rabisco).

    Toda figura deve ser capaz de:
    - ser desenhada no canvas;
    - atualizar suas coordenadas durante a criação;
    - verificar se está incompleta.
    """
    cor_linha: str
    cor_interna: str

    @abstractmethod
    def desenhar(self, canvas, dash = ()): # Método que será usado para desenhar as figuras
        pass

    @abstractmethod
    def atualizar(self, x, y): #Método que será usada para atualizar a posição das figuras
        pass

    @abstractmethod
    def incompleta(self): # Método que checará se a figura realmente é diferente de um único ponto e precisa ser desenhada
        pass