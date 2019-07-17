from django.contrib import admin
from .models import Programacion, HoraProgramacion

# Register your models here.
class HoraProgramacionInline(admin.StackedInline):
    model = HoraProgramacion
    extra = 1

class ProgramacionAdmin(admin.ModelAdmin):
    inlines = [HoraProgramacionInline,]

admin.site.register(Programacion, ProgramacionAdmin)