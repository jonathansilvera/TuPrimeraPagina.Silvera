from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_posteo, name='crear_posteo'),
    path('lista/', views.lista_posteos, name='lista_posteos'),
]