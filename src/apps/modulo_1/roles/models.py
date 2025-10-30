from django.db import models
from apps.modulo_1.usuario.models import Usuario, Persona


# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)
    jerarquia = models.PositiveSmallIntegerField()


    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(jerarquia__gte=1) & models.Q(jerarquia__lte=5),
                name="rol_jerarquia_entre_1_y_5"
            )
        ]
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
   
    def __str__(self):
        return f"{self.nombre} - Jerarquia({self.jerarquia})"


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

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel_estudios = models.CharField(choices=grado)
    institucion_actual = models.CharField(max_length=255)
    experiencia_laboral = models.TextField(blank=True, null=True)


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


class UsuarioRol(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE)


    def __str__(self):
        return f"Usuario {self.usuario_id} - Rol {self.rol.nombre}"