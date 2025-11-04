from django.contrib import admin

from apps.modulo_4.asistencia.models import Asistencia

admin.site.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id_asistencia', 'id_inscripcion', 'fecha_clase', 'presente')
    search_fields = ('id_inscripcion__id_estudiante__usuario__nombre', 'fecha_clase')
    list_filter = ('presente', 'fecha_clase')
