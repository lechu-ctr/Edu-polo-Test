from django.db import models
from apps.modulo_1.usuario.models import Usuario, Persona
from django.contrib.auth.models import Group

# Create your models here.
class Rol(models.Model):
    jerarquias = [
        (1, "Administrador"),
        (2, "Coordinador"),
        (3, "Mesa de Entrada"),
        (4, "Docente"),
        (5, "Estudiante"),
    ]

    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)
    jerarquia = models.PositiveSmallIntegerField(choices=jerarquias)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(jerarquia__gte=1) & models.Q(jerarquia__lte=5),
                name="rol_jerarquia_entre_1_y_5"
            )
        ]
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def save(self, *args, **kwargs):
        if not self.group:
            grupo, _ = Group.objects.get_or_create(name=self.nombre)
            self.group = grupo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} (Jerarquía {self.jerarquia})"
        
class Docente(models.Model):
    especialidad = models.CharField(max_length=100)
    experiencia = models.TextField()
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"{self.id_persona.nombre} - Especialidad {self.especialidad}"

class Estudiante(models.Model):
    grado = [
        ('PR', 'Primaria'),
        ('SE', 'Secundaria'),
        ('UN', 'Universidad'),
        ('OT', 'Otro'),
    ]

    ciudad_residencia = [
        ('USH', 'Ushuaia'),
        ('RGA', 'Río Grande'),
        ('TLH', 'Tolhuin'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel_estudios = models.CharField(choices=grado)
    institucion_actual = models.CharField(max_length=255)
    experiencia_laboral = models.TextField(blank=True, null=True)
    ciudad_residencia = models.CharField(choices=ciudad_residencia)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"Estudiante: {self.usuario.persona.nombre} {self.usuario.persona.apellido}"

class Tutor(models.Model):
    tipo = [
        ('AC', 'Academico'),
        ('PE', 'Personal'),
        ('LA', 'Laboral'),
        ('OT', 'Otro'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_tutor = models.CharField(choices=tipo)
    telefono_contacto = models.CharField(max_length=15)
    disponibilidad_horaria = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    def __str__(self):
        return f"Tutor: {self.usuario.persona.nombre} {self.usuario.persona.apellido}"

class TutorEstudiante(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)
    observacion = models.TextField(null=True)

    def __str__(self):
        return f"Tutor: {self.tutor.usuario.persona.nombre} - Estudiante: {self.estudiante.usuario.persona.nombre}"
    
    class Meta:
        verbose_name = "Tutor/Estudiante"
        verbose_name_plural = "Tutor/Estudiante"
        unique_together = ('tutor', 'estudiante')

class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="roles")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Usuario/Rol"
        verbose_name_plural = "Usuarios/Roles"
        unique_together = ('usuario', 'rol')

    def __str__(self):
        return f"{self.usuario.persona.nombre} → {self.rol.nombre}"

    @staticmethod
    def asignar_rol(usuario, nuevo_rol):
        """Elimina roles anteriores y asigna el nuevo (como define el sistema del Polo)."""
        UsuarioRol.objects.filter(usuario=usuario).delete()
        UsuarioRol.objects.create(usuario=usuario, rol=nuevo_rol)
        # Vincular también con el grupo de Django
        usuario.user.groups.clear()
        if nuevo_rol.group:
            usuario.user.groups.add(nuevo_rol.group)