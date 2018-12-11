from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut =
    nombre =
    correo =
    telefono =
    empresa = 

class Cotizacion(models.Model):
    numero =
    fecha =
    cliente =
    servicio =
    estado =

class Empleado(models.Model):
    rut =
    nombre =
    correo =
    telefono =
    usuario =
    contraseña =
