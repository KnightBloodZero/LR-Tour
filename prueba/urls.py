from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Portada, name='Portada'),
    url(r'^login/$', views.propioLogin, name='login'),
    url(r'^registrarse/$', views.registrarse, name='registrarse'),
    url(r'^report/$', views.vistaAdministrarReportes, name='vistaAdministrarReportes'),
    url(r'^nuevolugar/$', views.sugerirNuevoLugar, name='nuevolugar'),
    url(r'^suge/$', views.vistaAdministrarSugerencias, name='vistaAdministrarSugerencias'),
    url(r'^lugares/$', views.vistaMostrarRegiones, name='vistaMostrarRegiones'),
    url(r'^moderador/$', views.vistaPrincipalModerador, name='vistaPrincipalModerador'),
    url(r'^ruta/$', views.vistaPrincipalRutas, name='vistaPrincipalRutas'),
    url(r'^configruta/$', views.vistaConfigurarRuta, name='vistaConfigurarRuta'),
    url(r'^sugerirlugar/$', views.sugerirNuevoLugar, name='sugerirNuevoLugar')
]


