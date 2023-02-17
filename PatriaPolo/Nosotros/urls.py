from django.urls import path
from django.conf import settings

from .views import (
    nosotros,
)

urlpatterns = [
path('', nosotros, name="Nosotros"),
]