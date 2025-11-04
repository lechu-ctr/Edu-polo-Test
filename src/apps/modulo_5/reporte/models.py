from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.CharField(max_length=50)  # Ej: "A. Lunes"

    def __str__(self):
        return f"{self.nombre} | {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado_inscripcion = models.BooleanField(default=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"




class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        estado = "Presente" if self.presente else "Ausente"
        return f"{self.estudiante} - {self.fecha} - {estado}"


class Egreso(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.estudiante} - {self.fecha} - {self.motivo}"
