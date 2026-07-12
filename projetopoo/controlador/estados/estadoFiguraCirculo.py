from controlador.estados.estadoFiguras import EstadoFiguras
from modelo.figuras.circulo import Circulo

class EstadoFiguraCirculo(EstadoFiguras):

    # Estado responsável pela criação de Círculos.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Circulo(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )