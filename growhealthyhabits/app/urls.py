from django.urls import path
from .views import index,tarea,presupuesto,ejercicio,contacto,agregar_tarea,agregar_ejercicio,agregar_presupuesto

urlpatterns = [
    path('', index,name="index"),
    path('presupuesto/', presupuesto,name="presupuesto"),
    path('ejercicio/', ejercicio,name="ejercicio"),
    path('tarea/', tarea,name="tarea"),
    path('contacto/', contacto,name="contacto"),
    path('agregar_tarea/', agregar_tarea,name="agregar_tarea"),
    path('agregar_ejercicio/', agregar_ejercicio,name="agregar_ejercicio"),
    path('agregar_presupuesto/', agregar_presupuesto,name="agregar_presupuesto"),
]