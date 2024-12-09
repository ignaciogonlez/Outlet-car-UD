from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language

urlpatterns = [
    # Rutas sin traducción
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('i18n/', include('django.conf.urls.i18n')),  # Para el cambio de idioma
]

# Rutas que soportan internacionalización
urlpatterns += i18n_patterns(
    path('', include('appOutletDjango.urls')),  # Incluye las rutas de la aplicación
)

# Archivos estáticos (si es necesario en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
