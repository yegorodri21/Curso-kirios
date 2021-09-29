from django import forms
from  .models import Curso, Registrom


class NuevoCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class RegistromForm(forms.ModelForm):
    class Meta:
        model = Registrom
        fields = [
            'cedula',
            'fecha',
            

        ]
