from django.urls import path, include
from materia_app import views

urlpatterns = [
    path("",views.lasmaterias,name="lasmaterias"),
    path("registrarMateria/",views.registrarMateria,name="registrarMateria"),
    path("seleccionarMateria/<codigo>",views.seleccionarMateria,name="seleccionarMateria"),
    path("editarMateria/", views.editarMateria, name="editarMateria"),
    path("borrarMateria/<codigo>",views.borrarMateria,name="borrarMateria"),
    
]
