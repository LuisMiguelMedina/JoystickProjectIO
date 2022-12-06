from tkinter import *

#Arreglo inicial
letras_botones = ['w','a','s','d']

#Colores de interfaz
BG_COLOR = "#1e1e2e"
FG_COLOR = "#cdd6f4"
BTN_BG_COLOR = "#11111b"

# Asignamos las variables de los campos al arreglo
def set_variables():
    letras_botones[0] = entry_buton_1.get()
    letras_botones[1] = entry_buton_2.get()
    letras_botones[2] = entry_buton_3.get()
    letras_botones[3] = entry_buton_4.get()
    confirmation_pop_up()

#Enseñamos como fue configurado los botones
def confirmation_pop_up():
    pop_up = Toplevel(screen)
    pop_up.config(background=BG_COLOR)
    pop_up.title('botones seleccionados')
    pop_up.geometry("200x150")
    message = f"Las letras seleccionadas son:\n" \
              f"Boton 1 - {letras_botones[0]}\n" \
              f"Boton 2 - {letras_botones[1]}\n" \
              f"Boton 2 - {letras_botones[2]}\n" \
              f"Boton 2 - {letras_botones[3]}"
    alert = Label(pop_up, text=message)
    alert.config(bg=BG_COLOR, fg=FG_COLOR)
    alert.pack()
    btn = Button(pop_up, text="Ok", command=pop_up.destroy)
    btn.pack()

#Enviamos el arreglo (Para usarlo en el archivo KeyboardController)
def manda_arreglo():
    return letras_botones


#Ventana inicial
screen = Tk()
screen.title("selector de botones miados")
screen.config(bg=BG_COLOR)
title_label = Label(text="Bienvenido a nuestro selector de botones miados")
title_label.config(bg=BG_COLOR, fg=FG_COLOR, font=('arial', 12))
title_label.grid(column=0, row=0, columnspan=2, pady=20)

# Configuracion de la entrada 1
label_button_1 = Label(text=f"boton 1")
label_button_1.grid(column=0, row=1)
label_button_1.config(bg=BG_COLOR, fg=FG_COLOR)

#Campo de escritura de la entrada 1
entry_buton_1 = Entry(width=10, justify=CENTER)
entry_buton_1.grid(column=1, row=1)
entry_buton_1.insert(0, letras_botones[0])



# Configuracion de la entrada 2
label_button_2 = Label(text=f"boton 2")
label_button_2.grid(column=0, row=2)
label_button_2.config(bg=BG_COLOR, fg=FG_COLOR)

#Campo de escritura de la entrada 2
entry_buton_2 = Entry(width=10, justify=CENTER)
entry_buton_2.grid(column=1, row=2, pady=20, padx=20)
entry_buton_2.insert(0, letras_botones[1])



# Configuracion de la entrada 3
label_button_3 = Label(text=f"boton 3")
label_button_3.grid(column=0, row=3)
label_button_3.config(bg=BG_COLOR, fg=FG_COLOR)

#Campo de escritura de la entrada 3
entry_buton_3 = Entry(width=10, justify=CENTER)
entry_buton_3.grid(column=1, row=3)
entry_buton_3.insert(0, letras_botones[2])



# Configuracion de la entrada 4
label_button_4 = Label(text=f"boton 4")
label_button_4.grid(column=0, row=4)
label_button_4.config(bg=BG_COLOR, fg=FG_COLOR)

#Campo de escritura de la entrada 4
entry_buton_4 = Entry(width=10, justify=CENTER)
entry_buton_4.grid(column=1, row=4, pady=20, padx=20)
entry_buton_4.insert(0, letras_botones[3])



#Boton de confirmar la assignacion de teclas
button_confirmar = Button(text="Confirmar", command=set_variables)
button_confirmar.grid(column=0, row=5, columnspan=2)

#Boton de enviar el arreglo donde guarda los datos de las teclas asginadas
button_enviar = Button(text="Chingar el programa", command=manda_arreglo)
button_enviar.grid(column=3, row=5, columnspan=1)

#Se repite el main 
screen.mainloop()
