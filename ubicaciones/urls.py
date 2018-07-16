from django.conf.urls import url
from . import _departamento as departamento
from . import _provincia as provincia
from . import _distrito as distrito

urlpatterns = [
  url(r'^/departamento/listar$', departamento.listar, name='departamento_listar'),
  url(r'^/departamento/guardar$', departamento.guardar, name='departmento_guardar'),
  url(r'^/provincia/listar/(?P<departamento_id>[0-9]+)$', provincia.listar, name='provincia_listar'),
  url(r'^/provincia/guardar$', provincia.guardar, name='provincia_guardar'),
  url(r'^/distrito/listar/(?P<provincia_id>[0-9]+)$', distrito.listar, name='distrito_listar'),
  url(r'^/distrito/buscar$', distrito.buscar, name='distrito_buscar'),
  url(r'^/distrito/guardar$', distrito.guardar, name='distrito_guardar'),
  url(r'^/distrito/nombre/(?P<distrito_id>[0-9]+)$', distrito.nombre, name='distrito_nombre'),
]
