from cgitb import grey
from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master Python")
ventana.geometry("700x400")

marco_padre = Frame(ventana, width=200, height=200)

marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=200, height=200)
marco.config(
    bg="grey",
    bd=5,
    relief=RAISED
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="grey",
    fg="white",
    font=("Arial", 20),
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)

marco = Frame(marco_padre, width=200, height=200)
marco.config(
    bg="green",
    bd=5,
    relief=RAISED
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=200, height=200)

marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=200, height=200)
marco.config(
    bg="blue",
    bd=5,
    relief=RAISED
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=200, height=200)
marco.config(
    bg="orange",
    bd=5,
    relief=RAISED
)
marco.pack(side=RIGHT)

ventana.mainloop()