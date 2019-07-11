from django.contrib import admin
from .models import Videos, Directores, Tipos, Categorias, Episodios, Temporadas
from lugar.models import Pais
import nested_admin


class TiposAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    
class DirectoresAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class CategoriasAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class EpisodiosInline(nested_admin.NestedTabularInline):
    model = Episodios
    extra = 1

class TemporadasInline(nested_admin.NestedStackedInline):
    model = Temporadas
    extra = 1
    inlines = [EpisodiosInline]


class VideosAdmin(nested_admin.NestedModelAdmin):
    autocomplete_fields = ['tipo','director','categoria', 'pais']
    inlines = [TemporadasInline]

    

# Register your models here.
admin.site.register(Tipos,TiposAdmin)
admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Directores,DirectoresAdmin) 
admin.site.register(Videos,VideosAdmin)  