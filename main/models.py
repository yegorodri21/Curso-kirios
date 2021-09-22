from django.db import models
from datetime import datetime
# Create your models here.
class Curso(models.Model):
    curso_titulo=models.CharField(max_length=200)
    curso_contenido=models.TextField()
    curso_publicado=models.DateTimeField(
        "fecha de publicacion", default=datetime.now())
    foto=models.ImageField('albums', upload_to='albums', null=True)
    # foto=models.ImageField(upload_to='albums', null=True)

    def __str__(self):
        return self.curso_titulo

