from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from AppProyectoFinalGavino.models import *
from AppProyectoFinalGavino.forms import *
from django.views.generic.edit import DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


# Create your views here.

@login_required
def editarPerfil(request):
    usuario = request.user 
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(miFormulario)
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {'mensaje':'Contraseña incorrecta.'})

            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, 'inicio.html', {'mensaje':'Usuario Creado'})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contras)
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "inicio.html", {"mensaje":"Error, datos incorrectos."})
        else:
            return render(request, "inicio.html", {"mensaje":"Error, formulario erroneo."})
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

    
def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

# def contacto(request):
#     return render(request, 'contacto.html')

# def newsletter(request):
#     return render(request, 'newsletter.html')

def autor(self):
    autor = Autor(nombre="Pedro", apellido="Gaviño", genero="Fantasía")
    autor.save()
    muestraDeTexto = f'Nombre y apellido: {autor.nombre}, {autor.apellido} - Genero: {autor.genero}'

    return HttpResponse(muestraDeTexto)

def posteoFormulario(request):
    if request.method == 'POST':
        miFormulario = PosteoFormulario(request.POST)


        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            posteo = Posteo(titulo=informacion['titulo'], descripcion=informacion['descripcion'],autor=informacion['autor'], profesion=informacion['profesion'], fechaPublicacion=informacion['fechaPublicacion'])
            posteo.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = PosteoFormulario()
    return render (request, 'posteoFormulario.html', {'miFormulario': miFormulario})



def autorFormulario(request):
    if request.method == 'POST':
        miFormulario = AutorFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data


            autor = Autor(nombre=informacion['nombre'], apellido=informacion['apellido'], genero=informacion['genero'])
            autor.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = AutorFormulario()
    return render (request, 'autorFormulario.html', {'miFormulario': miFormulario})

def newsletter(request):
    if request.method == 'POST':
        miFormulario = NewsletterFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            newsletter = Newsletter(email=informacion['email'])
            newsletter.save()

            return render(request, 'inicio.html')
    
    else:
        miFormulario = NewsletterFormulario()
    return render (request, 'newsletter.html', {'miFormulario': miFormulario})

def contacto(request):
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data


            contacto = Contacto(nombre=informacion['nombre'], email=informacion['email'], celular=informacion['celular'], descripcion=informacion['descripcion'])
            contacto.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = ContactoFormulario()
    return render(request, 'contacto.html', {'miFormulario': miFormulario})


# def publicacion(request):
#     posteo = Posteo.objects.all()
#     contexto = {'posteo':posteo}

#     return render(request, 'inicio.html', contexto)

def busquedaAutor(request):
    return render(request, 'busquedaAutor.html')

def buscar(request):
    if request.GET['genero']:
        genero = request.GET['genero']
        autor = Autor.objects.filter(genero__icontains=genero)

        return render(request, 'resultadoBusqueda.html', {"autor": autor, "genero": genero})
    
    else:

        respuesta = f'No enviaste datos de busqueda'

    return HttpResponse(respuesta)

def leerPosteo(request):
    posteo = Posteo.objects.all()

    contexto = {"posteo": posteo}

    return render(request, "inicio.html", contexto)

def eliminarAutor(request, autor_nombre):
    try:
        autor = Autor.objects.get(nombre=autor_nombre)
    except Autor.MultipleObjectsReturned:
        autor = Autor.objects.filter(nombre=autor_nombre)[0]
    autor.delete()

    autores = Autor.objects.all()
    contexto = {"autores":autores}
    return render(request, "leerAutor.html", contexto)

def leerAutor(request):
    autores = Autor.objects.all()

    contexto = {"autores": autores}

    return render(request, "leerAutor.html", contexto)

@login_required
def editarAutor(request, autor_nombre):
    autor = Autor.objects.get(nombre=autor_nombre)
    if request.method == 'POST':
        miFormulario = AutorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            autor.nombre = informacion['nombre']
            autor.apellido = informacion['apellido']
            autor.genero = informacion['genero']

            autor.save()
            return render(request, "inicio.html")
    else:
        miFormulario = AutorFormulario(initial={'nombre':autor.nombre,'apellido':autor.apellido,'genero':autor.genero})

        return render(request, "editarAutor.html", {"miFormulario":miFormulario, "autor_nombre":autor_nombre})

class AutorDelete(DeleteView):
    model = Autor
    template_name = "autor_confirm_delete.html"
    success_url = "/AppProyectoFinalGavino/leerAutor"