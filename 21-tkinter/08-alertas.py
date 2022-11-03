from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("ALERTA!!!", "Esta es una alerta desde Python") #tambien hay otros métodos como showwarning(), showerror(), etc.

Button(ventana, text="Mostrar Alerta!!!", command=sacarAlerta). pack()

def salir():
    resultado = MessageBox.askquestion("Salir", "¿Continuar?") 

    if resultado != "yes":
        ventana.destroy()

Button(ventana, text="Salir", command=salir). pack()

ventana.mainloop()