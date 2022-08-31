"""
ejercicio9:

    - Programa que pida numeros al usuario indefinidamente hasta que ingrese el numero 111

"""

contador = 1

while contador < 100:
    numero = int(input("Ingresa un número: "))
    if numero == 111:
        break
    else:
        print(f"Ingresaste el número {numero}")

    