from django.db import models

# Create your models here.
class Programacion(models.Model):
    titulo = models.CharField(max_length = 225)
    link = models.URLField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Programación"
        verbose_name_plural = "Programaciones"

class HoraProgramacion(models.Model):
    programacion = models.ForeignKey(Programacion, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 225)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        verbose_name ="Hora Programación"
        verbose_name_plural ="Horas de programacion"
        
    