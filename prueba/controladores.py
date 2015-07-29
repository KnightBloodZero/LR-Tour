from django.db import models
from django import forms
from prueba.models import SugerenciaLugar
from prueba.models import Region
from prueba.models import Ruta

class controladorVistaSugerencias(models.Model):

    def mostrarSugerencias(self):
        consulta = SugerenciaLugar.objects.all()
        Lista = []
        for obj in consulta:
            Lista.append(obj)
        return Lista

    def crearSugerencia(nombreDelaSugerenciaACrear, regionDelaSugerenciaACrear, ciudadDelaSugerenciaACrear, comunaDelaSugerenciaACrear, imagenDelLugarDelaSugerenciaACrear, razonDeVisitaDelaSugerenciaACrear):
        nuevaSugerencia = SugerenciaLugar(nombreDelLugar=nombreDelaSugerenciaACrear,region=regionDelaSugerenciaACrear,ciudad=ciudadDelaSugerenciaACrear,comuna=comunaDelaSugerenciaACrear,imagenDelLugar=imagenDelLugarDelaSugerenciaACrear,razonDeVisita=razonDeVisitaDelaSugerenciaACrear)
        nuevaSugerencia.save()
        return nuevaSugerencia

class controladorVistaMostrarRegiones(models.Model):
    
    def mostrarRegiones(self):
        consulta = Region.objects.all()
        Lista = []
        for obj in consulta:
            Lista.append(obj)
        return Lista

class controladorRutas(models.Model):
    
    def llamarAModeloRuta(self):
        return Ruta

    def InstanciaDeRuta(self):
        nuevo = Ruta()
        return nuevo

    def obtenerListaDeRutasDelUsuarioActual(request, self):
            print('I')
            usuarioActual = request.user
            print('II')
            listaDeRutasDelUsuario = Ruta.objects.get(usuario=usuarioActual)
            print('III')
            return listaDeRutasDelUsuario




