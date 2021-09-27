from django.contrib import admin
from .models import Matricula

# Register your models here.
class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombres',
        'apellidos',
        'fecha_Matricula',
        'curso',
        )

admin.site.register(Matricula, MatriculaAdmin)