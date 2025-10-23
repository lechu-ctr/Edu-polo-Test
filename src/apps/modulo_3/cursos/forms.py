from django import forms
from .models import Curso, Comision, Material
# Importamos el modelo Usuario para poder filtrar por docentes
from gestion_usuarios.models import Usuario, Rol

class CursoForm(forms.ModelForm):
    """Formulario para el modelo Curso."""
    class Meta:
        model = Curso
        fields = [
            'nombre', 
            'descripcion', 
            'edad_minima', 
            'requisitos', 
            'contenido_multimedia', 
            'estado'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'requisitos': forms.Textarea(attrs={'rows': 3}),
        }

class ComisionForm(forms.ModelForm):
    """Formulario para el modelo Comision."""
    class Meta:
        model = Comision
        fields = [
            'fk_id_curso',
            'dias_horarios',
            'lugar',
            'fecha_inicio',
            'fecha_fin',
            'cupo_maximo',
            'estado'
        ]
        # Para usar un selector de fecha en los campos de fecha
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'dias_horarios': forms.Textarea(attrs={'rows': 2}),
        }

class MaterialForm(forms.ModelForm):
    """Formulario para subir materiales."""
    class Meta:
        model = Material
        fields = ['nombre_archivo', 'descripcion', 'archivo']

class ImportarCursosForm(forms.Form):
    """Formulario simple para subir el archivo Excel."""
    archivo_excel = forms.FileField(label="Seleccionar archivo .xlsx")

class AsignacionDocenteForm(forms.Form):
    """Formulario para asignar un docente a una comisión."""
    
    # Obtenemos el Rol 'Docente'
    try:
        rol_docente = Rol.objects.get(nombre='Docente')
        # Creamos un queryset solo con usuarios que tengan el rol de Docente
        queryset_docentes = Usuario.objects.filter(fk_id_rol=rol_docente)
    except Rol.DoesNotExist:
        # Si el rol no existe, el queryset estará vacío para evitar errores
        queryset_docentes = Usuario.objects.none()

    docente = forms.ModelChoiceField(
        queryset=queryset_docentes,
        label="Seleccionar Docente"
    )
