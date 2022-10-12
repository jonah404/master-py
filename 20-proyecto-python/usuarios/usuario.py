class Usuario:

    def __init__(self, nombre, apellido, email, passwd):
        self.nombre   = nombre
        self.apellido = apellido
        self.email    = email
        self.passwd   = passwd

    def registrar(self):
        return self.nombre

    def identificar(self):
        return self.nombre