from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('prueba.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
]