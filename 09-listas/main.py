"""
LISTAS (arrays)
son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""

# Definir lista
peliculas = ["batman", "hulk", "superman"]

cantantes = list(('korn', 'BTMH', 'LP'))

years = list(range(2020, 2050))

variada = ["jona", 4, True, 4.5]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
# Indices

peliculas[1] = "spiderman"
print(peliculas[1]) #Indice 1
print(peliculas[-1]) #Indice de atrás hacia adelante
print(cantantes[1:3]) #Indice del 1 al 3
print(cantantes[1:]) #Indice desde el 1 en adelante

# Añadir elementos a lista

cantantes.append("RATM") # Con el método "append"
print(cantantes)

# Recorrer lista
"""
nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)



for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)}. {pelicula}") #Muestra el listado con su correspondiente indice, metodo "index"
"""
# Listas multidimensionales (listas dentro de listas)

contactos = [
    [
        'Jona',
        'Jona@mail.com'
    ],
    [
        'pepe',
        'pepe@pepe.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

# print(contactos[1][0])







