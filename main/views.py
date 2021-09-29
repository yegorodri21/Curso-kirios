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

    user_form = Usuario(prefix='form_user')
    registro_form = RegistromForm(prefix='form_registro') 
  
    contexto = {
        'user_form':Usuario,
        'registro_form':RegistromForm
       
    }

    if request.method == 'POST':
        user_form = Usuario(request.POST, prefix='form_registro')
        registro_form = RegistromForm(request.POST, prefix='form_inscripcion')
        
        if user_form.is_valid() and registro_form.is_valid():
            estudiante = user_form.save(commit=False)
            estudiante.user = request.user
            estudiante.save()
            curso = Curso.objects.get(pk = pk)
            matricula = registro_form.save(commit=False)
            matricula.curso = curso
            matricula.estudiante = estudiante
            matricula.save()
            return redirect('inscripciones:lista_estudiantes')
        else:
            print('Error en los forms')
            print(registro_form.errors)
            messages.error(request, user_form.errors)
            messages.error(request, registro_form.errors)
            
    return render(request,'matricula/registroM.html', contexto) 

    # if request.method=='POST':
    #     registro = RegistromForm(request.POST)

    #     if forms.is_valid():
    #         estudiante=Form.save()
    #         RegistromForm=form_registro.cleaned_data.get('Estudiante')
    #         messages.success(request, f"Estudiante registrado : {registroM}")
    #         return redirect("main:homepage")
    # else:
    #     contexto={
    #         'form_registro': form_registro,
    #         'form_estudiante': form_estudiante,
    #     }
    #     form = RegistromForm()
  
    # return render(request, "matricula/registroM.html", contexto)


def modificar(request, id):

        registro = get_object_or_404(Registrom, id =id)
        # estudiante= 
        contexto={
            'form_registro': RegistromForm(instance=registro),
            'form_estudiante': form_estudiante(instance=estudiante),
        }
        form = RegistromForm()
  
        return render(request, "matricula/registroM.html", contexto)