# tkinter es un módulo para crear interfaces gráficas de usuario
from tkinter import *
import os.path # Para comprobar la existencia de archivos


class Programa:
    def __init__(self):
        self.title = "Master en Python"
        self.icon = './imagenes/terminal.ico'
        self.icon_alt = './21-tkinter/imagenes/terminal.ico'
        self.size = "770x470"
        self.rezisable = False

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana
        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivos
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()


        # Cambiar el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.rezisable:
            ventana.resizable(1, 1) #los parámetros (0, 0) significan valores horizontal y vertical 0 y 1 (false y true)
        else:
            ventana.resizable(0, 0)


    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#Instanciar el programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola!")
programa.addTexto("Soy un texto.")
programa.mostrar()

