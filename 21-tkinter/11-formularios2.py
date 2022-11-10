from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("consolas", 20)
)

encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

# Botones check
def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo WEB "

    if movil.get():
        if web.get():
            texto += "y Desarrollo Móvil "
        else:
            texto += "Desarrollo Móvil "
    
    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )

web = IntVar()
movil = IntVar()


Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo WEB",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo Móvil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio Buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tu género?").grid(row=5)

Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)
Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

# Option Menu
def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Opcion 1")

Label(ventana, text="Selecciona una opción").grid(row=5, column=1)

select = OptionMenu(ventana, opcion, "Opción 1", "Opción 2", "Opción 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()