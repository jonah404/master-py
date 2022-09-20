# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores
"""
try:

    nombre = input("¿Cuál es tu nombre?: ")

    if len(nombre)>1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingresa tu nombre nuevamente")
else:
    print("Todo salió perfecto")

finally:
    print("Fin de la iteración")
"""

# Multiples excepciones
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros.")
except ValueError:
    print("Introduce un numero correcto.")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__) #Detecta el tipo de error
"""

#Exepciones personalizadas o lanzar excepcion (rasie)
try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Ingresa tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es correcta")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido! {nombre}")
except ValueError:
    print("Introducce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)




