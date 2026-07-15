from controlador.estados.estadoFiguras import EstadoFiguras

class EstadoSelecao(EstadoFiguras):

    def clicar(self, controlador, event):

        controlador.figura_selecionada = (
            controlador.desenho.selecionar(
                event.x,
                event.y
            )
        )

        controlador.desenhar()

    def arrastar(self, controlador, event):
        pass

    def soltar(self, controlador, event):
        pass