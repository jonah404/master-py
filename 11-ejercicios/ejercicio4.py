"""
Ejercicio4
Crear un script que tenga 4 variables, una lista, un string, un entero y un boolean
y que imprima un msj segun el tipo de dato de cada variable.

"""

def traducir(tipo):
    result = "None"
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Número entero"
    elif tipo == bool:
        result="Booleano"

    return result

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f"Este dato es del tipo {traducir(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    
    return result

mi_lista = ["Hola mundo", 77]
titulo = "Master en Python"
numero = 100
verdadero = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))


"""
lista = [1,2,3]
texto = "Esto es un string"
num = 1
verdadero = true

def tipoDato(dato):
    print(type(dato))

tipoDato(lista)
tipoDato(texto)
tipoDato(num)
tipoDato(verdadero)
"""
