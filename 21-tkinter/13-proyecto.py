"""
Crear un programa que tenga:
- (hecho) Ventana
- (hecho) Tamaño fijo 
- (hecho) No redimensionable 
- (hecho) Un Menu (Inicio, Añadir, Información, Salir) 
- (hecho) Opcion de salir 
- (hecho) Diferentes pantallas
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

# Pantallas
# Abrir pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)
    # Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)
    
    # Campos del formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    #Ocultar pantallasa
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    add_label.grid_remove()
    home_label.grid_remove()

    return True

# Variables importantes
name_data = StringVar()
price_data =StringVar()


# Definir campos de pantallas (Inicio)
home_label = Label(ventana, text="Inicio")
# Definir campos de pantallas (add)
add_label = Label(ventana, text="Añadir")

# Campos del formulario
add_name_label = Label(ventana, text="Nombre: ")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio: ")
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text="Descripción: ")
add_description_entry = Text(ventana)

# Definir campos de pantallas (info)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Jonah - 2022" )

# Cargar pantalla inicio
home()

# Crear menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menú
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()


