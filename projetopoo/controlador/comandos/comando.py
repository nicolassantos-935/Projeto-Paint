from abc import ABC, abstractmethod

class Comando(ABC):
    """
    Classe base para todos os comandos da aplicação.
    """

    @abstractmethod
    def executar(self):
        # Executa a ação do comando.
        pass

    @abstractmethod
    def desfazer(self):
        # Desfaz a ação executada pelo comando.
        pass