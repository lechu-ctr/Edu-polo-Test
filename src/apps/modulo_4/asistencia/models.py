from django.db import models
from apps.modulo_2.inscripciones.models import Inscripcion


from django.db import models

class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    id_inscripcion = models.ForeignKey( Inscripcion, 
        on_delete=models.CASCADE,  # Por ejemplo, si se borra la inscripción, se borran sus registros de asistencia
        db_column='id_inscripcion' # Mantiene el nombre de columna de tu DB original
    )
    fecha_clase = models.DateField()
    presente = models.BooleanField(default=False)
    class Meta:
       
        db_table = 'asistencia'
        
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        # Muestra una representación legible del objeto
        return f"Asistencia de {self.id_inscripcion} en {self.fecha_clase}"

