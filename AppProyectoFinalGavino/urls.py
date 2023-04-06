from django.urls import path, include
from AppProyectoFinalGavino import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('inicio', views.inicio, name='Inicio'),
    path('autor', views.autor, name='Autor'),
    path('fotoAvatar', views.fotoAvatar, name='fotoAvatar'),
    path('about', views.about, name='About'),
    path('contacto', views.contacto, name='Contacto'),
    path('newsletter', views.newsletter, name='Newsletter'),
    path('autorFormulario', views.autorFormulario, name='AutorFormulario'),
    path('posteoFormulario', views.posteoFormulario, name='PosteoFormulario'),
    #path('contactoFormulario', views.contactoFormulario, name='ContactoFormulario'),
    # path('newsletterFormulario', views.newsletterFormulario, name='NewsletterFormulario'),
    path('busquedaAutor', views.busquedaAutor, name='BusquedaAutor'),
    path('buscar/', views.buscar),
    path('borrar/<int:pk>', views.AutorDelete.as_view(), name='Delete'),
    path('', views.leerPosteo, name='LeerPosteo'),
    path('leerAutor',views.leerAutor, name='LeerAutor'),
    path('eliminarAutor/<autor_nombre>/', views.eliminarAutor, name='EliminarAutor'),
    path('editarAutor/<autor_nombre>', views.editarAutor, name='EditarAutor'),
    path('login', views.login_request, name='Login'),
    path('registro', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
]