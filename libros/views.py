from django.shortcuts import render

from libros.models import Libro

def index(request):
    return render(request, 'libros/index.html')

def buscar(request):
    if request.method == "GET":
        query = request.GET.get('query')
        resultados = Libro.objects.filter(titulo__icontains=query)
        return render(request, 'libros/resultados.html', {'resultados': resultados})
