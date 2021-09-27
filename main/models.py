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
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    cedula=models.CharField(max_length=10)
    materia=models.CharField(max_length=200)
    fecha=models.DateTimeField(
        "fecha de matricula", default=datetime.now())

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido, self.cedula, self.materia, self.fecha)

class Matriculados (models.Model):
    materia=models.CharField(max_length=200)
    cedula=models.CharField(max_length=10)
    fecha=models.DateTimeField(
        "fecha de matricula", default=datetime.now())

    def __str__(self):
        return self.Cedula
