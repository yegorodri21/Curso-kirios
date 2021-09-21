from django.shortcuts import render

# Create your views here.
def matricula(request,):
    form = Resgistro_m (prefix='form_registro')
    
    