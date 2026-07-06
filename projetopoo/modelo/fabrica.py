from modelo.figuras.linha import Linha
from modelo.figuras.retangulo import Retangulo
from modelo.figuras.circulo import Circulo
from modelo.figuras.rabisco import Rabisco
from modelo.figuras.oval import Oval

class FabricaFiguras:

    @classmethod
    def criar(cls,tipo,x,y,cor_linha,cor_interna):

        if tipo=="Linha":
            return Linha(cor_linha,"",x,y,x,y)

        if tipo=="Retangulo":
            return Retangulo(cor_linha,cor_interna,x,y,x,y)

        if tipo=="Ovais":
            return Oval(cor_linha,cor_interna,x,y,x,y)

        if tipo=="Circulo":
            return Circulo(cor_linha,cor_interna,x,y,x,y)

        return Rabisco(cor_linha,"",[(x,y)])