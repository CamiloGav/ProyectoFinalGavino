from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from AppProyectoFinalGavino.models import *
from AppProyectoFinalGavino.forms import *


# Create your views here.

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


