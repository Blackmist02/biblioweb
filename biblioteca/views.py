from django.shortcuts import render
from .models import libro, usuario, prestamo
# Create your views here.

def index(request):
    libros = libro.objects.all()
    usuarios = usuario.objects.all()
    prestamos = prestamo.objects.all()
    context = {
        'libros': libros,
        'usuarios': usuarios,
        'prestamos': prestamos
    }
    return render(request, 'biblioteca/index.html', context)