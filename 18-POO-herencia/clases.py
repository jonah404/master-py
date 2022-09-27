# Herencia: es la posibilidad de compartir atributos y metodos entre clases.
# y que diferentes clases hereden de otros. 

class Persona:
    """
    nombre
    apellido
    altura
    edad
    """

    # Geters y Seters

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self):
        self.nombre = nombre

    def setApellido(self):
        self.apellido = apellido

    def setAltura(self):
        self.altura = altura
    
    def setEdad(self):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"

class Informático(Persona): # Herdea de la clase persona
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, Python"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes =lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "Ordenador reparado"




