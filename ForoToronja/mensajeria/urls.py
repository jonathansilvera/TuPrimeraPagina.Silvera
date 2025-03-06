from django.urls import path
from . import views

app_name = 'mensajeria'

urlpatterns = [
    # URLs de mensajería
    path('enviar/', views.EnviarMensajeView.as_view(), name='enviar_mensaje'),
    path('bandeja-entrada/', views.BandejaEntradaView.as_view(), name='bandeja_entrada'),
    path('mensaje/<int:pk>/', views.DetalleMensajeView.as_view(), name='detalle_mensaje'),
]