from django import forms
from .models import Docente

# Importamos los modelos de Persona, Usuario y Rol del Módulo 1
from apps.modulo_1.usuario.models import Persona, Usuario
from apps.modulo_1.roles.models import Rol

class DocenteForm(forms.ModelForm):
    """
    Formulario combinado para crear y editar Docentes.
    Maneja campos del modelo 'Docente' y del modelo 'Persona'.
    """
    
    # --- Campos del modelo 'Persona' ---
    # Los definimos manualmente aquí
    dni = forms.IntegerField(label="DNI")
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    correo = forms.EmailField(label="Correo Electrónico")
    telefono = forms.CharField(label="Teléfono", required=False)
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.CharField(label="Género", required=False)
    domicilio = forms.CharField(label="Domicilio", required=False)

    class Meta:
        model = Docente # El formulario se basa en tu modelo 'Docente'
        fields = ['especialidad', 'experiencia'] # Campos de tu modelo
        widgets = {
            'experiencia': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        """
        Sobrescribimos el __init__ para rellenar los campos de 'Persona'
        cuando estamos editando (cuando se pasa un 'instance').
        """
        super().__init__(*args, **kwargs)
        
        # Si estamos editando (self.instance.pk existe)
        if self.instance and self.instance.pk:
            # Rellenamos los campos de Persona
            persona = self.instance.fk_id_usuario.fk_id_persona
            self.fields['dni'].initial = persona.dni
            self.fields['nombre'].initial = persona.nombre
            self.fields['apellido'].initial = persona.apellido
            self.fields['correo'].initial = persona.correo
            self.fields['telefono'].initial = persona.telefono
            self.fields['fecha_nacimiento'].initial = persona.fecha_nacimiento
            self.fields['genero'].initial = persona.genero
            self.fields['domicilio'].initial = persona.domicilio

    def save(self, commit=True):
        """
        Sobrescribimos el 'save' para manejar los 3 modelos:
        1. Guardar/Actualizar 'Persona'
        2. Guardar/Actualizar 'Usuario' (asignando el Rol)
        3. Guardar/Actualizar 'Docente' (el perfil)
        """
        
        # Obtenemos los datos de Persona del formulario
        datos_persona = {
            'dni': self.cleaned_data['dni'],
            'nombre': self.cleaned_data['nombre'],
            'apellido': self.cleaned_data['apellido'],
            'correo': self.cleaned_data['correo'],
            'telefono': self.cleaned_data.get('telefono'),
            'fecha_nacimiento': self.cleaned_data['fecha_nacimiento'],
            'genero': self.cleaned_data.get('genero'),
            'domicilio': self.cleaned_data.get('domicilio'),
        }

        # 1. Guardar/Actualizar Persona
        if self.instance and self.instance.pk:
            # Estamos actualizando
            Persona.objects.filter(pk=self.instance.fk_id_usuario.fk_id_persona_id).update(**datos_persona)
            persona = self.instance.fk_id_usuario.fk_id_persona
        else:
            # Estamos creando
            persona = Persona.objects.create(**datos_persona)

        # 2. Guardar/Actualizar Usuario
        try:
            rol_docente = Rol.objects.get(nombre='Docente')
        except Rol.DoesNotExist:
            raise Exception("El Rol 'Docente' no existe. Pide al Módulo 1 que lo cree.")

        usuario, created = Usuario.objects.update_or_create(
            fk_id_persona=persona,
            defaults={
                'fk_id_rol': rol_docente,
                'contraseña': 'temporal_pass_123' if created else Usuario.objects.get(fk_id_persona=persona).contraseña
            }
        )
        
        # 3. Guardar/Actualizar Docente (el perfil)
        # Obtenemos el perfil 'Docente' que se está guardando
        docente = super().save(commit=False)
        docente.fk_id_usuario = usuario # Asignamos el usuario
        
        if commit:
            docente.save()
            
        return docente
