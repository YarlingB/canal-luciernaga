from django.db import models
from sorl.thumbnail import ImageField
from noticias.models import Categoria
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Biblioteca(models.Model):
    nombre = models.CharField(max_length = 225)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = RichTextUploadingField(verbose_name='Descripción')
    foto = ImageField('Imagen',upload_to='fotos/biblioteca')
    archivo = models.FileField(upload_to='documento/biblioteca')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Biblioteca"
        verbose_name_plural = "Biblioteca"