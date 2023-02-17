from django.shortcuts import render
from django.conf import settings
from Productos.models import Productos
# from PatriaPoloApp.models import Articulos
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    productos_import=Productos.objects.filter(section=5)
    return render(request, "PatriaPoloApp/index.html", {"productos_import": productos_import} )

def productos_descripcion(request):
    return render(request, "PatriaPoloApp/descripcion.html")

def navbar(request):
    return render(request, "PatriaPoloApp/navbar.html")
