
"""
# FOR

for variable in elemmento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print(f"Voy por el {contador}")

    resultado += contador

print(f"El resultado es: {resultado}")


# Ejemplo tablas de multiplicar
print("\n############## EJEMPLO ############")

numUsuario = int(input("¿De que número quieres saber la tabla? "))

if numUsuario < 1:
    numUsuario = 1

print(f"### Tabla de multiplicar del número {numUsuario} ###0")

for numTabla in range(1, 11):

    if numUsuario == 45:
        print("El 45 es un número prohibido!!, no se mostrará su multiplicación")
        break

    print(f"{numUsuario} x {numTabla} = {numUsuario* numTabla}")
else:
    print("Tabla finalizada.") 




