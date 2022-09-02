"""
Una funcion es un conjunto de instrucciones agrupaadas bajo un nombre
concreto que pueden reutilizarse invocando a laa funcion tantas veces 
como sea necesario.

def nombre_funcion(parametros):
    # conjunto de instrucciones

nombre_funcion(parametro)
Se puede llamar a la función las veces que sea necesario.

"""
"""
# Ejemplo 1

# Definir función
def mostrarNombres():
    print("Jona")
    print("Juan")
    print("Paula")
    print("\n")

#Invocar función
mostrarNombres()

# Ejemplo 2: "PARAMETROS"

def muestraNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("y eres mayor de edad.")
    else:
        print("y eres menor de edad.")

nombre = input("Ingresaa tu nombre: ")
edad   = int(input("Ingresa tu edad: "))

muestraNombre(nombre, edad)
"""
# Ejemplo 3

def tabla(num):
    print(f"Tabla de multiplicar del numero: {num}")

    for count in range(11):
        operacion = num * count
        print(f"{num} x {count} = {operacion}")

    print("\n")

tabla(3)
tabla(8)

# Ejemplo 3.1

for ntabla in range(1,11):
    tabla(ntabla)


# Ejemplo 4 : PARAMETROS OPCIONALES

def getEmpleado(nombre, dni = None): #Asignando el valor por defecto al parametro.
    print("Empleado")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Jona", 456785)

#Ejemplo 5: PARAMETROS OPCIONALESS Y RETURN

def saludame(nombre):
    saludo = f"Hola {nombre}."

    return saludo

print(saludame("jona"))

# Ejemplo 6

def calculadora(num1, num2, basicas=False):

    suma  = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div   = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(div)

    return cadena

print(calculadora(5,5, True))


# Ejemplo 7 - FUNCIONES DENTRO DE OTRAS

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Jona", "Alvarez"))

# Ejemplo 8 - FUNCIONES LAMBDA

dimeElAnio = lambda anio: f"El año es {anio}"

print(dimeElAnio(2021))

