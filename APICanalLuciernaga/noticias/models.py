from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from lugar.models import Pais

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length =225)

    def __str__(self):
        return self.nombre

class Clasificacion(models.Model):
    nombre = models.CharField(max_length = 225)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nombre
        
class Tipo(models.Model):
    nombre = models.CharField(max_length = 225)

    def __str__(self):
        return self.nombre

class Comunicacion(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete = 225)
    titulo = models.CharField(max_length = 225)
    clasificacion = models.ForeignKey(Clasificacion, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    autor = models.CharField(max_length = 255)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='fotos/noticias')
    descripcion = models.CharField(max_length = 225)
    pais = models.ForeignKey(Pais, on_delete = 255)
    fuente = models.CharField(max_length = 225)
    ultimo_momento = models.BooleanField()
    tags = TaggableManager()
    slug = models.SlugField(max_length=250, unique=True, editable= False)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Comunicacion, self).save(*args, **kwargs)
    