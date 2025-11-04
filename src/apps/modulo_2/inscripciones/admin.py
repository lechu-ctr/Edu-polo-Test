from django.contrib import admin

from apps.modulo_2.inscripciones.models import Inscripcion



admin.site.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'id_estudiante', 'id_comision', 'id_curso', 'fecha_inscripcion', 'estado')
    search_fields = ('id_estudiante__usuario__nombre', 'id_curso__nombre')
    list_filter = ('estado', 'fecha_inscripcion')