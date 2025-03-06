from django.db import models
from django.utils import timezone

class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='paginas/')
    fecha = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.titulo
    
    