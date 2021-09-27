from django.db import models
from main.models import Curso


# Create your models here.
class Matricula(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    fecha_inscripcion = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)   

    def __str__(self):
        return '%s %s' % (self.fecha_inscripcion, self.curso)