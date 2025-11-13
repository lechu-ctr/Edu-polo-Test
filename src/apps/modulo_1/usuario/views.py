from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
#Persona
class PersonaListView(ListView):
    model = Persona
    template_name = 'modulo_1/usuario/persona/persona_list.html'

class PersonaCreateView(CreateView):
    model = Persona
    template_name = 'modulo_1/usuario/persona/persona_create.html'
    fields = '__all__'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = 'modulo_1/usuario/persona/persona_update.html'
    fields = '__all__'
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'modulo_1/usuario/persona/persona_delete.html'
    success_url = reverse_lazy('persona_list')

#Usuario
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'modulo_1/usuario/usuario/usuario_list.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'modulo_1/usuario/usuario/usuario_create.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'modulo_1/usuario/usuario/usuario_update.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'modulo_1/usuario/usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario_list')