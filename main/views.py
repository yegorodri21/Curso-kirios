from django import forms
from django.core.files.base import File
from django.forms.forms import Form
from django.http import request
from main.form import NuevoCurso, RegistromForm, Usuario
from .models import Registrom
import main
from .models import Curso
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Curso

# Create your views here.
def homepage (request):
    return render (request, "main/inicio.html", {"cursos": Curso.objects.all})

def registro(request):
     
    if request.method =="POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
               usuario = form.save()
               nombre_usuario = form.cleaned_data.get('username')
               messages.success(request, f"Nueva Cuenta Creada: {nombre_usuario}")
               login(request, usuario)
               messages.info(request, f"Has sido logeado como: {nombre_usuario}")
               return redirect("main:homepage")
          else:
               for msg in form.error_messages:
                    messages.error(request, f"{msg}: form.error_messages[msg]")

    form = UserCreationForm()
    return render(request, "main/registro.html", {"form": form})
        
def logout_request(request):
    logout (request)
    messages.info (request,"Saliste exitosamente")
    return redirect("main:homepage")

def login_request(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get ('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request,user)
                messages.info(request, f"Estas logeado como{usuario}")
                return redirect ("main:homepage")
            else:
                messages.error(request, "Usuario o contraseña equivocado")
        else:
            messages.error(request,"Usuario o contraseña equivocada")

    form= AuthenticationForm ()
    return render(request, "main/login.html",{"form":form})

def curso_form(request):
    if request.method == 'GET':
        form = NuevoCurso
        contexto = {
        'form' : form
        }
    else:
        form = NuevoCurso(request.POST, request.FILES)
        contexto = {
        'form' : form
        }
        if form.is_valid():
               curso_form=form.save()
               return redirect('main:homepage')

    return render(request,  "main/cursos.html", contexto)

def registro_create(request, pk):

    contexto={
        'form': Registrom()
    }
    if request.method=='POST':
        formulario=Registrom(contexto=request.POST, files =request.FILES)
        if formulario.is_valid():
            formulario.save()
            contexto["mensaje"]="Matriculado con exito"
        else:
            contexto["form"]=formulario
            
    # if request.method=='POST':
    #     registro = Usuario(request.POST)
    #     registro_form = RegistromForm(request.POST, prefix='form_inscripcion')
    #     if forms.is_valid():
    #         estudiante=Form.save()
    #         RegistromForm=form_registro.cleaned_data.get('Estudiante')
    #         messages.success(request, f"Estudiante registrado : {registroM}")
    #         return redirect("main:homepage")
    # else:
    #      contexto = {
    #     'user_form':Usuario,
    #     'registro_form':RegistromForm
       
    #     }
    #     form = RegistromForm()
  
    return render(request, "matricula/registroM.html", contexto)


def modificar(request, id):

        registro = get_object_or_404(Registrom, id=id)
        data={
            'form_registro': RegistromForm(instance=registro),
        }
        if request.method=='POST':
            formulario=RegistromForm(data=request.POST,instance=registro, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="modificar")
            data["form"]=formulario

        return render(request, "matricula/modificar.html", data)

def eliminar(request, id):
    registro=get_object_or_404(Registrom,id=id)
    registro.delete()
    return redirect (to="eliminar")

def materias (request):
    materias =Registrom.object.all()
    data={
        'materias':materias
    }
    return render (request,"matricula/materias.html",data)