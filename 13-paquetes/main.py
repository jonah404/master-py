# Para que python sepa que la carpeta es de paquetes, hay que crear un archivo llamado __init__.py
# que indica que dicha carpeta contiene paquetes, no lleva código dentro.
# Para instalar paquetes externos hay que ir a pypi.org

print("Probando paquetes:")

from mipaquete import pruebas, herramientas

pruebas.probando()
herramientas.nombreCompleto("Jonatan", "Alvarez")



