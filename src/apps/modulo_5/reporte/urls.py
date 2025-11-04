from django.urls import path
from . import views

urlpatterns = [
    path('inscritos/', views.reporte_inscritos, name='reporte_inscritos'),
    path('asistencia/', views.reporte_asistencia, name='reporte_asistencia'),
    path('egresos/', views.reporte_egresos, name='reporte_egresos'),
    path('estudiantes/', views.reporte_estudiantes, name='reporte_estudiantes'),
]
