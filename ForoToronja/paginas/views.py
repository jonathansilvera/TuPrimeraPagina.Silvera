from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pagina
from .forms import PaginaForm
from django.urls import reverse_lazy


class ListaPaginasView(ListView):
    model = Pagina
    template_name = 'paginas/lista.html'
    context_object_name = 'paginas'

class DetallePaginaView(DetailView):
    model = Pagina
    template_name = 'paginas/detalle.html'

class CrearPaginaView(CreateView):
    model = Pagina
    form_class = PaginaForm
    template_name = 'paginas/crear.html'
    success_url = reverse_lazy('paginas:lista')
    def form_valid(self, form):
        return super().form_valid(form)  

class EditarPaginaView(UpdateView):
    model = Pagina
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'paginas/editar.html'
    success_url = reverse_lazy('paginas:editar')

class EliminarPaginaView(DeleteView):
    model = Pagina
    success_url = '/paginas/lista/'
    template_name = 'paginas/eliminar.html'