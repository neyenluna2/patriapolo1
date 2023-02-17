from django.contrib import admin
from .models import Productos, SeccionProductos

# Register your models here.
    
class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=('updated', 'created')

class SeccionAdmin(admin.ModelAdmin):
    readonly_fields=('updated', 'created')
    

#Registramos nuestra/s Clases en el panel del administrador.
admin.site.register(Productos, ProductosAdmin)
admin.site.register(SeccionProductos, SeccionAdmin)

