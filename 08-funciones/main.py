"""
Una funcion es un conjunto de instrucciones agrupaadas bajo un nombre
concreto que pueden reutilizarse invocando a laa funcion tantas veces 
como sea necesario.

def nombre_funcion(parametros):
    # conjunto de instrucciones

nombre_funcion(parametro)
Se puede llamar a la función las veces que sea necesario.

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