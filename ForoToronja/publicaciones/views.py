from django.shortcuts import render, redirect
from .models import Posteo
from .forms import PosteoForm

def crear_posteo(request):
    if request.method == 'POST':
        form = PosteoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_posteos')  
    else:
        form = PosteoForm()
    return render(request, 'publicaciones/crear_posteo.html', {'form': form})

def lista_posteos(request):
    posteos = Posteo.objects.all().order_by('-fecha_creacion')  
    return render(request, 'publicaciones/lista_posteos.html', {'posteos': posteos})

def inicio(request):
    return render(request, 'inicio.html')

def acerca_de(request):
    return render(request, 'acerca_de.html')
 