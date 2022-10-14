import mysql.connector
import datetime
import hashlib # para hashear las passwords, encriptar

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python",
    port=3306
)

cursor = database.cursor(buffered=True)

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

        
        

        return[cursor.rowcount, self]

    def identificar(self):
        return self.nombre

