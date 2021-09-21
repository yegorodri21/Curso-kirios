from django import forms
from  .models import Curso


class NuevoCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

# class Materia(forms.Form):
#     Nombre=forms.CharField(label="Nombre", max_length=255, min_length=3, required=True)
#     Apellido=forms.CharField(label="Apellido", max_length=255, min_length=3, required=True)
#     Materia=forms.CharField(label="Materia", max_length=255, min_length=3, required=True)
#     Precio=forms.DecimalField(label="Precio",min_value=0.1)
