from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('appOutletDjango.urls')),  # Incluye las rutas de la aplicación
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
]
