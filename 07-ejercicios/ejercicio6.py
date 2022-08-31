"""
ejercicio 6
    - Mostrar todas las tablas de multiplicar del 1 al 10.
    - mostrando el titulo de la tabla y luego las multiplicaciones.
"""

for titulo in range(1,11):
    print(f"Tabla del {titulo}:")
    for num in range(1,11):
        print(f"{num} x {titulo} = {num*titulo}")   




