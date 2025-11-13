from django.urls import path
from .views import DocenteCreateView, DocenteDeleteView, DocenteListView, DocenteUpdateView, EstudianteCreateView, EstudianteDeleteView, EstudianteListView, EstudianteUpdateView, TutorCreateView, TutorDeleteView, TutorListView, TutorUpdateView, RolCreateView, RolDeleteView, RolListView, RolUpdateView

app_name = "roles"

urlpatterns = [
#Rol
    path('rol/', RolListView.as_view(), name='rol_list'),
    path('rol/crear/', RolCreateView.as_view(), name='rol_create'),
    path('rol/editar/<int:pk>/', RolUpdateView.as_view(), name='rol_update'),
    path('rol/eliminar/<int:pk>/', RolDeleteView.as_view(), name='rol_delete'),

#Docente
    path('docente/', DocenteListView.as_view(), name='docente_list'),
    path('docente/crear/', DocenteCreateView.as_view(), name='docente_create'),
    path('docente/editar/<int:pk>/', DocenteUpdateView.as_view(), name='docente_update'),
    path('docente/eliminar/<int:pk>/', DocenteDeleteView.as_view(), name='docente_delete'),

#Estudiante
    path('estudiante/', EstudianteListView.as_view(), name='estudiante_list'),
    path('estudiante/crear/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('estudiante/editar/<int:pk>/', EstudianteUpdateView.as_view(), name='estudiante_update'),
    path('estudiante/eliminar/<int:pk>/', EstudianteDeleteView.as_view(), name='estudiante_delete'),

#Tutor
    path('tutor/', TutorListView.as_view(), name='tutor_list'),
    path('tutor/crear/', TutorCreateView.as_view(), name='tutor_create'),
    path('tutor/editar/<int:pk>/', TutorUpdateView.as_view(), name='tutor_update'),
    path('tutor/eliminar/<int:pk>/', TutorDeleteView.as_view(), name='tutor_delete'),
]