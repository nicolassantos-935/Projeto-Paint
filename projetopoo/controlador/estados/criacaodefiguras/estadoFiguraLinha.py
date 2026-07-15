from controlador.estados.criacaodefiguras.estadoCriacaoFigura import EstadoCriacaoFigura
from modelo.figuras.linha import Linha

class EstadoFiguraLinha(EstadoCriacaoFigura):

    # Estado responsável pela criação de Linhas.
    def criar_figura(self, x, y, cor_linha, cor_interna):
        return Linha(
            cor_linha,
            "",
            x,
            y,
            x,
            y
        )