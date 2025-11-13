from django.urls import path
from .views import PersonaListView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView, UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView

app_name = "usuario"

urlpatterns = [
#Persona
    path('personas/', PersonaListView.as_view(), name='persona_list'),
    path('personas/crear/', PersonaCreateView.as_view(), name='persona_create'),
    path('personas/editar/<int:pk>/', PersonaUpdateView.as_view(), name='persona_update'),
    path('personas/eliminar/<int:pk>/', PersonaDeleteView.as_view(), name='persona_delete'),

#Usuario
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/crear/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]
