from django.shortcuts import render

# Create your views here.


from .models import Productos
from .producto import Producto
from .precio_dolar import precio_venta


'''def productos(request):
    productos_import=Productos.objects.filter(section=5)
    indumentaria=Productos.objects.filter(section=4)
    palos=Productos.objects.filter(section=3)
    monturas=Productos.objects.filter(section=2)
    return render(request, "productos/products_tienda.html", {
        "productos_import": productos_import,
        "indumentaria": indumentaria,
        "palos": palos,
        "monturas": monturas
        })'''

def productos_favoritos(request):
    productos_import=Productos.objects.filter(section=5)
    return render(request, "productos/favoritos_p.html", {"productos_import": productos_import})


'''def detalles(request, producto_id):
    producto_class=Producto(request)
    producto=Productos.objects.get(id=producto_id)
    producto_class.agregar(producto)
    return render(request, "productos/descripcion_products.html", {"producto": producto}

def detalles(request):
    return render(request, "productos/descripcion_products.html")'''

# Vistas de productos favoritos:
def bolsocalavera(request):
    return render(request, "productos_d/bolsos/bolsocalavera.html")
def botasmarrones(request):
    return render(request, "productos_d/calzado/botasmarrones.html")
def monturadecuero(request):
    return render(request, "productos_d/monturas/monturadecuero.html")
def cascoargentina(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/cascoargentina.html", {"precio__dolar": int(precio__dolar)})

#Vistas de cascos:
def cascos(request):
    precio__dolar = precio_venta
    return render(request, "productos_d/cascos/cascos.html", {"precio__dolar": int(precio__dolar)})
def casprint(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/casprint.html", {"precio__dolar": int(precio__dolar)})
def cascosamarillos(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cas-amarillos.html", {"precio__dolar": int(precio__dolar)})
def cascoazul_f(request):
    precio__dolar = precio_venta*117      
    return render(request, "productos_d/cascos/casazul_f.html", {"precio__dolar": int(precio__dolar)})
def cascoazul_m(request):
    precio__dolar = precio_venta*120 
    return render(request, "productos_d/cascos/casazul_m.html", {"precio__dolar": int(precio__dolar)}) 
def CascoAzulyGris(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/casazulygris.html", {"precio__dolar": int(precio__dolar)})   
def CascoGris(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascogris.html", {"precio__dolar": int(precio__dolar)})
def cascobyn(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/cascobyn.html", {"precio__dolar": int(precio__dolar)})
def cascobordo(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascobordo.html", {"precio__dolar": int(precio__dolar)})   
def cascobrilloso(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/cascobrilloso.html", {"precio__dolar": int(precio__dolar)})
def cascocamuflado(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascocamuflado.html", {"precio__dolar": int(precio__dolar)})
def cascochina(request):
    precio__dolar = precio_venta*119
    return render(request, "productos_d/cascos/cascochina.html", {"precio__dolar": int(precio__dolar)})
def cascodegrade(request):
    precio__dolar = precio_venta*119
    return render(request, "productos_d/cascos/cascodegrade.html", {"precio__dolar": int(precio__dolar)})
def cascopastel(request):
    precio__dolar = precio_venta*128
    return render(request, "productos_d/cascos/cascopastel.html", {"precio__dolar": int(precio__dolar)})
def cascopastelverde(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascopastelv.html", {"precio__dolar": int(precio__dolar)})
def cascoflores(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/cascoflores.html", {"precio__dolar": int(precio__dolar)})
def cascogeometrico(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/cascogeometrico.html", {"precio__dolar": int(precio__dolar)})
def cascogrisclaro(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascogc.html", {"precio__dolar": int(precio__dolar)})
def cascogrisazulado(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/cascoga.html", {"precio__dolar": int(precio__dolar)})
def cascoleon(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascoleon.html", {"precio__dolar": int(precio__dolar)})
def cascogverde(request):
    precio__dolar = precio_venta*117
    return render(request, "productos_d/cascos/cascogeverde.html", {"precio__dolar": int(precio__dolar)})
def cascogyc(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascogyc.html", {"precio__dolar": int(precio__dolar)})
def cascomilitar(request):
    precio__dolar = precio_venta*119
    return render(request, "productos_d/cascos/cascomilitar.html", {"precio__dolar": int(precio__dolar)})
def cascolobo(request):
    precio__dolar = precio_venta*124
    return render(request, "productos_d/cascos/cascolobo.html", {"precio__dolar": int(precio__dolar)})
def cascostones(request):
    precio__dolar = precio_venta*124
    return render(request, "productos_d/cascos/cascostones.html", {"precio__dolar": int(precio__dolar)})
def cascoryb(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascoryb.html", {"precio__dolar": int(precio__dolar)})
def cascorosab(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascorosab.html", {"precio__dolar": int(precio__dolar)})
def cascotropical(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascotropical.html", {"precio__dolar": int(precio__dolar)})
def cascoverde(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascoverde.html", {"precio__dolar": int(precio__dolar)})
def cascovioleta(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/cascovioleta.html", {"precio__dolar": int(precio__dolar)})
def casconaranja(request):
    precio__dolar = precio_venta*120
    return render(request, "productos_d/cascos/casconaranja.html", {"precio__dolar": int(precio__dolar)})

# Calzado
def calzado(request):
    return render(request, "productos_d/calzado/calzado.html")
def botasmarrones(request):
    return render(request, "productos_d/calzado/botasmarrones.html")
def fundas(request):
    return render(request, "productos_d/calzado/fundas.html")

# Riendas y estribos
def estribos(request):
    return render(request, "productos_d/riendas_y_estribos/estribos.html")
def riendasnegras(request):
    return render(request, "productos_d/riendas_y_estribos/riendasnegras.html")
def riendasyestribos(request):
    return render(request, "productos_d/riendas_y_estribos/riendasestribos.html")
def riendas(request):
    return render(request, "productos_d/riendas_y_estribos/riendas_y_estribos.html")

# Monturas
def monturas(request):
    precio__dolar = precio_venta*230
    return render(request, "productos_d/monturas/monturas.html", {"precio__dolar": int(precio__dolar)})

# Bolsos
def bolsos(request):
    return render(request, "productos_d/bolsos/bolsos.html")

# Cinturones
def cinturones(request):
    return render(request, "productos_d/cinturones/cinturones.html")
def cinturon(request):
    precio__dolar = precio_venta*25
    return render(request, "productos_d/cinturones/cinturon.html", {"precio__dolar": int(precio__dolar)})
def sobresincha(request):
    precio__dolar = precio_venta*21
    return render(request, "productos_d/cinturones/sobresinchas.html", {"precio__dolar": int(precio__dolar)})    

# Rodilleras
def rodilleras(request):
    return render(request, "productos_d/rodilleras/rodilleras.html")
def rodillerasniño(request):
    return render(request, "productos_d/rodilleras/rodillerasniño.html")
def rodillerasadulto(request):
    return render(request, "productos_d/rodilleras/rodillerasadulto.html") 
def rodillerasmujer(request):
    return render(request, "productos_d/rodilleras/rodillerasmujer.html") 
def vendas(request):
    precio__dolar = precio_venta*14.5
    return render(request, "productos_d/bolsos/vendas.html", {"precio__dolar": float(precio__dolar)}) 








