from django.db import models
from Apps.Principal.models import estudiante, administradores

class EstudianteAutorizado(models.Model):
    estudiante = models.OneToOneField(estudiante, on_delete=models.CASCADE)
    fecha_autorizacion = models.DateTimeField(auto_now_add=True)
    autorizado_por = models.ForeignKey(administradores, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.estudiante.nombre} {self.estudiante.apellido} - Autorizado"
    
    class Meta:
        verbose_name = "Estudiante Autorizado"
        verbose_name_plural = "Estudiantes Autorizados"

class Publicacion(models.Model):
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]
    
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(EstudianteAutorizado, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='borrador')
    vistas = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor.estudiante.nombre}"
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-fecha_creacion']