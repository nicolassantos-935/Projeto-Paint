from abc import ABC, abstractmethod

class EstadoFiguras(ABC):

    @abstractmethod
    def clicar(self, controlador, event):
        pass
    
    @abstractmethod
    def arrastar(self, controlador, event):
        pass

    @abstractmethod
    def soltar(self, controlador, event):
        pass