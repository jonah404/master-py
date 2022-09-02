nombre = "Jona"

# FUNCIONES GENERALES

print(type(nombre))

# Detectar el tipado, tipo de dato.

comprobar = isinstance(nombre, str)
if comprobar == True:
    print("Esa variable es un tipo de dato string.")
else:
    print("Ese dato no es un tipo de dato string.")

if not isinstance (nombre, float):
    print("La variable no es un numero con decimales.")

# Limpiar espacios

frase = "      frase "
print(frase.strip())

# Eliminar variables

year = 2022
print(year)
del year
#print(year)

# Comprobr variables vacías
texto = "  ff  "

if len(texto)<=0:
    print("La vaariable está vcía.")
else:
    print("La variable tiene contenido: ", len(texto))

# Encontrar cracteres

frase = "mi frase"
print(frase.find("frase"))


# Reemplazar palaabras en un string}

nueva_frase = frase.replace("mi", "la")
print(nueva_frase)

# Mayúsculas y minúsculas
print(nombre) 
print(nombre.lower())
print(nombre.upper())

