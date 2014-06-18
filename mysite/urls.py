#encoding:utf-8
from django.conf.urls import *
from mysite.views import current_datetime
# Descomenta las siguientes 2 lineas para habilitar el administrador:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^time/$', current_datetime),
    # Ejemplos:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Descomente admin/doc en la linea siguiente para hablitar la documentación del administrador:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Descomenta la siguientes linea para habilitar el administrador:
    # url(r'^admin/', include(admin.site.urls)),
)
