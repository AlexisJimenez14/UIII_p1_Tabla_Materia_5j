from django.shortcuts import render,redirect
from .models import Materia
from django.shortcuts import get_object_or_404# Create your views here.
def lasmaterias(request):
    lasmaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"mismaterias":lasmaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    
    guardarmateria=Materia.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    )# guardar el registro
    
    return redirect("/")




def seleccionarMateria(request, codigo):
    materia = get_object_or_404(Materia, codigo=codigo)
    return render(request, "editarMateria.html", {"mismaterias": materia})


def editarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save() #registro acutalidado
    return redirect("/")
    
def borrarMateria(request, codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete() #borra el registro
    return redirect("/")