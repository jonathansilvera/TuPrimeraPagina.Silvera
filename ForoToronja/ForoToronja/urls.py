from django.contrib import admin
from django.urls import path, include
from publicaciones.views import inicio, acerca_de
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  
    path('acerca-de/', acerca_de, name='acerca_de'),  
    path('cuentas/', include('cuentas.urls')),  
    path('mensajeria/', include('mensajeria.urls')),  
    path('paginas/', include('paginas.urls')),  
    path('publicaciones/', include('publicaciones.urls')),
    path('cuentas/', include('cuentas.urls', namespace='cuentas')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

