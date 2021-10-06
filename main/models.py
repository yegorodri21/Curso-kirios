from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.base import Model

class Curso(models.Model):
    curso_titulo=models.CharField(max_length=200)
    curso_contenido=models.TextField()
    curso_publicado=models.DateTimeField(
        "fecha de publicacion", default=datetime.now())
    foto=models.ImageField('albums', upload_to='albums', null=False)

    def __str__(self):
        return self.curso_titulo

class Registrom (models.Model):
    cedula=models.CharField(max_length=10)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE, null=True)
    estudiante=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    fecha=models.DateTimeField(
        "fecha de matricula", default=datetime.now())
    costo=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '%s %s %d' % ( self.cedula, self.fecha, self.costo)