from tkinter import *
from turtle import right

ventana = Tk()
ventana.geometry("500x500")


texto = Label(ventana, text="Bienvenio a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    font=("consolas", 15)
    )
texto.pack()

texto = Label(ventana, text="Mi nombre")
texto.config(
    height=4,
    bg="orange",
    font=("Consolas", 10),
    padx = 40,
    pady = 40,
    cursor="heart"
)
texto.pack(anchor=CENTER)

texto = Label(ventana, text="Master en Python")
texto.config(
    height=4,
    bg="gray",
    font=("Consolas", 12),
    padx = 40,
    pady = 40,
    cursor="star"
)
texto.pack(anchor=CENTER)




ventana.mainloop()