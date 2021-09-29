from django.contrib import admin
from django.forms import widgets
from .models import Curso, Registrom
from tinymce.widgets import TinyMCE
from django.utils.html import format_html
from django.db import models

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin): 
    list_display=(
        'id',
        "curso_publicado",
    "curso_contenido",
    "curso_titulo",
    "foto",
    )


@admin.register(Registrom)
class RegistromAdmin(admin.ModelAdmin):
    '''Admin View for Registrom'''

    list_display = ('id',
    'curso',
    'estudiante',
    'fecha',)
    