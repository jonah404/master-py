"""
Ejercicio2
Escribir un programaa que añada 
valores a una lista mientras que su longitud sea menor a 120
y luego mostrar la lista.
Usar while y for.
"""

#Con for
"""
coleccion = []

for contador in range(0,120):
    coleccion.append(f"Elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion)
"""
#Con while

coleccion = []
x=0

while x<120:
    coleccion.append(f"Elemento-{x}")
    x+=1

print(coleccion)





