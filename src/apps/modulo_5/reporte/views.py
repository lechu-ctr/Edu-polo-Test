from django.shortcuts import render
from .models import Estudiante, Asistencia, Egreso,Curso
from django.db.models import Count, Q
# Create your views here.


def reporte_estudiantes(request):
    estudiantes = Estudiante.objects.select_related('curso')

    datos = []
    for estudiante in estudiantes:
        total_asistencias = Asistencia.objects.filter(estudiante=estudiante, presente=True).count()
        total_clases = Asistencia.objects.filter(estudiante=estudiante).count()
        porcentaje = round((total_asistencias / total_clases) * 100, 2) if total_clases > 0 else 0

        egresado = Egreso.objects.filter(estudiante=estudiante).exists()

        datos.append({
            'id': estudiante.id,
            'nombre': f"{estudiante.nombre} {estudiante.apellido}",
            'curso': estudiante.curso.nombre,
            'asistencia': porcentaje,
            'egreso': egresado,
            'activo': estudiante.estado_inscripcion,
            'fecha': estudiante.fecha_inscripcion
        })

    return render(request, 'reportes/reporte_estudiantes.html', {'datos': datos})


def reporte_asistencia(request):
    curso_filtrado = request.GET.get('curso')
    cursos = Curso.objects.all()

    try:
        curso_filtrado = int(curso_filtrado)
    except (TypeError, ValueError):
        curso_filtrado = None

    asistencias = (
        Asistencia.objects.filter(curso_id=curso_filtrado)
        if curso_filtrado and cursos.filter(id=curso_filtrado).exists()
        else Asistencia.objects.all()
    )

    resumen = (
        Asistencia.objects
        .values('curso__nombre')
        .annotate(
            total=Count('id'),
            presentes=Count('id', filter=Q(presente=True))
        )
    )

    labels = [r['curso__nombre'] for r in resumen]
    porcentajes = [
        round((r['presentes'] / r['total']) * 100, 2) if r['total'] > 0 else 0
        for r in resumen
    ]

    return render(request, 'reportes/reporte_asistencia.html', {
        'asistencias': asistencias,
        'cursos': cursos,
        'curso_filtrado': curso_filtrado,
        'labels': labels,
        'porcentajes': porcentajes
    })
    
def reporte_egresos(request):
    curso_filtrado = request.GET.get('curso')
    cursos = Curso.objects.all()

    try:
        curso_filtrado = int(curso_filtrado)
    except (TypeError, ValueError):
        curso_filtrado = None

    egresos = (
        Egreso.objects.filter(curso_id=curso_filtrado)
        if curso_filtrado and cursos.filter(id=curso_filtrado).exists()
        else Egreso.objects.all()
    )

    return render(request, 'reportes/reporte_egresos.html', {
        'egresos': egresos,
        'cursos': cursos,
        'curso_filtrado': curso_filtrado
    })