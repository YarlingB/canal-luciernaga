from django.contrib import admin
from .models import Tematicas, Noticias

class TematicasAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class NoticiasAdmin(admin.ModelAdmin):
    autocomplete_fields = ['tematica']

# Register your models here.
admin.site.register(Tematicas,TematicasAdmin)
admin.site.register(Noticias,NoticiasAdmin)