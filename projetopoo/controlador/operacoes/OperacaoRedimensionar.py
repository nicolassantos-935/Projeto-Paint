from controlador.operacoes.Operacao import Operacao
from controlador.comandos.ComandoRedimensionarFigura import ComandoRedimensionarFigura

class OperacaoRedimensionar(Operacao):

    def arrastar(self, controlador, event):

        controlador.figura_selecionada.atualizar(
            event.x,
            event.y
        )

    def soltar(self, controlador, event):

        estado_final = controlador.figura_selecionada.obter_estado()

        controlador.executar_comando(
            ComandoRedimensionarFigura(
                controlador.figura_selecionada,
                controlador.estado_inicial,
                estado_final
            )
        )