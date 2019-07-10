from django.db import models
from django.utils.text import slugify
from lugar.models import Pais

# Create your models here.

class Tipos(models.Model):
    nombre = models.CharField(max_length = 255)
    
    class Meta:
         ordering = ['-id']

    def __str__(self):
        return self.nombre
    
   

class Categorias(models.Model):
    nombre = models.CharField(max_length = 255)

    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.nombre


class Directores(models.Model):
    nombre = models.CharField(max_length = 255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Videos(models.Model):
    tipo = models.ForeignKey(Tipos, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 225)
    sinopsis = models.CharField(max_length = 225)
    fecha = models.DateField()
    director = models.ForeignKey(Directores, on_delete = models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    url = models.URLField(null = True, blank = True)
    slug = models.SlugField(max_length = 250, unique=True, editable= False)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Videos, self).save(*args, **kwargs)

TEMPORADAS_CHOICE = [
    (1, 'Temporada 1'),
    (2, 'Temporada 2'),
    (3, 'Temporada 3'),
    (4, 'Temporada 4'),
    (5, 'Temporada 5'),
]

class Temporadas(models.Model):
    info_video = models.ForeignKey(Videos, on_delete = models.CASCADE)
    temporada = models.IntegerField(choices = TEMPORADAS_CHOICE)

class Episodios(models.Model):
    temporada = models.ForeignKey(Temporadas, related_name = 'episodio_temporada', on_delete = models.CASCADE)
    link = models.URLField(max_length = 225)
    titulo = models.CharField(max_length = 225)
    sinopsis = models.CharField(max_length = 225)
    slug = models.SlugField(max_length=250, unique=True, editable= False)


    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Episodios, self).save(*args, **kwargs)



