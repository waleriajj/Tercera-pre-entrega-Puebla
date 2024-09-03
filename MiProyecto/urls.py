from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore # type: ignore
from libros import urls as libros_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include(libros_urls)),  # Esto asegura que las URLs de 'libros' sean accesibles
]
