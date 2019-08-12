from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 225)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Biblioteca(models.Model):
    nombre = models.CharField(max_length = 225)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.TextField(max_length = 255)
    foto = ImageField('Imagen',upload_to='fotos/biblioteca')
    archivo = models.FileField(upload_to='documento/biblioteca')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Biblioteca"
        verbose_name_plural = "Biblioteca"