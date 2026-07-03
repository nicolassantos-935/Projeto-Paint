from figuras.linha import Linha
from figuras.retangulo import Retangulo
from figuras.circulo import Circulo
from figuras.rabisco import Rabisco
from figuras.oval import Oval

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