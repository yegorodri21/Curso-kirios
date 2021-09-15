from django import forms
import main
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .models import Curso

# Create your views here.
def homepage (request):
    return render (request, "main/inicio.html", {"cursos": Curso.objects.all})


def registro (request):
    form = UserCreationForm(request.POST)
    
    if request.method=="POST":
        if form.is_valid():
            usuario=form.save()
        login(request, usuario)
        return redirect("main:homepage")
    else:
        for msg in form.error_messages:
            print(form.error_messages[msg])

        form = UserCreationForm
        return render (request, "main/registro.html", {"form":form})
