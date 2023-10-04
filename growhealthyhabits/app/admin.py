from django.contrib import admin
from .models import Presupuesto,Tarea, RutinaEjercicio,Contacto
# Register your models here.

class PresupuestoAdmin(admin.ModelAdmin):
    list_editable=["monto"]
    list_display=["monto"]
    search_fields=["tipo"]
    list_filter=["monto"]
    list_per_page=3


admin.site.register(Presupuesto)
admin.site.register(Tarea)
admin.site.register(RutinaEjercicio)
admin.site.register(Contacto)