from django.urls import path  # type: ignore # Importamos el módulo de rutas de Django
from libros import views  # Importamos las vistas desde la aplicación 'libros'

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página principal
    path('buscar/', views.buscar, name='buscar'),  # Ruta para la funcionalidad de búsqueda # type: ignore
]
