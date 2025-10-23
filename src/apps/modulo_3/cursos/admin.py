from django.contrib import admin
from .models import Curso, Comision, ComisionDocente, Material

# Inline para poder asignar docentes directamente desde la Comision
class ComisionDocenteInline(admin.TabularInline):
    model = ComisionDocente
    extra = 1  # Cuántos campos vacíos mostrar

class ComisionAdmin(admin.ModelAdmin):
    list_display = ('id_comision', 'fk_id_curso', 'lugar', 'fecha_inicio', 'estado')
    list_filter = ('estado', 'lugar', 'fk_id_curso')
    search_fields = ('fk_id_curso__nombre',)
    inlines = [ComisionDocenteInline] # Aquí conectamos el Inline

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'edad_minima')
    search_fields = ('nombre',)
    list_filter = ('estado',)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre_archivo', 'fk_id_comision', 'fk_id_docente', 'fecha_subida')
    list_filter = ('fk_id_comision',)
    search_fields = ('nombre_archivo', 'fk_id_comision__fk_id_curso__nombre')

# Registramos los modelos en el sitio de administración
admin.site.register(Curso, CursoAdmin)
admin.site.register(Comision, ComisionAdmin)
admin.site.register(Material, MaterialAdmin)
