from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.hexagono import Hexagono

class EstadoFiguraHexagono(EstadoCriacaoFigura):

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