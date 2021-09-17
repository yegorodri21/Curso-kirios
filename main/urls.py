from typing import ValuesView
from django.urls import path, include
from.import views 

app_name='main'

urlpatterns =[
    path('',views.homepage, name='homepage'),
    path ('registro/',views.registro, name="registro"),
    path ('logout/', views.logout_request, name="logout"),
    path ('login/', views.login_request, name ="login"),
    path ('curso_form/', views.curso_form,name="curso_form"),
]