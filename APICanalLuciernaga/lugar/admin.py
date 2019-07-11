from django.contrib import admin
from .models import *

class PaisAdmin(admin.ModelAdmin):
    search_fields = ['nombre']


# Register your models here.
admin.site.register(Pais, PaisAdmin)