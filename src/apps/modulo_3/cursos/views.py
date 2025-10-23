from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
import pandas as pd # Necesitarás instalar: pip install pandas openpyxl

# Importamos Modelos y Forms de nuestra app
from .models import Curso, Comision, Material, ComisionDocente
from .forms import CursoForm, ComisionForm, MaterialForm, ImportarCursosForm, AsignacionDocenteForm

# Importamos los modelos de la app de usuarios
from gestion_usuarios.models import Usuario, Rol

# --- CRUD para Cursos ---

class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/curso_list.html' # Plantilla que usaremos
    context_object_name = 'cursos'

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('cursos:curso_list') # Redirige a la lista al tener éxito

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('cursos:curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('cursos:curso_list')

# --- CRUD para Comisiones ---

class ComisionListView(ListView):
    model = Comision
    template_name = 'cursos/comision_list.html'
    context_object_name = 'comisiones'

class ComisionCreateView(CreateView):
    model = Comision
    form_class = ComisionForm
    template_name = 'cursos/comision_form.html'
    success_url = reverse_lazy('cursos:comision_list')

class ComisionUpdateView(UpdateView):
    model = Comision
    form_class = ComisionForm
    template_name = 'cursos/comision_form.html'
    success_url = reverse_lazy('cursos:comision_list')

class ComisionDeleteView(DeleteView):
    model = Comision
    template_name = 'cursos/curso_confirm_delete.html' # Reutilizamos la plantilla de confirmar
    success_url = reverse_lazy('cursos:comision_list')

# --- Vistas para Funcionalidades Específicas ---

def asignar_docente(request, pk):
    """
    Vista para asignar y desasignar docentes de una comisión.
    'pk' es el ID de la Comision.
    """
    comision = get_object_or_404(Comision, id_comision=pk)
    
    # Obtenemos los docentes ya asignados a esta comisión
    docentes_asignados_ids = ComisionDocente.objects.filter(fk_id_comision=comision).values_list('fk_id_docente', flat=True)
    docentes_asignados = Usuario.objects.filter(id_usuario__in=docentes_asignados_ids)
    
    if request.method == 'POST':
        # Lógica para agregar un docente
        form = AsignacionDocenteForm(request.POST)
        if form.is_valid():
            docente = form.cleaned_data['docente']
            if docente not in docentes_asignados:
                ComisionDocente.objects.create(fk_id_comision=comision, fk_id_docente=docente)
                messages.success(request, f'Docente {docente} asignado correctamente.')
            else:
                messages.warning(request, f'El docente {docente} ya estaba asignado.')
            return redirect('cursos:comision_asignar_docente', pk=comision.id_comision)
    else:
        # Lógica para mostrar el formulario
        form = AsignacionDocenteForm()

    context = {
        'comision': comision,
        'docentes_asignados': docentes_asignados,
        'form': form
    }
    return render(request, 'cursos/comision_asignar_docentes.html', context)

def desasignar_docente(request, pk, docente_id):
    """
    Vista para quitar un docente de una comisión.
    'pk' es el ID de la Comision.
    'docente_id' es el ID del Usuario (docente).
    """
    comision = get_object_or_404(Comision, id_comision=pk)
    docente = get_object_or_404(Usuario, id_usuario=docente_id)
    asignacion = ComisionDocente.objects.filter(fk_id_comision=comision, fk_id_docente=docente)
    
    if asignacion.exists():
        asignacion.delete()
        messages.success(request, f'Docente {docente} desasignado correctamente.')
    else:
        messages.error(request, 'La asignación no existe.')
        
    return redirect('cursos:comision_asignar_docente', pk=comision.id_comision)


def gestion_materiales(request, pk):
    """
    Vista para que un docente suba y vea materiales de una comisión.
    'pk' es el ID de la Comision.
    """
    comision = get_object_or_404(Comision, id_comision=pk)
    materiales = Material.objects.filter(fk_id_comision=comision)
    
    # --- SIMULACIÓN DE USUARIO LOGUEADO ---
    # En la vida real, obtendrías el docente desde 'request.user'
    # Por ahora, usaremos el primer docente que exista.
    # Asegúrate de que exista un docente en tu BD.
    try:
        rol_docente = Rol.objects.get(nombre='Docente')
        docente_logueado = Usuario.objects.filter(fk_id_rol=rol_docente).first()
        if not docente_logueado:
             messages.error(request, "No hay docentes en el sistema para simular la subida.")
    except Rol.DoesNotExist:
        docente_logueado = None
    # --- FIN DE LA SIMULACIÓN ---
    
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            if not docente_logueado:
                messages.error(request, "Error: No se pudo identificar al docente.")
                return redirect('cursos:comision_gestion_materiales', pk=comision.id_comision)
                
            material = form.save(commit=False)
            material.fk_id_comision = comision
            material.fk_id_docente = docente_logueado # Se asigna el docente logueado
            material.save()
            messages.success(request, 'Material subido correctamente.')
            return redirect('cursos:comision_gestion_materiales', pk=comision.id_comision)
    else:
        form = MaterialForm()

    context = {
        'comision': comision,
        'materiales': materiales,
        'form': form,
        'docente_simulado': docente_logueado # Solo para mostrar
    }
    return render(request, 'cursos/gestion_materiales.html', context)

def importar_cursos_excel(request):
    """
    Vista para la importación masiva de Cursos (no comisiones) desde Excel.
    """
    if request.method == 'POST':
        form = ImportarCursosForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo_excel']
            try:
                # Lee el archivo excel
                df = pd.read_excel(archivo)
                cursos_creados = 0
                for index, row in df.iterrows():
                    # Crea un objeto Curso por cada fila
                    Curso.objects.create(
                        nombre=row['nombre'],
                        descripcion=row.get('descripcion', ''),
                        edad_minima=row.get('edad_minima', 0),
                        requisitos=row.get('requisitos', ''),
                        estado='Abierto'
                    )
                    cursos_creados += 1
                messages.success(request, f'{cursos_creados} cursos importados correctamente.')
                return redirect('cursos:curso_list')
            except Exception as e:
                messages.error(request, f'Error al procesar el archivo: {e}')
    else:
        form = ImportarCursosForm()
    
    return render(request, 'cursos/importar_cursos.html', {'form': form})
