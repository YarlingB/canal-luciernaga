from django.db import models

# Create your models here.

class Programacion(models.Model):
    titulo = models.CharField(max_length = 225)
    link = models.URLField()
    hora = models.TimeField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name ="Programación"
        verbose_name_plural ="Programaciones"
        
    