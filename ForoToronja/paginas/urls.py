from django.urls import path
from . import views

app_name = 'paginas'  
urlpatterns = [
    path('lista/', views.ListaPaginasView.as_view(), name='lista'),
    path('crear/', views.CrearPaginaView.as_view(), name='crear'),  
    path('detalle/<int:pk>/', views.DetallePaginaView.as_view(), name='detalle'),  
    path('editar/<int:pk>/', views.EditarPaginaView.as_view(), name='editar'),  
    path('eliminar/<int:pk>/', views.EliminarPaginaView.as_view(), name='eliminar'), 
]
