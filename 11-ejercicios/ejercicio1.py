"""
Hacer un programa que tenga 8 numeros enteros
1- Recorrer la lista y mostrarla
2- Hacer funcion que recorra lista de números y devuelva un string para mostrarla
3- Ordenarla y mostrarla
4- Mostrar su longitud
5- Buscar algun elemento (que el usuario pida por teclado)
"""

lista = [456,4856,0,4564,48965,6123,7,1238]

#1 
print("Ejercicio 1: Recorrer y mostrar lista")

for num in lista:
    print(num)

#2
print("Ejercicio 2: Hacer función que recorra la lista y la muestre")

def recorre(lista):
    resultado = ""
    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"
    return resultado

print(recorre(lista))

#3
print("Ejercicio 3: Ordenar lista y mostrarla")
lista.sort()
print(lista)

#4
print("Ejercicio 4: Mostrar longitud de la lista")
print(len(lista))

#5
print("Ejercicio 5: Buscar elemento de la lista")

num_list = int(input("Número a buscar: "))

if num_list in lista:
    print(f"El numero {num_list} se encuentra en la lista!")
else:
    print(f"El número {num_list} no se encuentra en la lista :(")

#5 BIS OTRA FORMA (incorporado manejo de errores):
try:
    busqueda = int(input("Ingresa el número: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda < 0:
        busqueda = int(input("Ingresa el número: "))
    else:
        print(f"Ingresste el {busqueda}")

    print(f"Buscar en la lista el numero {busqueda}")


    search = lista.index(busqueda)

    print(f"El número buscado existe en la lista, es el indice: {search}")
except:
    print("El número no está en la lista")




