from django import forms
from  .models import Curso


class NuevoCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'