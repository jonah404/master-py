import datetime
import hashlib # para hashear las passwords, encriptar
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, email, passwd):
        self.nombre   = nombre
        self.apellido = apellido
        self.email    = email
        self.passwd   = passwd

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]

        except:
            
            result = [0, self]

        return result

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s" # Consulta para ver si existe el usuario

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result


