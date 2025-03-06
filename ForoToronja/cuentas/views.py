from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Perfil
from .forms import FormularioRegistroUsuario, FormularioActualizarPerfil



class RegistroUsuarioView(CreateView):
    form_class = FormularioRegistroUsuario
    template_name = 'cuentas/registro.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
    
    def registro(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('inicio') 
            else:
                return render(request, 'cuentas/registro.html', {'form': form})
        else:        
            form = UserCreationForm()
            return render(request, 'cuentas/registro.html', {'form': form})
        

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
