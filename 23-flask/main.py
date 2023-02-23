from flask import Flask

app = Flask(__name__) #Crear la app de flask (Instanciando framework dde Flask)

@app.route('/') #Crear la ruta
def index(): #Vincular la ruta a un método (se puede poner un nombre diferente al de la ruta)
    return "Aprendiendo Flask"

@app.route('/informacion')
def informacion():
    return "<h1>Página de información</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Página de contacto</h1>"

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Página de lenguajes</h1>"

if __name__ == '__main__': #Esto es para identificar que este archivo es el fichero principal
    app.run(debug=True) #Esto es para ejecutar el servidor y que en cada modificación se recargue automáticamente
