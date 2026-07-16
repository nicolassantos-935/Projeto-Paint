from controlador.operacoes.Operacao import Operacao
from controlador.comandos.ComandoMoverFigura import ComandoMoverFigura

class OperacaoMover(Operacao):

    def arrastar(self, controlador, event):

        dx = event.x - controlador.mouse_x
        dy = event.y - controlador.mouse_y

        controlador.figura_selecionada.mover(dx, dy)

        controlador.mouse_x = event.x
        controlador.mouse_y = event.y

    def soltar(self, controlador, event):

        estado_final = controlador.figura_selecionada.obter_estado()

        controlador.executar_comando(
            ComandoMoverFigura(
                controlador.figura_selecionada,
                controlador.estado_inicial,
                estado_final
            )
        )