from paintapp import PaintApp

# Função que irá executar todo o código
def main():
    app = PaintApp()
    app.executar()

# Parte final da modularização, que checa o nome do arquivo e, caso receba True, executa a função main
if __name__ == "__main__":
    main()