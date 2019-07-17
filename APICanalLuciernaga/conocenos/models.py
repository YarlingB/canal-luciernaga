from django.db import models

# Create your models here.

class Mision(models.Model):
    titulo = models.CharField(max_length = 255 )
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Misión"
        verbose_name = "Misión"

class Vision(models.Model):
    titulo = models.CharField(max_length = 255 )
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Vision"
        verbose_name = "Visión"


class Valor(models.Model):
    titulo = models.CharField(max_length = 255 )
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Valor"
        verbose_name = "Valor"



class Fundacion(models.Model):
    titulo = models.CharField(max_length = 255 )
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Fundación"
        verbose_name = "Fundaciones"
