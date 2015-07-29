from django.db import models
from django import forms
from django.contrib.auth.models import User

class Mayo(models.Model):
         cantidad = models.CharField(max_length=30)
         mayiktor = models.CharField(max_length=30)

class Usuario(forms.Form):
        nombre = forms.CharField(max_length=30)
        contra = forms.CharField(max_length=30)

class FormularioReporte(models.Model):
        nombreUsuario = models.CharField(max_length=30)
        asunto = models.CharField(max_length=30)
        descripcion = models.CharField(max_length=30)

class Region(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)  

class Comuna(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey(Region)
    descripcion = models.CharField(max_length=30)  

class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey(Region)
    comuna = models.ForeignKey(Comuna)
    descripcion = models.CharField(max_length=30)

class Lugar(models.Model):
    nombreDelLugar = models.CharField(max_length=30)
    region = models.ForeignKey(Region)
    ciudad = models.ForeignKey(Ciudad)
    comuna = models.ForeignKey(Comuna)
    imagenDelLugar = models.CharField(max_length=30)
    razonDeVisita = models.CharField(max_length=30)

class SugerenciaLugar(models.Model):
    nombreDelLugar = models.CharField(max_length=30)
    region = models.ForeignKey(Region)
    ciudad = models.ForeignKey(Ciudad)
    comuna = models.ForeignKey(Comuna)
    imagenDelLugar = models.CharField(max_length=30)
    razonDeVisita = models.CharField(max_length=30)

    def __str__(self):
        return self.nombreDelLugar 

class Ruta(models.Model):
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User)
    lugares = models.ManyToManyField(Lugar)

