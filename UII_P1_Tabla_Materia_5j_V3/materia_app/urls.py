from django.urls import path, include
from materia_app import views

urlpatterns = [
    path("",views.lasmaterias,name="lasmaterias"),
    path("registrarMateria/",views.registrarMateria,name="registrarMateria"),
    
]
