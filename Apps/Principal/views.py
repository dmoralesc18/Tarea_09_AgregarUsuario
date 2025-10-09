from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Apps.Principal.models import administradores, estudiante
from .forms import EstudianteForm, AdministradorForm


class EstudiantesView(TemplateView):
    template_name = 'Estudiantes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = estudiante.objects.all()
        return context

class AdministradoresView(TemplateView):
    template_name = 'Administradores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administradores'] = administradores.objects.all()
        return context

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante creado exitosamente.')
            return redirect('principal:Estudianteapp')
    else:
        form = EstudianteForm()
    
    return render(request, 'crear_estudiante.html', {'form': form})

def editar_estudiante(request, pk):
    estudiante_obj = get_object_or_404(estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante actualizado exitosamente.')
            return redirect('principal:Estudianteapp')
    else:
        form = EstudianteForm(instance=estudiante_obj)
    
    return render(request, 'editar_estudiante.html', {
        'form': form, 
        'estudiante': estudiante_obj
    })

def eliminar_estudiante(request, pk):
    estudiante_obj = get_object_or_404(estudiante, pk=pk)
    if request.method == 'POST':
        nombre_completo = f"{estudiante_obj.nombre} {estudiante_obj.apellido}"
        estudiante_obj.delete()
        messages.success(request, f'Estudiante {nombre_completo} eliminado exitosamente.')
        return redirect('principal:Estudianteapp')
    
    return render(request, 'eliminar_estudiante.html', {
        'estudiante': estudiante_obj
    })

def detalle_estudiante(request, pk):
    estudiante_obj = get_object_or_404(estudiante, pk=pk)
    return render(request, 'detalle_estudiante.html', {
        'estudiante': estudiante_obj
    })

def crear_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administrador creado exitosamente.')
            return redirect('principal:Administradoresapp')
    else:
        form = AdministradorForm()
    
    return render(request, 'crear_administrador.html', {'form': form})

def editar_administrador(request, pk):
    administrador_obj = get_object_or_404(administradores, pk=pk)
    if request.method == 'POST':
        form = AdministradorForm(request.POST, instance=administrador_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administrador actualizado exitosamente.')
            return redirect('principal:Administradoresapp')
    else:
        form = AdministradorForm(instance=administrador_obj)
    
    return render(request, 'editar_administrador.html', {
        'form': form, 
        'administrador': administrador_obj
    })

def eliminar_administrador(request, pk):
    administrador_obj = get_object_or_404(administradores, pk=pk)
    if request.method == 'POST':
        nombre_completo = administrador_obj.nombre
        administrador_obj.delete()
        messages.success(request, f'Administrador {nombre_completo} eliminado exitosamente.')
        return redirect('principal:Administradoresapp')
    
    return render(request, 'eliminar_administrador.html', {
        'administrador': administrador_obj
    })

def detalle_administrador(request, pk):
    administrador_obj = get_object_or_404(administradores, pk=pk)
    return render(request, 'detalle_administrador.html', {
        'administrador': administrador_obj
    })

class EstudianteCreateView(CreateView):
    model = estudiante
    form_class = EstudianteForm
    template_name = 'estudiantes/crear_estudiante.html'
    success_url = reverse_lazy('principal:Estudianteapp')
    
    def form_valid(self, form):
        messages.success(self.request, 'Estudiante creado exitosamente.')
        return super().form_valid(form)

class EstudianteUpdateView(UpdateView):
    model = estudiante
    form_class = EstudianteForm
    template_name = 'estudiantes/editar_estudiante.html'
    success_url = reverse_lazy('principal:Estudianteapp')
    
    def form_valid(self, form):
        messages.success(self.request, 'Estudiante actualizado exitosamente.')
        return super().form_valid(form)

class EstudianteDeleteView(DeleteView):
    model = estudiante
    template_name = 'estudiantes/eliminar_estudiante.html'
    success_url = reverse_lazy('principal:Estudianteapp')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Estudiante eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)