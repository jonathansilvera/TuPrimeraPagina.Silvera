from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Perfil
from .forms import FormularioRegistroUsuario, FormularioActualizarPerfil
from django.contrib.auth import login



class RegistroUsuarioView(CreateView):
    form_class = FormularioRegistroUsuario
    template_name = 'cuentas/registro.html'
    success_url = reverse_lazy('inicio')  # Redirige después del registro exitoso

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Inicia sesión automáticamente después del registro
        return super().form_valid(form)  # Retorna la respuesta adecuada
        

class LoginView(LoginView):
    template_name = 'cuentas/login.html'

class LogoutView(LogoutView):
    next_page = 'inicio'

class PerfilView(DetailView):
    model = Perfil
    template_name = 'cuentas/perfil.html'
    context_object_name = 'perfil'

#class ActualizarPerfilView(UpdateView):
#    model = Perfil
#    form_class = FormularioActualizarPerfil
#    template_name = 'cuentas/actualizar_perfil.html'
#    success_url = reverse_lazy('perfil')
#    def get_success_url(self):
#        return reverse_lazy('perfil', kwargs={'pk': self.object.pk})
    
class ActualizarPerfilView(UpdateView):
    model = Perfil
    form_class = FormularioActualizarPerfil
    template_name = 'cuentas/actualizar_perfil.html'

    def get_success_url(self):
        return reverse_lazy('cuentas:perfil', kwargs={'pk': self.object.pk})
