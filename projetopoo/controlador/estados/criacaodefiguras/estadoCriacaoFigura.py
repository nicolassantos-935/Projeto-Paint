from abc import ABC, abstractmethod
from controlador.estados.estadoFiguras import EstadoFiguras
from controlador.comandos.ComandoAdicionarFigura import ComandoAdicionarFigura


class EstadoCriacaoFigura(EstadoFiguras, ABC):

    @abstractmethod
    def criar_figura(self, x, y, cor_linha, cor_interna):
        pass


    def clicar(self, controlador, event):

        controlador.figura_atual = self.criar_figura(
            event.x,
            event.y,
            controlador.visual.cor_linha.get(),
            controlador.visual.cor_interna.get()
        )


    def arrastar(self, controlador, event):

        if controlador.figura_atual is None:
            return

        controlador.figura_atual.atualizar(
            event.x,
            event.y
        )

        controlador.desenhar()


    def soltar(self, controlador, event):

        if controlador.figura_atual is None:
            return

        if not controlador.figura_atual.incompleta():

            controlador.executar_comando(
                ComandoAdicionarFigura(
                    controlador.desenho,
                    controlador.figura_atual
                )
            )

        controlador.figura_atual = None
        controlador.desenhar()