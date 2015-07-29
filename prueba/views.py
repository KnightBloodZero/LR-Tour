from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.template import Context, Template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django import forms
import prueba.models
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from prueba.models import SugerenciaLugar
from prueba.models import Comuna
from prueba.models import Region
from prueba.models import Ciudad
from prueba.models import Lugar
from prueba.models import Ruta
from django.db import models
from prueba.controladores import controladorVistaSugerencias
from prueba.controladores import controladorVistaMostrarRegiones
from prueba.controladores import controladorRutas


def index(request):
    mayo1 = prueba.models.Mayo()
    mayo1.cantidad = "Rojo qlo feeder"
    mayo1.mayiktor = "Chupala Zoo"
    return render(request, 'PaginaPrueba.html', {"Mayo" : mayo1})

def Portada(request):
    return render(request, 'Portada.html')

def propioLogin(request):
    if request.method == 'POST':
        form = prueba.models.Usuario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            contra = form.cleaned_data['contra']
            user = authenticate(username=nombre, password=contra)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.user.is_superuser:
                        return HttpResponseRedirect('/moderador')
                    else:
                        return HttpResponseRedirect('/lugares')
                else:
                  return

    else:
        form = prueba.models.Usuario()

    return render(request, 'Login.html', {'form': form})

def registrarsee(request):
    if request.method == 'POST':
        form = prueba.models.Usuario(request.POST)
        if form.is_valid():
            print ('1')
            nombre = form.cleaned_data['nombre']
            print ("El nombre es %s" % (request.POST['nombre']))
            print ("El nombre es %s" % (nombre))
            message = form.cleaned_data['contra']
            print ('3')
            print('4')
            return HttpResponseRedirect('/')

    else:
        form = prueba.models.Usuario()

    return render(request, 'Registrarse.html', {'form': form})


def registrarse(request):
    if request.method == 'POST':
        form = prueba.models.Usuario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            contra = form.cleaned_data['contra']
            usuario_creado = User.objects.create_user(username=nombre, email=None, password=contra)
            usuario_creado.save()
            users = User.objects.all()
            print ("Los usuarios creados hasta ahora son %s" % users)
            return HttpResponseRedirect('/')

    else:
        form = prueba.models.Usuario()

    return render(request, 'Registrarse.html', {'form': form})

def vistaAdministrarReportess(request):
    print ('1')
    WndePrueba = prueba.models.FormularioReporte()
    print ('2')
    WndePrueba.nombreUsuario = "nombre1"
    print ('3')
    WndePrueba.asunto = "asunto1"
    print ('4')
    WndePrueba.descripcion = "descripcion1"
    print ('5')
    WndePrueba2 = prueba.models.FormularioReporte()
    print ('6')
    WndePrueba2.nombreUsuario = 'nombre2'
    print ('7')
    WndePrueba2.asunto = 'asunto2'
    print ('8')
    WndePrueba2.descripcion = 'descripcion2'
    print ('9')
    ListaDeReportes = [WndePrueba, WndePrueba2]
    return render(request, 'VistaAdministrarReportes.html', {'ListaDeReportes' : ListaDeReportes})

def vistaAdministrarReportes(request):
    print ('1')
    WndePrueba = prueba.models.FormularioReporte(nombreUsuario = 'nombre1',asunto = 'asunto1',descripcion = 'descripcion1')
    print ('2')
    print ("%s" % WndePrueba.nombreUsuario)
    print ('6')
    WndePrueba2 = prueba.models.FormularioReporte(nombreUsuario = 'nombre2',asunto = 'asunto2',descripcion = 'descripcion2')
    print ('7')
    print ('9')
    ListaDeReportes = [WndePrueba, WndePrueba2]
    return render(request, 'VistaAdministrarReportes.html', {'ListaDeReportes' : ListaDeReportes})

def sugerirNuevoLugar(request):
    if request.method == 'POST':
        form = SugerenciaLugar(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombreDelLugar']
            region = form.cleaned_data['region']
            ciudad = form.cleaned_data['ciudad']
            comuna = form.cleaned_data['comuna']
            imagenDelLugar = form.cleaned_data['imagenDelLugar']
            razonDeVisita = form.cleaned_data['razonDeVisita']
            controlador = controladorVistaSugerencias()
            controlador.crearSugerencia(nombre,region,ciudad,comuna,imagenDelLugar,razonDeVisita)
            return HttpResponseRedirect('/')

    else:
        form = SugerenciaLugar()

    return render(request, 'SugerirLugar.html', {'form': form})

def vistaAdministrarSugerencias(request):
    if 'botonDeSugerencia' in request.POST:
            valor = request.POST['botonDeSugerencia']
            opcionSeleccionada = SugerenciaLugar.objects.get(id=valor)
            return render(request, 'BaseSugerenciasLugar.html', {'form': opcionSeleccionada})
    controlador = controladorVistaSugerencias()
    ListaDeSugerencias = controlador.mostrarSugerencias()
    return render(request, 'VistaAdministrarSugerencias.html', {'ListaDeSugerencias': ListaDeSugerencias})

def vistaMostrarRegiones(request):
    if 'botonDeSeleccionDeRegion' in request.POST:
            valor = request.POST['botonDeSeleccionDeRegion']
            listaDeComunasDeLaRegion = Comuna.objects.filter(region__id=valor)
            return render(request, 'VistaMostrarComunas.html', {'ListaDeComunas': listaDeComunasDeLaRegion})
    elif 'botonDeSeleccionDeComuna' in request.POST:
            valor = request.POST['botonDeSeleccionDeComuna']
            listaDeCiudadesDeLaRegion = Ciudad.objects.filter(comuna__id=valor)
            return render(request, 'VistaMostrarCiudades.html', {'ListaDeCiudades': listaDeCiudadesDeLaRegion})
    elif 'botonDeSeleccionDeCiudad' in request.POST:
            valor = request.POST['botonDeSeleccionDeCiudad']
            listaDeLugaresDeLaRegion = Lugar.objects.filter(ciudad__id=valor)
            return render(request, 'VistaMostrarLugares.html', {'ListaDeLugares': listaDeLugaresDeLaRegion})
    elif 'botonDeSeleccionDeLugar' in request.POST:
            valor = request.POST['botonDeSeleccionDeLugar']
            lugarDeterminado = Lugar.objects.get(id=valor)
            return render(request, 'BaseLugar.html', {'form': lugarDeterminado})
    elif 'botonLogout' in request.POST:
        logout(request)
        return HttpResponseRedirect('/')
    controlador = controladorVistaMostrarRegiones()
    ListaDeSugerencias = controlador.mostrarRegiones()
    usuario = request.user
    return render(request, 'VistaMostrarRegiones.html', {'ListaDeRegiones': ListaDeSugerencias, 'usuario': usuario})

def vistaPrincipalModerador(request):
    if 'botonLogout' in request.POST:
        logout(request)
        return HttpResponseRedirect('/')
    usuario = request.user
    return render(request, 'vistaPrincipalModerador.html', {'usuario': usuario})

def vistaPrincipalRutas(request):
    if 'botonDeNuevaRuta' in request.POST:
            nuevaRuta = Ruta()
            return HttpResponseRedirect('/configruta')
    usuarioActual = request.user
    listaDeRutasDelUsuario = Ruta.objects.filter(usuario__id=usuarioActual.id, lugares__isnull=False)
    return render(request, 'VistaMostrarRutas.html', {'ListaDeRutas' : listaDeRutasDelUsuario})

def vistaConfigurarRuta(request):
    if 'botonDeSeleccionDeRegion' in request.POST:
            print('Entro')
            valor = request.POST['botonDeSeleccionDeRegion']
            listaDeComunasDeLaRegion = Comuna.objects.filter(region__id=valor)
            return render(request, 'RutavistaMostrarComunas.html', {'ListaDeComunas': listaDeComunasDeLaRegion})
    elif 'botonDeSeleccionDeComuna' in request.POST:
            print('Entro')
            valor = request.POST['botonDeSeleccionDeComuna']
            listaDeCiudadesDeLaRegion = Ciudad.objects.filter(comuna__id=valor)
            return render(request, 'RutavistaMostrarCiudades.html', {'ListaDeCiudades': listaDeCiudadesDeLaRegion})
    elif 'botonDeSeleccionDeCiudad' in request.POST:
            print('Entro')
            valor = request.POST['botonDeSeleccionDeCiudad']
            listaDeLugaresDeLaRegion = Lugar.objects.filter(ciudad__id=valor)
            return render(request, 'RutavistaMostrarLugares.html', {'ListaDeLugares': listaDeLugaresDeLaRegion})
    elif 'botonDeSeleccionDeLugar' in request.POST:
            print('Entro')
            valor = request.POST['botonDeSeleccionDeLugar']
            lugarDeterminado = Lugar.objects.get(id=valor)
            return render(request, 'RutabaseLugar.html', {'form': lugarDeterminado})
    elif 'botonLogout' in request.POST:
        print('Entro')
        logout(request)
        return HttpResponseRedirect('/')
    elif 'botonDeAgregarARuta' in request.POST:
            print('Agregar a Ruta')
            valor = request.POST['botonDeAgregarARuta']
            lugarDeterminado = Lugar.objects.get(id=valor)
            print('1')
            nuevaRutaAHacer.save()
            print('2')
            nuevaRutaAHacer.lugares.add(lugarDeterminado)
            print('3')
            nuevaRutaAHacer.save()
            print('4')
            listaDeLugaresQueComponenLaRuta = Lugar.objects.filter(ruta__id=nuevaRutaAHacer.id)
            print('5')
            listaDeLugaresDeLaRegion = Lugar.objects.filter(ciudad__id=lugarDeterminado.ciudad.id)
            print('6')
            return render(request, 'RutavistaMostrarLugares.html.html', {'ListaDeLugares': listaDeLugaresDeLaRegion, 'Ruta' : listaDeLugaresQueComponenLaRuta})
    nuevo = controladorVistaMostrarRegiones()
    print('Comienzo')
    ListaDeSugerencias = nuevo.mostrarRegiones()
    usuario = request.user
    nuevaRutaAHacer = Ruta()
    lista = []
    print('Termino')
    return render(request, 'RutavistaMostrarRegiones.html', {'ListaDeRegiones': ListaDeSugerencias , 'Ruta' : lista})
