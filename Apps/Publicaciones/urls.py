# Apps/Publicaciones/urls.py
from django.contrib import admin
from django.urls import path, include
from Apps.Publicaciones import views
from .views import (
    AdminView, 
    PublicacionesView, 
    AutorizadosView,
    crear_publicacion,
    editar_publicacion,
    eliminar_publicacion,
    detalle_publicacion,
    crear_autorizado,
    editar_autorizado,
    eliminar_autorizado,
    detalle_autorizado,
    buscar_publicaciones,
    toggle_estado_autorizado,
    cambiar_estado_publicacion,
)

app_name = 'publicaciones'

urlpatterns = [
    path('admin/', views.AdminView.as_view(), name='adminapp'),
    path('publicaciones/', views.PublicacionesView.as_view(), name='publicacionesapp'),
    path('autorizados/', views.AutorizadosView.as_view(), name='autorizadosapp'),
    
    # =============== URLs CRUD PARA PUBLICACIONES ===============
    path('publicaciones/crear/', crear_publicacion, name='crear_publicacion'),
    path('publicaciones/editar/<int:pk>/', editar_publicacion, name='editar_publicacion'),
    path('publicaciones/eliminar/<int:pk>/', eliminar_publicacion, name='eliminar_publicacion'),
    path('publicaciones/detalle/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
    
    # =============== URLs CRUD PARA ESTUDIANTES AUTORIZADOS ===============
    path('autorizados/crear/', crear_autorizado, name='crear_autorizado'),
    path('autorizados/editar/<int:pk>/', editar_autorizado, name='editar_autorizado'),
    path('autorizados/eliminar/<int:pk>/', eliminar_autorizado, name='eliminar_autorizado'),
    path('autorizados/detalle/<int:pk>/', detalle_autorizado, name='detalle_autorizado'),
    
    # =============== URLs ADICIONALES ===============
    path('publicaciones/buscar/', buscar_publicaciones, name='buscar_publicaciones'),
    path('autorizados/toggle/<int:pk>/', toggle_estado_autorizado, name='toggle_estado_autorizado'),
    path('publicaciones/cambiar-estado/<int:pk>/', cambiar_estado_publicacion, name='cambiar_estado_publicacion'),
]