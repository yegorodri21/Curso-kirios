from django.db import models
from datetime import datetime

class Curso(models.Model):
    curso_titulo=models.CharField(max_length=200)
    curso_contenido=models.TextField()
    curso_publicado=models.DateTimeField(
        "fecha de publicacion", default=datetime.now())
    foto=models.ImageField('albums', upload_to='albums', null=True)

    def __str__(self):
        return self.curso_titulo

class Registrom (models.Model):
    nombre=models.TextField(max_length=200)
    apellido=models.TextField(max_length=200)
    cedula=models.DecimalField(max_digits=15, decimal_places=14, default=0)
    materia=models.CharField(max_length=200)
    fecha=models.DateTimeField(
        "fecha de matricula", default=datetime.now())

    def __str__(self):
        return self.Cedula
