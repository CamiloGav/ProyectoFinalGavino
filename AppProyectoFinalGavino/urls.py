from django.urls import path, include
from AppProyectoFinalGavino import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('autor', views.autor, name='Autor'),
    path('about', views.about, name='About'),
    path('contacto', views.contacto, name='Contacto'),
    path('autorFormulario', views.autorFormulario, name='AutorFormulario'),
    path('contactoFormulario', views.contactoFormulario, name='ContactoFormulario')

]