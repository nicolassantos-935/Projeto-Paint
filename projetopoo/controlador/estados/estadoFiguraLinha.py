from controlador.estados.estadoFiguras import EstadoFiguras
from modelo.figuras.linha import Linha

class EstadoFiguraLinha(EstadoFiguras):

    # Estado responsável pela criação de Linhas.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Linha(
            cor_linha,
            "",
            x,
            y,
            x,
            y
        )