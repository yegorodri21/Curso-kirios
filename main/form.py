from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  .models import Curso, Registrom


class NuevoCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class Usuario(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',

        ]
        labels = {
            'username': 'Nombre de usuario', 

        }

class RegistromForm(forms.ModelForm):
    class Meta:
        model = Registrom
        fields = [
            'cedula',
            'fecha',
            

        ]
