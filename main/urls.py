from typing import ValuesView
from django.urls import path
from .import views 

app_name='main'

urlpatterns =[
    path('',views.homepage, name='homepage'),
    path ('registro/',views.registro, name="registro"),
    path ('logout/', views.logout_request, name="logout"),
    path ('login/', views.login_request, name ="login"),
    path ('curso_form/', views.curso_form,name="curso_form"),
    path ('registro_create/<int:pk>/', views.registro_create, name="registro_create"),

    # path ('materias/', views.materias,name="materias"),

]