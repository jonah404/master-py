def holaMundo(nombre):
    return f"Hola como estas {nombre}"


def calculadora(num1, num2, basicas=False):

    suma  = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div   = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(div)

    return cadena


