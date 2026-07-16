from abc import ABC, abstractmethod

class Operacao(ABC):

    @abstractmethod
    def arrastar(self, controlador, event):
        pass

    @abstractmethod
    def soltar(self, controlador, event):
        pass