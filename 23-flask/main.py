from flask import Flask, redirect, url_for, render_template # redirect y url_for se usan para redireccionar, render_template se usa para
from datetime import datetime

app = Flask(__name__) #Crear la app de flask (Instanciando framework dde Flask)

# Context processors (es un código que va a estar disponible para usar en todas las páginas)

@app.context_processor 
def date_now():
    return{
        'now': datetime.utcnow()
    }

# Endpoints (Rutas)

@app.route('/') #Crear la ruta
def index(): #Vincular la ruta a un método (se puede poner un nombre diferente al de la ruta)
    return render_template('index.html', 
                           dato1="Valor",
                           dato2="Valor2",
                           lista=["Uno", "Dos", "Tres"]
                           )

@app.route('/informacion')
@app.route('/informacion/<string:nombre>') # <nombre> es un parámetro, de ésta forma páso parámetros y puedo recibir los datos que viajan en el
@app.route('/informacion/<string:nombre>/<string:apellido>')
def informacion(nombre = "", apellido = ""):

    texto = ""

    if nombre != "" or apellido != "":
        texto = f"Bienvenido, {nombre} {apellido}"
        
    return render_template('informacion.html', texto=texto) #Se puede pasar la variable para como parámetro para mostrarla en el html

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion=None):

    if redireccion != None:
        return redirect(url_for('lenguajes'))

    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')

if __name__ == '__main__': #Esto es para identificar que este archivo es el fichero principal
    app.run(debug=True) #Esto es para ejecutar el servidor y que en cada modificación se recargue automáticamente
