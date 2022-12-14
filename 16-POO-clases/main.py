# Programacion orientada a objetos
# Definir una clase (molde para crear mas objetos de ese tipo)
# (coche) con características similares)

class Coche: #La clase hace que se puedan crear multiples objetos con ls mismas características

    # Atributos o Propiedades
    # Características
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F50"
    velocidad = 300
    hp = 500
    plazas = 2

    # Metodos, son acciones que hace el objeto (coche)(funciones)

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definicion de clase

# Crear objeto / Instanciar la clase

coche = Coche() # la variable es el Objeto

print("Coche 1: ")

coche.setColor("Amarillo")
coche.setModelo("F250")


print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.velocidad)

# Crear mas objetos

coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("Coche 2: ")

print(coche2.getColor())
print(coche2.marca, coche2.getModelo(), coche2.getColor())





