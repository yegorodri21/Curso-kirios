from django.db import models
from datetime import datetime

# Create your models here.

class registroM (models.Model):
    Materia=models.CharField(max_length=200)
    Nombre=models.TextField()
    Apellido=models.TextField()
    Precio=models.CharField(max_length=50)
    Fecha_matricula=models.DateTimeField(
        "fecha de matricula", default=datetime.now())

    def __str__(self):
        return self.curso_titulo