from tkinter import *

letra_boton_1: str = 'w'
letra_boton_2: str = 'a'
letra_boton_3: str = 's'
letra_boton_4: str = 'd'

BG_COLOR = "#1e1e2e"
FG_COLOR = "#cdd6f4"
BTN_BG_COLOR = "#11111b"


def set_variables():
    confirmation_pop_up()
    global letra_boton_1
    letra_boton_1 = entry_buton_1.get()
    global letra_boton_2
    letra_boton_2 = entry_buton_2.get()
    global letra_boton_3
    letra_boton_3 = entry_buton_3.get()
    global letra_boton_4
    letra_boton_4 = entry_buton_4.get()


def confirmation_pop_up():
    pop_up = Toplevel(screen)
    pop_up.config(background=BG_COLOR)
    pop_up.title('botones seleccionados')
    pop_up.geometry("200x150")
    message = f"Las letras seleccionadas son:\n" \
              f"Boton 1 - {letra_boton_1}\n" \
              f"Boton 2 - {letra_boton_2}\n" \
              f"Boton 3 - {letra_boton_3}\n" \
              f"Boton 4 - {letra_boton_4}"
    alert = Label(pop_up, text=message)
    alert.config(bg=BG_COLOR, fg=FG_COLOR)
    alert.pack()
    btn = Button(pop_up, text="Ok", command=pop_up.destroy)
    btn.pack()


screen = Tk()
screen.title("selector de botones miados")
screen.config(bg=BG_COLOR)
title_label = Label(text="Bienvenido a nuestro selector de botones miados")
title_label.config(bg=BG_COLOR, fg=FG_COLOR, font=('arial', 12))
title_label.grid(column=0, row=0, columnspan=2, pady=20)

label_button_1 = Label(text=f"boton 1")
label_button_1.grid(column=0, row=1)
label_button_1.config(bg=BG_COLOR, fg=FG_COLOR)
entry_buton_1 = Entry(width=10, justify=CENTER)
entry_buton_1.grid(column=1, row=1)
entry_buton_1.insert(0, letra_boton_1)

label_button_2 = Label(text=f"boton 2")
label_button_2.grid(column=0, row=2)
label_button_2.config(bg=BG_COLOR, fg=FG_COLOR)
entry_buton_2 = Entry(width=10, justify=CENTER)
entry_buton_2.grid(column=1, row=2, pady=20, padx=20)
entry_buton_2.insert(0, letra_boton_2)

label_button_3 = Label(text=f"boton 3")
label_button_3.grid(column=0, row=3)
label_button_3.config(bg=BG_COLOR, fg=FG_COLOR)
entry_buton_3 = Entry(width=10, justify=CENTER)
entry_buton_3.grid(column=1, row=3)
entry_buton_3.insert(0, letra_boton_3)

label_button_4 = Label(text=f"boton 4")
label_button_4.grid(column=0, row=4)
label_button_4.config(bg=BG_COLOR, fg=FG_COLOR)
entry_buton_4 = Entry(width=10, justify=CENTER)
entry_buton_4.grid(column=1, row=4, pady=20, padx=20)
entry_buton_4.insert(0, letra_boton_4)

button_confirmar = Button(text="Confirmar", command=set_variables)
button_confirmar.grid(column=0, row=5, columnspan=2)

screen.mainloop()