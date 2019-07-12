from django.contrib import admin
from .models import Categoria, Clasificacion, Comunicacion, Tipo

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ClasificacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    autocomplete_fields = ['categoria']

class TipoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class ComunicacionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['clasificacion','tipo', 'categoria' ]

# Register your models here.
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Comunicacion, ComunicacionAdmin)