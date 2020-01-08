from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage

from galeria.models import project
from servicios.models import Servicio
from cotizacion.models import Cliente
from cotizacion.models import Cotizacion

from contacto.forms import ContactoForm
from cotizacion.forms import CotizacionForm

# Create your views here.

def index(request):
    projects = project.objects.all()
    servicio = Servicio.objects.all()
    contact_form = ContactoForm(data=request.POST)
    cotizacion = CotizacionForm(data=request.POST)

    if cotizacion.is_valid():
        nombre_f = request.POST.get('nombre_c', '')
        apellido_f = request.POST.get('apellido', '')
        rut_f = request.POST.get('rut', '')
        empresa_f = request.POST.get('empresa', '')
        email_f = request.POST.get('email_c', '')
        servicio_f = request.POST.get('servicio', '')
        telefono_f = request.POST.get('telefono', '')


        try:
            b = Cliente(rut = rut_f,nombre = nombre_f,apellido = apellido_f,correo = email_f,telefono = telefono_f,empresa = empresa_f)
            c = Cotizacion(cliente=b,servicio=servicio_f ,estado=False)
            b.save()
            c.save()

            return redirect(reverse('home'))
        except:
            return redirect(reverse('home'))


    if contact_form.is_valid():
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        asunto = request.POST.get('asunto', '')
        mensaje = request.POST.get('mensaje', '')
        #Enviar Correo
        email = EmailMessage("Consulta: "+asunto,"De {} <{}\n\nEscribio:\n\n{}".format(nombre,email,mensaje),"no-contestar",["vicentemcvergara@gamil.com"],reply_to=[email])
        try:
            email.send()
            return redirect(reverse('home'))
        except:
            #Algo no ha ido bien
            return redirect(reverse('home'))



    return render(request,"base/index.html",{'projects': projects, 'form': contact_form, 'servicios':servicio, 'form_c': cotizacion})
