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
        Seleciona a figura clicada e define a operação
        que será realizada sobre ela.
        """

        # Procura uma figura na posição clicada.
        controlador.figura_selecionada = (
            controlador.desenho.selecionar(
                event.x,
                event.y
            )
        )

        # Caso nenhuma figura seja encontrada, remove a seleção e restaura as cores padrão.
        if controlador.figura_selecionada is None:

            controlador.visual.atualizar_cores(
                controlador.cor_linha_padrao,
                controlador.cor_interna_padrao
            )

            controlador.desenhar()
            return

        # Salva o estado inicial da figura para permitir desfazer a operação posteriormente.
        controlador.estado_inicial = (
            controlador.figura_selecionada.obter_estado()
        )

        # Armazena a posição atual do mouse.
        controlador.mouse_x = event.x
        controlador.mouse_y = event.y

        # Verifica se o clique ocorreu sobre o ponto utilizado para redimensionamento.
        controlador.redimensionando = (
            controlador.figura_selecionada.no_canto(
                event.x,
                event.y
            )
        )

        # Atualiza os indicadores de cor da interface com as cores da figura selecionada.
        controlador.visual.atualizar_cores(
            controlador.visual.cor_linha.get(),
            controlador.visual.cor_interna.get()
        )

        controlador.desenhar()

    def arrastar(self, controlador, event):
        """
        Move ou redimensiona a figura selecionada
        enquanto o botão esquerdo do mouse permanece pressionado.
        """

        # Não há nada para mover ou redimensionar.
        if controlador.figura_selecionada is None:
            return

        # Caso a figura não permita movimentação, encerra a operação.
        if (
            not controlador.redimensionando and
            not controlador.figura_selecionada.pode_mover()
        ):
            return

        # Caso a figura não permita redimensionamento,
        # encerra a operação.
        if (
            controlador.redimensionando and
            not controlador.figura_selecionada.pode_redimensionar()
        ):
            return

        # Atualiza o tamanho da figura.
        if controlador.redimensionando:

            controlador.figura_selecionada.atualizar(
                event.x,
                event.y
            )

        else:
            # Calcula o deslocamento do mouse.
            dx = event.x - controlador.mouse_x
            dy = event.y - controlador.mouse_y

            # Move a figura.
            controlador.figura_selecionada.mover(
                dx,
                dy
            )

            # Atualiza a posição atual do mouse.
            controlador.mouse_x = event.x
            controlador.mouse_y = event.y

        controlador.desenhar()

    def soltar(self, controlador, event):
        """
        Finaliza a operação e registra um comando
        para permitir desfazer posteriormente.
        """

        if controlador.figura_selecionada is None:
            return

        # Obtém o estado final da figura.
        estado_final = (
            controlador.figura_selecionada.obter_estado()
        )

        # Cria o comando correspondente à operação realizada.
        if controlador.redimensionando:

            # Caso a figura não permita redimensionamento, não registra comando.
            if not controlador.figura_selecionada.pode_redimensionar():
                return

            comando = ComandoRedimensionarFigura(
                controlador.figura_selecionada,
                controlador.estado_inicial,
                estado_final
            )

        else:
            # Caso a figura não permita movimentação, não registra comando.
            if not controlador.figura_selecionada.pode_mover():
                return

            comando = ComandoMoverFigura(
                controlador.figura_selecionada,
                controlador.estado_inicial,
                estado_final
            )

        controlador.executar_comando(comando)

    def clicar_direito(self, controlador, event):
        """
        Seleciona uma figura para iniciar o
        redimensionamento pelo botão direito.
        """

        controlador.figura_selecionada = (
            controlador.desenho.selecionar(
                event.x,
                event.y
            )
        )

        if controlador.figura_selecionada is None:
            return

        # Salva o estado inicial da figura.
        controlador.estado_inicial = (
            controlador.figura_selecionada.obter_estado()
        )

    def arrastar_direito(self, controlador, event):
        """
        Redimensiona a figura enquanto o botão
        direito permanece pressionado.
        """

        if controlador.figura_selecionada is None:
            return

        # Verifica se a figura permite redimensionamento.
        if not controlador.figura_selecionada.pode_redimensionar():
            return

        controlador.figura_selecionada.atualizar(
            event.x,
            event.y
        )

        controlador.desenhar()

    def soltar_direito(self, controlador, event):
        """
        Finaliza o redimensionamento e registra
        o comando correspondente.
        """

        if controlador.figura_selecionada is None:
            return

        # Caso a figura não permita redimensionamento, encerra a operação.
        if not controlador.figura_selecionada.pode_redimensionar():
            return

        comando = ComandoRedimensionarFigura(
            controlador.figura_selecionada,
            controlador.estado_inicial,
            controlador.figura_selecionada.obter_estado()
        )

        controlador.executar_comando(comando)