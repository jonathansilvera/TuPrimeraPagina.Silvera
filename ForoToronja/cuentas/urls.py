from django.urls import path , include
from . import views

app_name = 'cuentas'

urlpatterns = [
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('perfil/<int:pk>/', views.PerfilView.as_view(), name='perfil'),
    path('perfil/editar/<int:pk>/', views.ActualizarPerfilView.as_view(), name='editar_perfil'),
    
]