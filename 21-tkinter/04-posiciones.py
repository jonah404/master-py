from tkinter import *
from turtle import left, right

ventana = Tk()
#ventana.geometry("500x500")


texto = Label(ventana, text="Bienvenio a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    font=("consolas", 15)
    )
texto.pack(side=TOP)

texto = Label(ventana, text="jonatan.")
texto.config(
    height=4,
    bg="orange",
    font=("Consolas", 10),
    padx = 40,
    pady = 40,
    cursor="heart"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Texto 1")
texto.config(
    height=4,
    bg="gray",
    font=("Consolas", 12),
    padx = 40,
    pady = 40,
    cursor="star"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Texto 2")
texto.config(
    height=4,
    bg="green",
    font=("Consolas", 12),
    padx = 40,
    pady = 40,
    cursor="star"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Texto 3")
texto.config(
    height=4,
    bg="blue",
    font=("Consolas", 12),
    padx = 40,
    pady = 40,
    cursor="star"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Texto 4")
texto.config(
    height=4,
    bg="violet",
    font=("Consolas", 12),
    padx = 40,
    pady = 40,
    cursor="star"
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()