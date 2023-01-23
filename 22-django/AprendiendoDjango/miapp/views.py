from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
# MVC = Modelo vista controlador -> Acciones (metodos)
# MVT = Modelo template vista -> Acciones (metodos)


layout = """
<h1>Sitio web con django | Jonatan</h1>
<hr>
<ul>
    <li>
        <a href="/inicio">Inicio</a> 
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a> 
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a> 
    </li>
    <li>
        <a href="/contacto-dos">Contacto</a> 
    </li>
</ul>
<hr>
"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    ""
    
    year = 2022
    
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"
    """

    year = 2022
    hasta = range(year, 2051)

    nombre = "Jonatan"
    lenguajes = ['Javascript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
        })


def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="Jona", apellido="alvarez")

    return render(request, 'pagina.html', {
        'texto': 'texto',
        'lista': ['uno', 'dos', 'tres']
    })


def contacto(request, nombre="", apellido=""): # Recoger parámetros por url, parámetros opcionales
    
    html = ""

    if nombre and apellido:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellido}</h3>"
    
    return HttpResponse(layout+f"<h2>Página de contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request):

    if request.method == 'POST':
        title = request.POST['title']

        if len(title) <= 5:
            return HttpResponse("<h2>El título es muy pequeño</h2>")

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()

        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")


    
def create_article(request):

    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            # Crear mensaje flash (sesion que solo se muestra una vez)

            messages.success(request, f'Has creado correctamente el artículo {articulo.id}.')

            return redirect('articulos')
            #return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))

    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html',{'form': formulario})


def articulo(request):
    try:
        articulo = Article.objects.get(id=2, title="First articulo", public=True) #pk es primary key, tambien puede ser id o title
        response = f"Articulo: </br> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"
    
    return HttpResponse(response)

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Superman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):

    articulos = Article.objects.filter(public=True).order_by('-id')

#    articulos = Article.objects.filter(id__lte=6, title__contains='articulo')

#    articulos = Article.objects.filter(
#        Q(title__contains="2") | Q(title__contains="3")
 #   )

#    articulos = Article.objects.filter(
#        title="Articulo",
#    ).exclude(
#        public=False
#    )

    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=1")

    """
    Poniendo el menos(-) adelante ordena de forma descendente, 
    también se puede usar el título y otro dato, con[:3] limita la cantidad 
    que muestra, también puede ser [2:3] muestra desde el elemento dos al 3.
    """
    
    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
