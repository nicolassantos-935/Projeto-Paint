from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.retangulo import Retangulo

class EstadoFiguraRetangulo(EstadoCriacaoFigura):

    # Estado responsável pela criação de Retângulos.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Retangulo(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )