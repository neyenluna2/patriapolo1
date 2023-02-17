
from django.urls import path

#Importamos para poder buscar ver nuestras imagenes.
from django.conf import settings
from django.conf.urls.static import static

from PatriaPoloApp.views import (
    inicio,
    productos_descripcion,
    navbar,
)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path("descripcion/", productos_descripcion, name="Descripcion"),
    path("navbar/", navbar, name="navbar"),
]

#Para ver nuestras imagenes en el panel del admin:
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #settings.py, linea 123 y 124.