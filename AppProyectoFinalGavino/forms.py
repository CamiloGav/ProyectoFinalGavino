from django import forms

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    genero = forms.CharField()

class ContactoFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    celular = forms.CharField()
    descripcion = forms.CharField()