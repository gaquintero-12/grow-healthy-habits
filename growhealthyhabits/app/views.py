from django.shortcuts import render
from .models import Presupuesto,RutinaEjercicio,Tarea,Contacto
from .forms import ContactoForm,TareaForm,EjercicioForm,PresupuestoForm

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def presupuesto(request):
    presupuestos=Presupuesto.objects.all()
    data ={
        'presupuestos':presupuestos
    }
    return render(request,'app/presupuesto.html',data)

def ejercicio(request):
    return render(request,'app/ejercicio.html')

def tarea(request):
    return render(request,'app/tarea.html')

def contacto(request):
    data={
        'form':ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto enviado"
        else:
            data["form"]=formulario
    return render(request,'app/contacto.html',data)

def agregar_tarea(request):
    data={
        'form':TareaForm
    }

    if request.method == 'POST':
        formulario=TareaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Guardado correctamente"
        else:
            data["form"]=formulario
    return render(request, 'app/tarea/agregar_tarea.html',data)

def agregar_ejercicio(request):
    data={
        'form':EjercicioForm
    }
    if request.method == 'POST':
        formulario=TareaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Guardado correctamente"
        else:
            data["form"]=formulario
    return render(request, 'app/ejercicio/agregar_ejercicio.html',data)

def agregar_presupuesto(request):
    data={
        'form':PresupuestoForm
    }
    if request.method == 'POST':
        formulario=TareaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Guardado correctamente"
        else:
            data["form"]=formulario
    return render(request, 'app/presupuesto/agregar_presupuesto.html',data)