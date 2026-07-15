from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.rabisco import Rabisco

class EstadoFiguraRabisco(EstadoCriacaoFigura):

    # Estado responsável pela criação de Rabiscos.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Rabisco(
            cor_linha,
            "",
            [(x, y)]
        )