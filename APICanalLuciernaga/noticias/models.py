from django.db import models
from django.utils.text import slugify


# Create your models here.
class Noticias(models.Model):
    titulo = models.CharField(max_length = 225)
    descripcion = models.CharField(max_length = 225)
    fecha = models.DateField()
    slug = models.SlugField(max_length=250, unique=True, editable= False)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.Titulo)
        super(Noticias, self).save(*args, **kwargs)