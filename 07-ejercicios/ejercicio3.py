"""
Ejercicio3:
    - Escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales.
    - Resolverlo con for y while
"""

# WHILE

contador = 0
while contador <= 60:

    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es: {cuadrado}")
    
    contador += 1

# FOR

for num in range(61):
    cuadrado = num*num
    print(f"El cuadrado de {num} es: {cuadrado}")

