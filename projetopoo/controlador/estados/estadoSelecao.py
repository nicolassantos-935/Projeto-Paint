from controlador.estados.estadoFiguras import EstadoFiguras
from controlador.comandos.ComandoMoverFigura import ComandoMoverFigura
from controlador.comandos.ComandoRedimensionarFigura import ComandoRedimensionarFigura


class EstadoSelecao(EstadoFiguras):
    """
    Estado responsável por selecionar, mover e
    redimensionar figuras.
    """

    def clicar(self, controlador, event):
        """
        Seleciona a figura clicada e define qual
        operação será realizada.
        """

        controlador.figura_selecionada = (
            controlador.desenho.selecionar(
                event.x,
                event.y
            )
        )

        if controlador.figura_selecionada is None:

            controlador.desenhar()
            return

        controlador.estado_inicial = (
            controlador.figura_selecionada.obter_estado()
        )

        controlador.mouse_x = event.x
        controlador.mouse_y = event.y

        controlador.redimensionando = (
            controlador.figura_selecionada.no_canto(
                event.x,
                event.y
            )
        )

        controlador.visual.atualizar_cores(
            controlador.figura_selecionada.cor_linha,
            controlador.figura_selecionada.cor_interna
        )

        controlador.desenhar()

    def arrastar(self, controlador, event):
        """
        Move ou redimensiona a figura selecionada.
        """

        if controlador.figura_selecionada is None:
            return

        if controlador.redimensionando:

            controlador.figura_selecionada.atualizar(
                event.x,
                event.y
            )

        else:

            dx = event.x - controlador.mouse_x
            dy = event.y - controlador.mouse_y

            controlador.figura_selecionada.mover(
                dx,
                dy
            )

            controlador.mouse_x = event.x
            controlador.mouse_y = event.y

        controlador.desenhar()

    def soltar(self, controlador, event):
        """
        Registra a operação realizada para permitir
        desfazer posteriormente.
        """

        if controlador.figura_selecionada is None:
            return

        estado_final = (
            controlador.figura_selecionada.obter_estado()
        )

        if controlador.redimensionando:

            comando = ComandoRedimensionarFigura(
                controlador.figura_selecionada,
                controlador.estado_inicial,
                estado_final
            )

        else:

            comando = ComandoMoverFigura(
                controlador.figura_selecionada,
                controlador.estado_inicial,
                estado_final
            )

        controlador.executar_comando(comando)

    def clicar_direito(self, controlador, event):

        controlador.figura_selecionada = (
            controlador.desenho.selecionar(
                event.x,
                event.y
            )
        )

        if controlador.figura_selecionada is None:
            return

        controlador.estado_inicial = (
            controlador.figura_selecionada.obter_estado()
        )

    def arrastar_direito(self, controlador, event):

        if controlador.figura_selecionada is None:
            return

        controlador.figura_selecionada.atualizar(
            event.x,
            event.y
        )

        controlador.desenhar()

    def soltar_direito(self, controlador, event):

        if controlador.figura_selecionada is None:
            return

        comando = ComandoRedimensionarFigura(
            controlador.figura_selecionada,
            controlador.estado_inicial,
            controlador.figura_selecionada.obter_estado()
        )

        controlador.executar_comando(comando)