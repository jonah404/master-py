"""
Crear un programa que tenga:
- (hecho) Ventana
- (hecho) Tamaño fijo 
- (hecho) No redimensionable 
- (hecho) Un Menu (Inicio, Añadir, Información, Salir) 
- (hecho) Opcion de salir 
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla principal

"""

from tkinter import *

# Definiendo la ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto tkinter - Master Python")
ventana.resizable(0,0)

# Crear menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Información")
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menú
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()


