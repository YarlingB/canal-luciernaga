from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Create your models here.

class Tematicas(models.Model):
    nombre = models.CharField(max_length =225)

    def __str__(self):
        return self.nombre

class Noticias(models.Model):
    titulo = models.CharField(max_length = 225)
    tematica = models.ManyToManyField(Tematicas)
    autor = models.CharField(max_length = 255)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='fotos/noticias')
    descripcion = models.CharField(max_length = 225)
    tags = TaggableManager()
    slug = models.SlugField(max_length=250, unique=True, editable= False)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.Titulo)
        super(Noticias, self).save(*args, **kwargs)