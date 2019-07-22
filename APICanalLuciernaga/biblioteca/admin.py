from django.contrib import admin
from .models import Biblioteca, Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class BibliotecaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['categoria']

admin.site.register(Biblioteca,BibliotecaAdmin)
admin.site.register(Categoria,CategoriaAdmin)