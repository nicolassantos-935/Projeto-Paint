from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova

    #raio = ( (event.x - event.x)**2 + (event.y - event.y)**2 ) ** 0.5
    
    
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_linha.get(), "")
    elif tipo_figura_var.get() == 'Ovais': 
        figura_nova = ("oval", (event.x, event.y, event.x, event.y), cor_linha.get(), cor_interna.get())
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_linha.get(), cor_interna.get())
    elif tipo_figura_var.get() == "Circulo":
        figura_nova = ("circulo", (event.x , event.y , event.x , event.y ), cor_linha.get(), cor_interna.get())
    else :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_linha.get(), "") # "" se refere a cor interna, que não existe para rabisco e linha, mas é guardada para manter o mesmo padrão de tupla (figura, valores, cor da linha, cor interna) para todas as figuras


# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "oval":
        figura_nova = ("oval", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "retangulo":
        figura_nova = ("retangulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "circulo":
        
        figura_nova = ("circulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])
    else : # figura_nova[0] == "linha"
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras(): #abriga o valor de todas as figuras desenhadas, usado para mudar o tipo de figura
    canvas.delete("all")
    
    for fig, values, cor_linha, cor_interna in figuras:
        if cor_interna == "Sem cor":
            cor_interna = "" # Para que não haja conflito, já que "" é a cor "Sem cor" no tkinter

        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill = cor_linha)
        elif fig == "oval":
            canvas.create_oval(values[0], values[1], values[2], values[3], fill = cor_interna, outline = cor_linha) 
        elif fig == "retangulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], fill = cor_interna, outline = cor_linha)
        elif fig == "circulo":
            circulo_x1,circulo_y1,circulo_x2,circulo_y2 = values[0],values[1],values[2],values[3]
            raio = ( (circulo_x1 - circulo_x2)**2 + (circulo_y1 - circulo_y2)**2 ) ** 0.5
            
            canvas.create_oval(values[0] - raio, values[1] - raio, values[0] + raio, values[1] + raio, fill = cor_interna, outline = cor_linha) 
        
        else : # fig == "rabisco"
            canvas.create_line(values, fill = cor_linha)

#Desenha a figura que está sendo desenhada, mas ainda não foi incluída em figuras
def desenhar_figura_nova():
    fig, values, cor_linha, cor_interna = figura_nova
  
    if cor_interna == "Sem cor":
        cor_interna = ""

    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill = cor_linha)
    elif fig == "oval":
        canvas.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2), fill = cor_interna, outline = cor_linha)
    elif fig == "retangulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2), fill = cor_interna, outline = cor_linha)
    elif fig == "circulo":
        circulo_x1,circulo_y1,circulo_x2,circulo_y2 = values[0],values[1],values[2],values[3]
        raio = ( (circulo_x1 - circulo_x2)**2 + (circulo_y1 - circulo_y2)**2 ) ** 0.5   # calcula o raio do círculo a partir da distância entre o ponto inicial e o ponto final do mouse 
        canvas.create_oval(values[0] - raio, values[1] - raio, values[0] + raio, values[1] + raio, dash=(4, 2), fill = cor_interna, outline = cor_linha) #faz um circulo ao fazer um oval com distancias iguais entre todos os pontos do circulo e o centro
    else : # fig == "rabisco"
        canvas.create_line(values, dash=(4, 2), fill = cor_linha)

def incompleta(figura):
    fig, values, *_ = figura # "*_ " é usado para ignorar valores que não serão usados na função
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "oval":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "circulo":
        return (values[0], values[1]) == (values[2], values[3])
    else : # fig == "rabisco"
        return len(values) <= 1
    
def desfazer(event): #Metodo feito para desfazer a ultima figura desenhada utilizando a junção dos atalhos Ctrl + Z 
    global figuras
    if figuras:
        figuras.pop()
        desenhar_figuras()


#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Selecione a forma, a cor interna e a cor da linha:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu_fig = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Ovais', 'Retangulo','Circulo')
option_menu_fig.grid(column=1, row=0, sticky=W, **paddings)

# option menu de cor interna
cor_interna = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu_cor_int = ttk.OptionMenu(frame, cor_interna,
                             "Sem cor", "Sem cor", "white", "black", "red", "blue", "green", "yellow")
option_menu_cor_int.grid(column=2, row=0, sticky=W, **paddings)

# option menu de cor da linha
cor_linha = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu_cor_lin = ttk.OptionMenu(frame, cor_linha,
                             "black", "black", "white", "red", "blue", "green", "yellow",)
option_menu_cor_lin.grid(column=3, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=1920, height=1080)
canvas.grid(column=0, row=1, columnspan=4, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
root.bind('<Control-z>', desfazer)

root.mainloop() 