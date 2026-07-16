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

    #implementação padrão
    def clicar_direito(self, controlador, event):
        pass
    
    def arrastar_direito(self, controlador, event):
        pass

    def soltar_direito(self, controlador, event):
        pass