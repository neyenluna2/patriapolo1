class Producto:
    def __init__(self, request): # Creamos una función que llame al request. Usamos el método init como constructor.
        self.request=request # Decimos que el request es igual a la request en general.
        self.session=request.session # Y que la sesion es igual a la sesion iniciada en el request.
        producto=self.session.get("producto") # Que en producto se traiga el producto con la sesión.
        if not producto: # Si no hay producto:
            producto=self.session["producto"]={} # El producto es igual a un diccionario vacío.
        #else: De lo contrario: 
        self.producto=producto # Que el producto sea igual al producto. 

    def agregar(self, producto): # Creamos una función para agregar productos.
        if(str(producto.id) not in self.producto.keys()):
            self.producto[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "descripcion": producto.descripcion,
                "imagen": producto.imagen1.url,
            }
        else:
            for key, value in self.producto.items():
                if key == str(producto.id):
                    value["producto_id"] = key
                    break
        # self.guardar_producto()
        self.producto

    '''def guardar_producto(self):
        self.session["producto"]=self.producto
        self.session.modified=True'''