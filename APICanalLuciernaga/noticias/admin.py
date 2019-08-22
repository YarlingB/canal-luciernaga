from django.contrib import admin
from .models import *
from lugar.models import Pais

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

# class ClasificacionAdmin(admin.ModelAdmin):
#     search_fields = ['nombre']
    
class PaisAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ComunicacionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['categoria','pais' ]
    
    class Media:
        js = ('js/noticia/check.js',)

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
# admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Comunicacion, ComunicacionAdmin)