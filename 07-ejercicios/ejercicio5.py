"""
Ejercicio 5:
    - Hacer un programa que muestre todos los numeros entre dos numeros que diga el ususario.-
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 < num2:
    for contador in range(num1, (num2 + 1)):
        print(contador)
else:
    print("El número 1 debe ser menor al número 2")