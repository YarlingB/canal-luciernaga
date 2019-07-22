from django.db import models
from django.utils.text import slugify
from lugar.models import Pais

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length = 255)
    
    class Meta:
         ordering = ['-id']

    def __str__(self):
        return self.nombre
    
   

class Categoria(models.Model):
    nombre = models.CharField(max_length = 255)

    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.nombre


class Director(models.Model):
    nombre = models.CharField(max_length = 255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ['-id']


class Video(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete = models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    nombre = models.CharField(max_length = 225)
    sinopsis = models.TextField()
    fecha = models.DateField() 
    director = models.ForeignKey(Director, on_delete = models.CASCADE)
    produccion = models.CharField(max_length = 255)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    duracion = models.TimeField()
    url = models.URLField(null = True, blank = True)
    slug = models.SlugField(max_length = 250, unique=True, editable= False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Video, self).save(*args, **kwargs)

TEMPORADAS_CHOICE = [
    (1, 'Temporada 1'),
    (2, 'Temporada 2'),
    (3, 'Temporada 3'),
    (4, 'Temporada 4'),
    (5, 'Temporada 5'),
]

class Temporada(models.Model):
    info_video = models.ForeignKey(Video, on_delete = models.CASCADE)
    temporada = models.IntegerField(choices = TEMPORADAS_CHOICE)

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

class Episodio(models.Model):
    temporada = models.ForeignKey(Temporada, related_name = 'episodio_temporada', on_delete = models.CASCADE)
    link = models.URLField(max_length = 225)
    titulo = models.CharField(max_length = 225)
    sinopsis = models.CharField(max_length = 225)
    duracion = models.TimeField()
    slug = models.SlugField(max_length=250, unique=True, editable= False)


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Episodio"
        verbose_name_plural = "Episodios"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Episodio, self).save(*args, **kwargs)



