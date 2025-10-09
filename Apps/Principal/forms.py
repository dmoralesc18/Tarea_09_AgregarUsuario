from django import forms
from .models import estudiante, administradores

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = estudiante
        fields = ['nombre', 'apellido', 'edad', 'grado', 'curso']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la edad',
                'min': '1',
                'max': '100'
            }),
            'grado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1er Año, 2do Año, etc.'
            }),
            'curso': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Informática, Contabilidad, etc.'
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'grado': 'Grado',
            'curso': 'Curso',
        }

    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad < 15 or edad > 100:
            raise forms.ValidationError('La edad debe estar entre 15 y 100 años')
        return edad

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = administradores
        fields = ['nombre', 'edad', 'cargo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre completo'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la edad',
                'min': '18',
                'max': '70'
            }),
            'cargo': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[
                ('', 'Seleccione un cargo'),
                ('Director', 'Director'),
                ('Coordinador', 'Coordinador'),
                ('Secretario', 'Secretario'),
                ('Supervisor', 'Supervisor'),
                ('Otros', 'Otros'),
            ]),
        }
        labels = {
            'nombre': 'Nombre Completo',
            'edad': 'Edad',
            'cargo': 'Cargo',
        }

    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad < 18 or edad > 100:
            raise forms.ValidationError('La edad debe estar entre 18 y 100 años')
        return edad