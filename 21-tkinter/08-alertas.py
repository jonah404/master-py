from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("ALERTA!!!", "Esta es una alerta desde Python") #tambien hay otros métodos como showwarning(), showerror(), etc.

Button(ventana, text="Mostrar Alerta!!!", command=sacarAlerta). pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Continuar?") 

    if resultado != "yes":
        MessageBox.showinfo("Adios!", f"gracias por usar el sistema {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Jonatan")). pack()

ventana.mainloop()