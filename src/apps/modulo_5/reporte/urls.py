from django.urls import path
from . import views

urlpatterns = [
    path('inscritos/', views.reporte_inscritos, name='reporte_inscritos'),
    path('asistencias/', views.reporte_asistencias, name='reporte_asistencias'),
    path('egresos/', views.reporte_egresos, name='reporte_egresos'),
    path('estudiantes/', views.reporte_estudiantes, name='reporte_estudiantes'),
    path('dashboard/', views.reporte_estudiantes, name='reporte_dashboard'),
    path('base/', views.reporte_estudiantes, name='reporte_base'),
]
