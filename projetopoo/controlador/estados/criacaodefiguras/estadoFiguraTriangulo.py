from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.triangulo import Triangulo

class EstadoFiguraTriangulo(EstadoCriacaoFigura):

    # Estado responsável pela criação de triangulos.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Triangulo(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )