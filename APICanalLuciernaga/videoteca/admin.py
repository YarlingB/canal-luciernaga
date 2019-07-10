from django.contrib import admin
from .models import Videos, Directores, Tipos, Categorias, Episodios, Temporadas
import nested_admin
from django import forms

class EpisodiosInline(nested_admin.NestedTabularInline):
    model = Episodios
    extra = 1

class TemporadasInline(nested_admin.NestedStackedInline):
    model = Temporadas
    extra = 1
    inlines = [EpisodiosInline]

class VideosAdmin(nested_admin.NestedModelAdmin):
    inlines = [TemporadasInline]

 
# Register your models here.
admin.site.register(Tipos)
admin.site.register(Categorias)
admin.site.register(Directores)
admin.site.register(Videos,VideosAdmin)  