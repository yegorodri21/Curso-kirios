from django import forms
from  .models import Curso, Registrom, Matriculados


class NuevoCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = Registrom
        fields = [
            'nombre',
            'apellido',
            'cedula',
            'materia',
            'fecha',

        ]

class Matriculados(forms.ModelForm):
    class Meta:
        model = Matriculados
        fields = [
            'materia',
            'cedula',
            'fecha',

        ]
        