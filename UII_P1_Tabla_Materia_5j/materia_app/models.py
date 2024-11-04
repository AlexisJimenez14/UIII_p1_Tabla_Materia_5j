from django.db import models

# Create your models here.
class Materia(models.Model): #creas modelo de tu tabla con tu campo
    nombre= models.CharField(primary_key=True, max_length=6) 
    codigo=models.CharField(max_length=50)
    creditos= models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
    