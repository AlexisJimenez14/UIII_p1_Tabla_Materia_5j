from django.shortcuts import render
from .models import Materia
# Create your views here.
def lasmaterias(request):
    losaviones=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"misaviones":losaviones})