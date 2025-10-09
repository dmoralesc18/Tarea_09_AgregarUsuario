from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from django.db.models import Q
from .models import Publicacion, EstudianteAutorizado
from .forms import PublicacionForm, EstudianteAutorizadoForm, PublicacionFiltroForm

class AdminView(TemplateView):
    template_name = 'Admin.html'

class PublicacionesView(TemplateView):
    template_name = 'Publicacion.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicaciones'] = Publicacion.objects.all().order_by('-fecha_creacion')
        return context

class AutorizadosView(TemplateView):
    template_name = 'Autorizados.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autorizados'] = EstudianteAutorizado.objects.filter(activo=True).order_by('-fecha_autorizacion')
        return context

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save()
            messages.success(request, f'Publicación "{publicacion.titulo}" creada exitosamente.')
            return redirect('publicaciones:publicacionesapp')
    else:
        form = PublicacionForm()
    
    return render(request, 'crear_publicacion.html', {'form': form})

def editar_publicacion(request, pk):
    publicacion_obj = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion_obj)
        if form.is_valid():
            publicacion = form.save()
            messages.success(request, f'Publicación "{publicacion.titulo}" actualizada exitosamente.')
            return redirect('publicaciones:publicacionesapp')
    else:
        form = PublicacionForm(instance=publicacion_obj)
    
    return render(request, 'editar_publicacion.html', {
        'form': form, 
        'publicacion': publicacion_obj
    })

def eliminar_publicacion(request, pk):
    publicacion_obj = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        titulo = publicacion_obj.titulo
        publicacion_obj.delete()
        messages.success(request, f'Publicación "{titulo}" eliminada exitosamente.')
        return redirect('publicaciones:publicacionesapp')
    
    return render(request, 'eliminar_publicacion.html', {
        'publicacion': publicacion_obj
    })

def detalle_publicacion(request, pk):
    publicacion_obj = get_object_or_404(Publicacion, pk=pk)
    publicacion_obj.vistas += 1
    publicacion_obj.save(update_fields=['vistas'])
    
    return render(request, 'detalle_publicacion.html', {
        'publicacion': publicacion_obj
    })

def crear_autorizado(request):
    if request.method == 'POST':
        form = EstudianteAutorizadoForm(request.POST)
        if form.is_valid():
            autorizado = form.save()
            messages.success(request, f'Estudiante {autorizado.estudiante} autorizado exitosamente.')
            return redirect('publicaciones:autorizadosapp')
    else:
        form = EstudianteAutorizadoForm()
    
    return render(request, 'crear_autorizado.html', {'form': form})

def editar_autorizado(request, pk):
    autorizado_obj = get_object_or_404(EstudianteAutorizado, pk=pk)
    if request.method == 'POST':
        form = EstudianteAutorizadoForm(request.POST, instance=autorizado_obj)
        if form.is_valid():
            autorizado = form.save()
            messages.success(request, f'Autorización de {autorizado.estudiante} actualizada exitosamente.')
            return redirect('publicaciones:autorizadosapp')
    else:
        form = EstudianteAutorizadoForm(instance=autorizado_obj)
    
    return render(request, 'editar_autorizado.html', {'form': form})

def eliminar_autorizado(request, pk):
    autorizado_obj = get_object_or_404(EstudianteAutorizado, pk=pk)
    if request.method == 'POST':
        estudiante_nombre = str(autorizado_obj.estudiante)
        autorizado_obj.delete()
        messages.success(request, f'Autorización de {estudiante_nombre} eliminada exitosamente.')
        return redirect('publicaciones:autorizadosapp')
    
    return render(request, 'eliminar_autorizado.html', {
        'autorizado': autorizado_obj
    })

def detalle_autorizado(request, pk):
    autorizado_obj = get_object_or_404(EstudianteAutorizado, pk=pk)
    publicaciones = Publicacion.objects.filter(autor=autorizado_obj).order_by('-fecha_creacion')
    
    return render(request, 'detalle_autorizado.html', {
        'autorizado': autorizado_obj,
        'publicaciones': publicaciones
    })

def buscar_publicaciones(request):
    form = PublicacionFiltroForm(request.GET or None)
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        estado = form.cleaned_data.get('estado')
        autor = form.cleaned_data.get('autor')
        
        if titulo:
            publicaciones = publicaciones.filter(
                Q(titulo__icontains=titulo) | Q(contenido__icontains=titulo)
            )
        if estado:
            publicaciones = publicaciones.filter(estado=estado)
        if autor:
            publicaciones = publicaciones.filter(autor=autor)
    
    return render(request, 'buscar_publicaciones.html', {
        'form': form,
        'publicaciones': publicaciones
    })

def toggle_estado_autorizado(request, pk):
    """Vista para activar/desactivar un estudiante autorizado"""
    autorizado_obj = get_object_or_404(EstudianteAutorizado, pk=pk)
    
    if request.method == 'POST':
        autorizado_obj.activo = not autorizado_obj.activo
        autorizado_obj.save()
        
        estado = "activado" if autorizado_obj.activo else "desactivado"
        messages.success(request, f'Estudiante {autorizado_obj.estudiante} {estado} exitosamente.')
    
    return redirect('publicaciones:autorizadosapp')

def cambiar_estado_publicacion(request, pk):
    """Vista para cambiar el estado de una publicación"""
    publicacion_obj = get_object_or_404(Publicacion, pk=pk)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['borrador', 'publicado', 'archivado']:
            publicacion_obj.estado = nuevo_estado
            publicacion_obj.save()
            messages.success(request, f'Estado de la publicación cambiado a "{nuevo_estado}".')
        else:
            messages.error(request, 'Estado no válido.')
    
    return redirect('publicaciones:publicacionesapp')