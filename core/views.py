from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage

from galeria.models import project
from servicios.models import Servicio
from contacto.forms import ContactoForm

# Create your views here.

def index(request):

    projects = project.objects.all()
    servicio = Servicio.objects.all()
    contact_form= ContactoForm()
    if request.method == "POST":
        contact_form = ContactoForm(data=request.POST)
        if contact_form.is_valid():
            nombre = request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            asunto = request.POST.get('asunto', '')
            mensaje = request.POST.get('mensaje', '')
            #Enviar Correo
            email = EmailMessage("Consulta: "+asunto,"De {} <{}\n\nEscribio:\n\n{}".format(nombre,email,mensaje),"no-contestar",["vicentemcvergara@gamil.com"],reply_to=[email])
            try:
                email.send()
                return redirect(reverse('home')+"?ok")
            except:
                #Algo no ha ido bien
                return redirect(reverse('home')+"?fail")

    return render(request,"base/index.html",{'projects': projects, 'form': contact_form, 'servicios':servicio})
