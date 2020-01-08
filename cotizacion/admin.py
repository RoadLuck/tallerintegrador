from django.contrib import admin
from .models import Cliente, Cotizacion
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('rut', 'nombre','apellido','correo','telefono','empresa')

class CotizacionAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'servicio' ,'cliente')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)

# Register your models here.
