from django.contrib import admin
from .models import Curso, Estudiante, Asistencia, Egreso
# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Asistencia)
admin.site.register(Egreso)