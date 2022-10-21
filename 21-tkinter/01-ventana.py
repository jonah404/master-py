# tkinter es un módulo para crear interfaces gráficas de usuario
from tkinter import *
import os.path # Para comprobar la existencia de archivos

# Crear la ventana raiz
ventana = Tk()

# Titulo de la ventana
ventana.title("Titulo de la ventana")

# Comprobar si existe un archivos
ruta_icono = os.path.abspath('./imagenes/terminal.ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/terminal.ico')

# Icono de la ventana
ventana.iconbitmap(ruta_icono)

# Mostrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()


# Cambiar el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear el tamaño de la ventana
ventana.resizable(0, 0) #los parámetros significan valores horizontal y vertical 0 y 1 (false y true)


# Arrancar y mostrar ventana hasta que se cierre
ventana.mainloop()