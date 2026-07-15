from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.oval import Oval

class EstadoFiguraOval(EstadoCriacaoFigura):

    # Estado responsável pela criação de Ovais.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Oval(
            cor_linha,
            cor_interna,
            x,
            y,
            x,
            y
        )