from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 225)

class Biblioteca(models.Model):
    nombre = models.CharField(max_length = 225)
    categoria = models.ForeignKey(Categoria)
    descripcion = models.CharField(max_length = 255)
    foto = models.ImageField(upload_to='fotos/noticias')
    archivo = models.FileField(upload_to='documento/biblioteca', max_length=100, null=True, blank=True)