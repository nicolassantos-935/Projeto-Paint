from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.quadrado import Quadrado

class EstadoFiguraQuadrado(EstadoCriacaoFigura):

    # Estado responsável pela criação de quadrados.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Quadrado(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )