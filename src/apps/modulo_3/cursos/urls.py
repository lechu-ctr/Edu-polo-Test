from django.urls import path
from . import views

# Esto es importante para que los 'reverse_lazy' y {% url %} funcionen
app_name = 'cursos'

urlpatterns = [
    # --- URLs de Cursos ---
    path('cursos/', views.CursoListView.as_view(), name='curso_list'),
    path('cursos/nuevo/', views.CursoCreateView.as_view(), name='curso_create'),
    path('cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('cursos/<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='curso_delete'),
    
    # --- URLs de Comisiones ---
    path('comisiones/', views.ComisionListView.as_view(), name='comision_list'),
    path('comisiones/nueva/', views.ComisionCreateView.as_view(), name='comision_create'),
    path('comisiones/<int:pk>/editar/', views.ComisionUpdateView.as_view(), name='comision_update'),
    path('comisiones/<int:pk>/eliminar/', views.ComisionDeleteView.as_view(), name='comision_delete'),

    # --- URLs de Funcionalidades Especiales ---
    path('cursos/importar/', views.importar_cursos_excel, name='curso_importar'),
    path('comisiones/<int:pk>/asignar/', views.asignar_docente, name='comision_asignar_docente'),
    path('comisiones/<int:pk>/desasignar/<int:docente_id>/', views.desasignar_docente, name='desasignar_docente'),
    path('comisiones/<int:pk>/materiales/', views.gestion_materiales, name='comision_gestion_materiales'),
    
    # (Opcional) URL para eliminar materiales
    # path('materiales/<int:pk>/eliminar/', views.MaterialDeleteView.as_view(), name='material_delete'),
]
