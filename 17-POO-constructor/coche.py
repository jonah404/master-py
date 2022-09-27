class Coche:

    color = "Rojo"
    marca = "Ferrari"
    modelo = "F50"
    velocidad = 300
    hp = 500
    plazas = 2

    soy_publico = "soy un atributo publico" #Propiedad publica
    __soy_privado = "Soy un atributo privado" # Con los dos guiones indicamos que la propiedad es privada.

    #Constructor
    def __init__(self, color, marca, modelo, velocidad, hp, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.hp = hp
        self.plazas = plazas

    #Metodos, son acciones que hace el objeto (coche)(funciones)

    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "------- Informacion del vehículo------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        
        return info