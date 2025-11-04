from django.db import models
from django.utils import timezone 
from apps.modulo_3.cursos.models import Curso, Comision
from apps.modulo_1.roles.models import Estudiante,Tutor


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, 
        db_column='id_estudiante', 
        related_name='inscripciones_estudiante'
    )
    id_comision = models.ForeignKey(
        Comision, 
        on_delete=models.CASCADE, 
        db_column='id_comision',
        related_name='inscripciones_comision'
    )
    id_curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        db_column='id_curso',
        related_name='inscripciones_curso'
    )

    id_tutor = models.ForeignKey(
        Tutor, 
        on_delete=models.SET_NULL, # Una buena opción si el tutor es eliminado
        db_column='id_tutor',
        related_name='inscripciones_tutor',
        null=True, 
        blank=True
    )

    fecha_inscripcion = models.DateField(
        default=timezone.now
        
    )
    
    estado = models.CharField(max_length=50, default='Activo')
    
    observacion = models.TextField(null=True, blank=True)

    class Meta:
       
        db_table = 'inscripcion' 
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'
     

    def __str__(self):
        return f"Inscripción {self.id_inscripcion} - Estudiante: {self.id_estudiante}"