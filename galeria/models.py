from django.db import models

# Create your models here.

class project(models.Model):

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagenPequeña =models.ImageField(upload_to="galeria") #Definir tamaño
    imagenGrande = models.ImageField(upload_to="galeria") #Definir tamaño
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-creacion"]

    def __str__(self):
        return self.titulo
