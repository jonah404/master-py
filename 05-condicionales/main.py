# Condicional IF

"""
if condicion:
    instrucciones
else:
    otraas instrucciones


# Operadores de comparacioón

== igual
!= distinto
< menor que
> mayor que
<= menor igual que
>= mayor igual que

# Operadores logicos
and Y
or O
! negacion
not NO

"""
"""
# ejemplo1
print("########## ejemplo 1#########")

color = "verde"
#color = input("Adivina cual es mi color favorito: ")

if color == "verde":
    print("Excelente!")
    print("Mi color favorito es verde")
else:
    print("Incorrecto!")

# Ejemplo 2
print("########## ejemplo 2#########")

year = int(input("Ingrese el año actual: "))

if year >= 2022:
    print("Estamos de 2022 en adelante")
else:
    print("El año no debe ser menor al actual")

# Ejemplo 3
print("########## ejemplo 3#########")

name = "Jonatan"
city = "Villa Ramallo"
continent = "Sud América"
age = 37
adult = 18

if age >= adult:
    print(f"{name} es mayor de edad")

    if continent != "Europa":
        print("El usuario no es Europeo")
    else:
        print(f"Es Europeo y de {city}")

else:
    print(f"{name} No es mayor de edad")

# Ejemplo 4
print("########## ejemplo 4#########")

day = int(input("Ingresa el día de la semana: "))

if day == 1:
    print("Es lunes")
else:
    if day ==2:
        print("Es martes")
    else:
        if day == 3:
            print("Es miercoles")
        else:
            if day == 4:
                print("Es jueves")
            else:
                if day == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")


if day == 1:
    print("lunes")
elif day == 2:
    print("martes")
elif day == 3:
    print("miercoles")
elif day == 4:
    print("jueves")
elif day == 5:
    print("viernes")
else:
    print("finde")

# Ejemplo 5
print("########## ejemplo 5#########")

minAge = 18
maxAge = 65
workerAge = int(input("Ingrese su edad: "))

if workerAge >= 18 and workerAge <= 65:
    print("Está en edad para trabajar")
else:
    print("Su edad no está admitida para trabajar")
"""

# Ejemplo 6
print("########## ejemplo 6#########")

country = "Alemania"

if country == "Mexico" or country == "España" or country == "Colombia":
    print(f"{country} es un pais de habvla hispana")
else:
    print(f"{country} no es un pais de habla hispana")

# Ejemplo 7
print("########## ejemplo 7#########")

country = "España"

if not (country == "Mexico" or country == "España" or country == "Colombia"):
    print(f"{country} No es un pais de habvla hispana")
else:
    print(f"{country} es un pais de habla hispana")

# Ejemplo 8
print("########## ejemplo 8#########")

country = "Colombia"

if country != "Mexico" and country != "España" and country != "Colombia":
    print(f"{country} No es un pais de habvla hispana")
else:
    print(f"{country} es un pais de habla hispana")