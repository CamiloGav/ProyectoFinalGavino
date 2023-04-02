from django import forms

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    genero = forms.CharField()

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    celular = forms.IntegerField()
    descripcion = forms.CharField(max_length=30)

class NewsletterFormulario(forms.Form):
    email = forms.EmailField()
