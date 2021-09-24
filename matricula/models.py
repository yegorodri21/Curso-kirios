from django.db import models
from datetime import datetime

# Create your models here.

class registroM (models.Model):
    Nombre=models.TextField()
    Apellido=models.TextField()
    Cedula=models.DecimalField()
    Materia=models.CharField(max_length=200)
    Fecha_matricula=models.DateTimeField(
        "fecha de matricula", default=datetime.now())
    Correo=models.models.EmailField(_(""), max_length=254)

    def __str__(self):
        return self.Cedula