from django.db import models


class estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    grado = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class administradores(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    cargo = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.nombre, self.cargo)