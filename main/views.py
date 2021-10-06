from django import forms
from django.core.files.base import File
from django.forms.forms import Form
from django.http import request
from main.form import NuevoCurso, RegistromForm, UsuarioForm
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
          form = UsuarioForm(request.POST)
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

    form = UsuarioForm()
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
               form.save()
               return redirect('main:homepage')

    return render(request,  "main/cursos.html", contexto)

def registro_create (request, curso_pk):
    
    usuario_form=UsuarioForm()
    registro_form = RegistromForm(prefix='form_registro') 

    contexto = {
        'usuario_form':usuario_form,
        'registro_form':registro_form
    }
    if request.method == 'POST': 
        usuario_form=UsuarioForm(request.POST)
        registro_form = RegistromForm(request.POST)
        
        if  usuario_form.is_valid() and registro_form.is_valid():
            estudiante = usuario_form.save(commit=False)
            estudiante.user = request.user
            estudiante.save()
            curso = Curso.objects.get(curso_pk = curso_pk)
            matricula = registro_form.save(commit=False)
            matricula.curso = curso
            matricula.save()
            return redirect('main:materias')
        else:
            print('Error en los forms')
            print(usuario_form.errors)
            print(registro_form.errors)
            messages.error(request, usuario_form.errors)
            messages.error(request, registro_form.errors)
            
    return render(request,'matricula/registroM.html', contexto) 
        
def modificar(request, id):

        registro = get_object_or_404(Registrom, id=id)
        data={
            'form': RegistromForm(instance=registro)
        }
        if request.method=='POST':
            formulario=RegistromForm(data=request.POST,instance=registro, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('main:materias')
            data["form"]=formulario
        return render(request, "matricula/modificar.html", data)

def eliminar(request, id):
    registro=get_object_or_404(Registrom,id=id)
    registro.delete()
    return redirect('main:materias')

def materias (request):
    materias =Registrom.objects.all()
    data={
        'materias':materias
    }
    return render (request,"matricula/materias.html",data)


    