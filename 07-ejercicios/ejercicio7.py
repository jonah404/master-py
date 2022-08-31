"""
ejercicio7
    - Hacer un programa que muestre todos los numeros impares entre dos numeros que decida el usuario.
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


if num1 < num2:
    for contador in range(num1, (num2+1)):
        if contador%2 == 0:
            print(f"{contador} es par.")
        else:
            print(f"{contador} es impar.")
else:
    print("El número 1 debe ser mayor al 2")