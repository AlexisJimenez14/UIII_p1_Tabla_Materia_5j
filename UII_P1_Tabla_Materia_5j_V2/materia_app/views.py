from django.shortcuts import render
from .models import Materia
# Create your views here.
def lasmaterias(request):
    lasmaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"mismaterias":lasmaterias})