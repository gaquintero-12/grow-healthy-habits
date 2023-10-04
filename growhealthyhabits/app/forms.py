from django import forms
from .models import Contacto,Tarea,RutinaEjercicio,Presupuesto


class ContactoForm(forms.ModelForm):

    #nombre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model= Contacto
        #fields=["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields='__all__'

        

class TareaForm(forms.ModelForm):
    class Meta:
        model= Tarea
        fields= '__all__'
        widgets={
            "diaEntrega":forms.SelectDateWidget()
        }

class EjercicioForm(forms.ModelForm):
    class Meta:
        model= RutinaEjercicio
        fields= '__all__'

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model= Presupuesto
        fields= '__all__'