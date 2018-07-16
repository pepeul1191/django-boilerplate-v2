from django.conf.urls import url
from . import _departamento as departamento
from . import _provincia as provincia

urlpatterns = [
  url(r'^/departamento/listar$', departamento.listar, name='listar'),
  url(r'^/departamento/guardar$', departamento.guardar, name='guardar'),
  url(r'^/provincia/listar/(?P<departamento_id>[0-9]+)$', provincia.listar, name='listar'),
  url(r'^/provincia/guardar$', provincia.guardar, name='guardar'),
]
