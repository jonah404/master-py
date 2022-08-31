"""
# Bucle while
Es una esctuctura de control que itera o repita la ejecucion de una serie 
de instrucciones tantas veces como sea necesario hasta que deje de 
cumplirse la condicion.

while condicion:
    bloque de instrucciones
    actualizacion de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1


print("------------------------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

# Ejemplo 

print("####### EJEMPLO #######")

numUsuario = int(input("¿De que número quieres saber la tabla?: "))

if numUsuario < 1:
    numUsuario = 1

print(f"### Tabla del {numUsuario} ###")

contador = 1

while contador <= 10:
    print(f"{numUsuario} x {contador} = {numUsuario * contador}")
    contador += 1
else:
    print("Tabla finalizada.")


