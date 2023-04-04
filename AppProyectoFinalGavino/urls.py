from django.urls import path, include
from AppProyectoFinalGavino import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', views.inicio, name='Inicio'),
    path('autor', views.autor, name='Autor'),
    path('about', views.about, name='About'),
    path('contacto', views.contacto, name='Contacto'),
    path('newsletter', views.newsletter, name='Newsletter'),
    path('autorFormulario', views.autorFormulario, name='AutorFormulario'),
    path('posteoFormulario', views.posteoFormulario, name='PosteoFormulario'),
    #path('contactoFormulario', views.contactoFormulario, name='ContactoFormulario'),
    # path('newsletterFormulario', views.newsletterFormulario, name='NewsletterFormulario'),
    path('busquedaAutor', views.busquedaAutor, name='BusquedaAutor'),
    path('buscar/', views.buscar),
    path('leerPosteo', views.leerPosteo, name='LeerPosteo'),
    path('leerAutor',views.leerAutor, name='LeerAutor'),
    path('eliminarAutor/<autor_nombre>/', views.eliminarAutor, name='EliminarAutor'),
    path('editarAutor/<autor_nombre>', views.editarAutor, name='EditarAutor')
]