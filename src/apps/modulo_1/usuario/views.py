from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
#Persona
class PersonaListView(ListView):
    model = Persona
    template_name = 'usuario/persona_list.html'

class PersonaCreateView(CreateView):
    model = Persona
    template_name = 'usuario/persona_form.html'
    fields = '__all__'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = 'usuario/persona_form.html'
    fields = '__all__'
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'usuario/persona_confirm_delete.html'
    success_url = reverse_lazy('persona_list')

#Usuario
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuario/usuario_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuario/usuario_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')