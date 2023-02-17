from tkinter import CASCADE
from django.db import models

# Create your models here.
#ORM - Mapeo de objetos relacionales.


class SeccionProductos(models.Model):
    nombre_section=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name='seccion'
        verbose_name_plural='secciones'


    def __str__(self):
        return self.nombre_section
    

class Productos(models.Model):
    nombre=models.CharField(max_length=25) 
    descripcion=models.CharField(max_length=4500)
    short_description=models.CharField(max_length=1000, blank=True)
    imagen1=models.ImageField(upload_to='Productos') #'upload_to' para indicar la carpeta de destino de la imagen.
    imagen2=models.ImageField(upload_to='Productos', blank=True, null=True)
    imagen3=models.ImageField(upload_to='Productos', blank=True, null=True)
    imagen4=models.ImageField(upload_to='Productos', blank=True, null=True)
    section=models.ForeignKey(SeccionProductos, on_delete=models.CASCADE)
    precio=models.IntegerField()
    art_similares=models.CharField(max_length=30, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'


    def __str__(self):
        return self.nombre
