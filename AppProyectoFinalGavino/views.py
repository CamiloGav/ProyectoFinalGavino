from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from AppProyectoFinalGavino.models import Autor


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

def autor(self):
    autor = Autor(nombre="Pedro", apellido="Gaviño", genero="Fantasía")
    autor.save()
    muestraDeTexto = f'Nombre y apellido: {autor.nombre}, {autor.apellido} - Genero: {autor.genero}'

    return HttpResponse(muestraDeTexto)