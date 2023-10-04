from django.db import models

# Create your models here.
class Presupuesto(models.Model):
    tipo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    monto=models.IntegerField()
    metaMonto=models.IntegerField()
    metaFecha=models.DateTimeField()  
    imagen=models.ImageField(upload_to="movimientos", null=True)
    ingresos=models.IntegerField()
    egresos=models.IntegerField()

    def __str__(self):
        return self.descripcion

class Tarea(models.Model):
    nombre=models.CharField(max_length=50)
    Materia=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    diaEntrega=models.DateTimeField()
    imagen=models.ImageField(upload_to="evidencias", null=True)
    
    
    def __str__(self):
        return self.nombre

class RutinaEjercicio(models.Model):
    nombre=models.CharField(max_length=50)
    repeticiones=models.IntegerField()
    series=models.IntegerField()
    peso=models.IntegerField()
    imagen=models.ImageField(upload_to="ejemplos", null=True)

    def __str__(self):
        return self.nombre
    
opciones_consultas=[
    [0, "consulta"],
    [1,"reclamo"],
    [2,"felicitaciones"]
]

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta= models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()
    avisos=models.BooleanField()

    def __str__(self):
        return self.nombre