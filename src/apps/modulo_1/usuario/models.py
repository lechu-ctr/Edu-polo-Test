from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    generos = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
        ('P', 'Prefiero no decirlo'),
    ]

    dni = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, choices=generos, blank=True, null=True)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    condiciones_medicas = models.TextField(blank=True, null=True)

    @property
    def edad(self):
        today = date.today()
        return (
            today.year
            - self.fecha_nacimiento.year
            - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        )

    def __str__(self):
        return self.nombre

    @staticmethod
    def limpiar_dni(dni_raw: str) -> str:
        return ''.join(ch for ch in dni_raw if ch.isdigit())

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    contraseña = models.CharField(null=True, blank=True)
    permiso_imagen = models.BooleanField(default=False)
    permiso_voz = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.persona.nombre}"

    def tiene_rol(self, nombre_rol):
        return self.roles.filter(nombre=nombre_rol).exists()