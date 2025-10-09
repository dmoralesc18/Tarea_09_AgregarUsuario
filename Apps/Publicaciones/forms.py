from django import forms
from .models import Publicacion, EstudianteAutorizado
from Apps.Principal.models import estudiante, administradores

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'autor', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título de la publicación'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escriba el contenido de la publicación',
                'rows': 6
            }),
            'autor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'autor': 'Autor (Estudiante Autorizado)',
            'estado': 'Estado de la Publicación',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = EstudianteAutorizado.objects.filter(activo=True)

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 5:
            raise forms.ValidationError('El título debe tener al menos 5 caracteres')
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data['contenido']
        if len(contenido) < 50:
            raise forms.ValidationError('El contenido debe tener al menos 50 caracteres')
        return contenido

class EstudianteAutorizadoForm(forms.ModelForm):
    class Meta:
        model = EstudianteAutorizado
        fields = ['estudiante', 'autorizado_por', 'activo']
        widgets = {
            'estudiante': forms.Select(attrs={
                'class': 'form-control'
            }),
            'autorizado_por': forms.Select(attrs={
                'class': 'form-control'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'estudiante': 'Estudiante',
            'autorizado_por': 'Autorizado por',
            'activo': 'Activo',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        estudiantes_ya_autorizados = EstudianteAutorizado.objects.values_list('estudiante', flat=True)
        if self.instance.pk:
            estudiantes_ya_autorizados = estudiantes_ya_autorizados.exclude(pk=self.instance.pk)
        
        self.fields['estudiante'].queryset = estudiante.objects.exclude(
            id__in=estudiantes_ya_autorizados
        )
        self.fields['autorizado_por'].queryset = administradores.objects.all()

    def clean_estudiante(self):
        estudiante_seleccionado = self.cleaned_data['estudiante']
        existing = EstudianteAutorizado.objects.filter(estudiante=estudiante_seleccionado)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)
        
        if existing.exists():
            raise forms.ValidationError('Este estudiante ya tiene una autorización existente.')
        
        return estudiante_seleccionado

class PublicacionFiltroForm(forms.Form):
    titulo = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por título'
        })
    )
    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los estados')] + Publicacion.ESTADO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    autor = forms.ModelChoiceField(
        required=False,
        queryset=EstudianteAutorizado.objects.filter(activo=True),
        empty_label="Todos los autores",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )