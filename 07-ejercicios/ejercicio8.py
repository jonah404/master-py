"""
ejercicio 8:

    - Cuanto es el x % de x numero: ejemplo cuanto es el 20% de 150.

"""

num1        = int(input("Ingresa el numero para calcular su porcentaje: "))
porcentaje  = int(input(f"¿Que porcentaje quieres sacar de {num1}?: "))

calculo = (num1 * (porcentaje/100))

print(f"El {porcentaje}% de {num1} es: {calculo}")

