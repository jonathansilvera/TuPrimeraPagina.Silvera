from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Mensaje
from .forms import FormularioMensaje  # Ahora el formulario está definido

class EnviarMensajeView(CreateView):
    model = Mensaje
    form_class = FormularioMensaje
    template_name = 'mensajeria/enviar_mensaje.html'
    success_url = reverse_lazy('bandeja_entrada')

class BandejaEntradaView(ListView):
    model = Mensaje
    template_name = 'mensajeria/bandeja_entrada.html'

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user)

class DetalleMensajeView(DetailView):
    model = Mensaje
    template_name = 'mensajeria/detalle_mensaje.html'