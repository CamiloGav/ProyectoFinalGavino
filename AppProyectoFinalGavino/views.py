from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from AppProyectoFinalGavino.models import Autor
from AppProyectoFinalGavino.forms import AutorFormulario, ContactoFormulario


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contacto.html')

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

def contactoFormulario(request):
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data


            contacto = ContactoFormulario(nombre=informacion['nombre'], email=informacion['email'], celular=informacion['celular'], descripcion=informacion['descripcion'])
            contacto.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = ContactoFormulario()
    return render (request, 'contactoFormulario.html', {'miFormulario': miFormulario})