"""
URL configuration for Universidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps.Home import views
from .views import (
    EstudiantesView, 
    AdministradoresView,
    crear_estudiante,
    editar_estudiante,
    eliminar_estudiante,
    detalle_estudiante,
    crear_administrador,
    editar_administrador,
    eliminar_administrador,
    detalle_administrador,
)

app_name = 'principal'

urlpatterns = [
    path('', EstudiantesView.as_view(), name='Estudianteapp'),
    path('Administradores/', AdministradoresView.as_view(), name='Administradoresapp'),
    path('estudiantes/crear/', crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:pk>/', editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:pk>/', eliminar_estudiante, name='eliminar_estudiante'),
    path('estudiantes/detalle/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('administradores/crear/', crear_administrador, name='crear_administrador'),
    path('administradores/editar/<int:pk>/', editar_administrador, name='editar_administrador'),
    path('administradores/eliminar/<int:pk>/', eliminar_administrador, name='eliminar_administrador'),
    path('administradores/detalle/<int:pk>/', detalle_administrador, name='detalle_administrador'),
]