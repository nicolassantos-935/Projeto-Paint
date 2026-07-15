from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.circulo import Circulo

class EstadoFiguraCirculo(EstadoCriacaoFigura):

    def criar_figura(self, x, y, cor_linha, cor_interna):

        return Circulo(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )