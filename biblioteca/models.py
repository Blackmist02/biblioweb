from django.db import models

# Create your models here.

class libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True)
    autor = models.CharField(max_length=100)
    pais_autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()
    numero_paginas = models.IntegerField()
    fecha_publicacion = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.titulo

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    run = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    correo = models.EmailField()
    def __str__(self):
        return f"{self.nombre}"

class prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    fecha_maxima_devolucion = models.DateField()
    estado = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id_libro.titulo} - {self.id_usuario.nombre}"