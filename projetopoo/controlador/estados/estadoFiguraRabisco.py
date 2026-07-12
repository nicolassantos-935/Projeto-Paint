from controlador.estados.estadoFiguras import EstadoFiguras
from modelo.figuras.rabisco import Rabisco

class EstadoFiguraRabisco(EstadoFiguras):

    # Estado responsável pela criação de Rabiscos.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Rabisco(
            cor_linha,
            "",
            [(x, y)]
        )