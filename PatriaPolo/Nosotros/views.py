
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import NosotrosForm
from django.core.mail import EmailMessage

# Create your views here.

'''def nosotros(request):
    form_var = NosotrosForm()
    # Indicamos donde se va a guardar la información pasada al formulario:
    if request.method == "POST": # Si el método usado es igual a POST:
        form_var = NosotrosForm(data=request.POST) # Y que si 'NosotrosForm' utiliza dicho método:
        if form_var.is_valid(): # Y si nuestro formulario es válido:
            nombre=request.POST.get("nombre") #Que me traiga del formulario lo que haya en el campo del nombre. 
            apellido=request.POST.get("apellido") # El apellido, email, etc.
            email=request.POST.get("email")
            telefono=request.POST.get("telefono")
            mensaje=request.POST.get("mensaje")

            # Mandaremos al email la info:
            email=EmailMessage( "Mensaje desde Alonisia web",
                f"El usuario con nombre: {nombre} {apellido}, con la dirección: {email}, de telefono: {telefono},  manda el siguiente mensaje: {mensaje}"
                ,"", ["patriapolo@gmail.com"], reply_to=[email]
            )

            try:
                email.send()
                # Si todo es correcto que me redirrecione a una url igual pero con el parametro 'valido'.
                # Con ? se pasan parametros a una url.
                return redirect("/nosotros/?valido")
            except:
                return redirect("/nosotros/?novalido")

    return render(request, "nosotros/nosotros.html", {'mi_formulario':form_var})'''

def nosotros(request):
    return render(request, "nosotros/nosotros.html")