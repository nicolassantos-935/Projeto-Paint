from visual.paintapp import *
from controlador.controladorPaint import *
from modelo.desenho import *

# Função que irá executar todo o código
def main():
    visao = PaintApp()
    desenho = Desenho()
    controlador = ControladorPaint(desenho, visao)
    visao.executar()

# Parte final da modularização, que checa o nome do arquivo e, caso receba True, executa a função main
if __name__ == "__main__":
    main()