from controlador.estados.estadoFiguras import EstadoFiguras
from modelo.figuras.hexagono import Hexagono

class EstadoFiguraHexagono(EstadoFiguras):

    # Estado responsável pela criação de hexágonos.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Hexagono(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )