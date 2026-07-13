from controlador.estados.estadoFiguras import EstadoFiguras
from modelo.figuras.pentagono import Pentagono

class EstadoFiguraPentagono(EstadoFiguras):

    # Estado responsável pela criação de pentágonos.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Pentagono(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )