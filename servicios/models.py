from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagenPequeña =models.ImageField(upload_to="servicios") #700x400

    def __str__(self):
        return self.titulo
