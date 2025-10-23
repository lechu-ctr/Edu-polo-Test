from django.db import models
from gestion_usuarios.models import Usuario

class Curso(models.Model):
    OPCIONES_ESTADO_CURSO = [
        ('Abierto', 'Abierto'), # Se pueden crear comisiones
        ('Cerrado', 'Cerrado'), # Es un curso histórico
    ]
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False) 
    descripcion = models.TextField(blank=True, null=True) 
    edad_minima = models.IntegerField(blank=True, null=True) 
    requisitos = models.TextField(blank=True, null=True) 
    contenido_multimedia = models.URLField(max_length=255, blank=True, null=True) 
    estado = models.CharField(max_length=10, choices=OPCIONES_ESTADO_CURSO, default='Abierto') 

    def __str__(self):
        return self.nombre

class Comision(models.Model):
    OPCIONES_ESTADO_COMISION = [
        ('Abierta', 'Abierta'), # Permite inscripciones
        ('Cerrada', 'Cerrada'), # No permite más inscripciones
        ('Finalizada', 'Finalizada'), # El curso ya terminó
    ]
    id_comision = models.AutoField(primary_key=True)
    fk_id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='fk_id_curso') 
    dias_horarios = models.TextField(blank=True, null=True) 
    lugar = models.CharField(max_length=100, blank=True, null=True) 
    fecha_inicio = models.DateField(blank=True, null=True) 
    fecha_fin = models.DateField(blank=True, null=True) 
    cupo_maximo = models.IntegerField(default=20) 
    estado = models.CharField(max_length=10, choices=OPCIONES_ESTADO_COMISION, default='Abierta') 

    docentes = models.ManyToManyField(
        Usuario, 
        through='ComisionDocente',
        related_name='comisiones_asignadas'
    )

    def __str__(self):
        return f"{self.fk_id_curso.nombre} - (Comisión N°: {self.id_comision})"

class ComisionDocente(models.Model):
    # Tabla intermedia para asignar Docentes (Usuarios) a Comisiones
    fk_id_comision = models.ForeignKey(Comision, on_delete=models.CASCADE, db_column='fk_id_comision')
    # Usamos el modelo 'Usuario' que importamos
    fk_id_docente = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='fk_id_docente') 

    class Meta:
        unique_together = ('fk_id_comision', 'fk_id_docente') 

    def __str__(self):
        return f"{self.fk_id_comision} / {self.fk_id_docente}"

class Material(models.Model):
    # Modelo para "Gestión de Materiales" 
    id_material = models.AutoField(primary_key=True)
    fk_id_comision = models.ForeignKey(Comision, on_delete=models.CASCADE, db_column='fk_id_comision')
    # Usamos el modelo 'Usuario' importado (el docente que lo sube)
    fk_id_docente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, db_column='fk_id_docente')
    nombre_archivo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to='materiales_cursos/') # Guarda el archivo en /media/materiales_cursos/
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_archivo