"""
ejercicio10:
    - Programa que pida la nota de x cantidad de alumnos y imprimir cuantos aprobaron y cuantos no.
"""

contador    = 1
aprobados   = 0
reprobados = 0

num_alumnos = int(input("¿Cuantos alumnos tienes? "))

while contador <= num_alumnos:
    nota = int(input(f"¿Que nota tiene el alumno {contador}?: "))
    
    if nota>=5:
        aprobados   += 1
    else:
        reprobados += 1
    
    contador += 1

print(f"Cantidad de alumnos aprobados: {aprobados}")
print(f"Cantidad de alumnos aprobados: {reprobados}")