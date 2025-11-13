from django.shortcuts import render
from .models import Estudiante,Asistencia,Egreso, Curso
from django.db.models import Count, Q
from django.views.generic import TemplateView, ListView
# Create your views here.

def reporte_asistencias(request):
    # Ejemplo simple
    return render(request, 'reporte/asistencias.html')


def reporte_inscritos(request):
    # Ejemplo simple
    return render(request, 'reporte/inscritos.html')

def reporte_egresos(request):
    # Ejemplo simple
    return render(request, 'reporte/egresos.html')

def reporte_estudiantes(request):
    # Ejemplo simple
    return render(request, 'reporte/estudiantes.html')


class DashboardView(TemplateView): 
    template_name = 'reportes/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # algunos datos resumen
        context['total_estudiantes'] = Estudiante.objects.count()
        context['total_inscritos'] = Curso.objects.count()
        context['total_asistencias'] = Asistencia.objects.count()
        # otros datos según lo que quieras mostrar
        return context