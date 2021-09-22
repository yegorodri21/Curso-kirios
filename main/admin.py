from django.contrib import admin
from django.forms import widgets
from .models import Curso
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class CursoAdmin(admin.ModelAdmin): 
    fields=("curso_publicado",
    "curso_contenido",
    "curso_titulo",
    "foto",
    )
    # fieldsets=[
    #     ("Titulo/fecha", {"fields":["curso_titulo","curso_publicado"]}),
    #     ("Contenido", {"fields":["curso_contenido"]}),
    # ]

    # forma chingona de cuadro de texto
    # formfield_overrides={
    #     models.TextField:{'widget': TinyMCE()}
    # }
    def foto(self, obj):
        return "<img src="+ obj.foto.url+"/>"
admin.site.register(Curso,CursoAdmin)