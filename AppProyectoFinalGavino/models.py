from django.db import models
from django.contrib.auth.models import User


#user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posteo')

class Posteo(models.Model):

    titulo = models.CharField(max_length=100, help_text='Ingresa el título')
    descripcion = models.TextField(max_length=300, help_text='Ingresa una breve descripción')
    autor = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    fechaPublicacion = models.DateField()

    def __str__(self):
        return f'{self.titulo} de {self.autor}'

    
class Autor(models.Model):
    nombre = models.CharField(max_length=40, help_text='Ingresa el nombre')
    apellido = models.CharField(max_length=40, help_text='Ingresa el apellido')
    genero = models.CharField(max_length=40, help_text='Ingresa el genero')

    def __str__(self):
        return f'Autor: {self.nombre}, {self.apellido} - Genero: {self.genero}'
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    celular = models.IntegerField()
    mensaje = models.TextField(max_length=300, help_text='Ingresa una breve descripción')

    def __str__(self):
        return f'De {self.nombre}: {self.mensaje[0:50]}...'

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


    