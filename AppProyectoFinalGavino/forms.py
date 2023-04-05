from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class PosteoFormulario(forms.Form):

    titulo = forms.CharField(max_length=100, help_text='Ingresa el título')
    descripcion = forms.CharField(max_length=300, help_text='Ingresa una descripción')
    autor = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=40)
    fechaPublicacion = forms.DateField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name   = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
        help_text = {k:"" for k in fields}
