from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.PositiveIntegerField(blank=True)
    empresa = models.CharField(max_length=200)


    @classmethod
    def create(cls, rut, nombre,apellido, correo, telefono,empresa, servicio):
        cliente = cls(rut=rut, nombre=nombre, correo=correo, telefono=telefono,empresa=empresa,servicio=servicio)
        return cliente
    def __str__(self):
        return str(self.rut)+" "+self.nombre+" "+slef.apellido

class Cotizacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=200, default='default')
    estado = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"

    def __str__(self):
        return self.cliente
