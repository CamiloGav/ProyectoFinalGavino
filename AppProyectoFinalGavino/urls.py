from django.urls import path, include
from AppProyectoFinalGavino import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('/autor', views.autor, name='Autor'),

]