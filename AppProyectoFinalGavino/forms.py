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

# class PosteoFormulario(forms.Form):
#     # imagen = forms.ImageField(upload_to='nombredecarpeta', null=True, blank=True) #crear media y ""
#     titulo = forms.CharField(max_length=100, help_text='Ingresa el título')
#     descripcion = forms.Textarea(max_length=300, help_text='Ingresa una breve descripción')
#     autor = forms.CharField(max_length=40)
#     profesion = forms.CharField(max_length=40)
#     fechaPublicacion = forms.DateField()
