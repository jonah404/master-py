"""
Variables locales y globales.

Locales: Se definen dentro de la funcion y no se puede usar fuera
de ella, solo están disponibles dentro. A no ser que hagamos un return.

Globales: Son las que se declaaran fuera de una funcion y están
disponibles dentro y fuera de ellas.

"""

# VARIABLES GLOBALES

frase = "Mi frase"

print(frase)

# VARIABLES LOCALES

def holamundo():
    frase = "Mi Frase."
    print("Dentro de la función.")
    print(frase)

    year = 2022
    print(year)

    global website # Convierte una variable local en global
    website = "jon.com"
    print("Dentro de la función: ", website)

    return "Dato devuelto " + str(year)

print(holamundo())
print("Fuera de la funcion", website)


