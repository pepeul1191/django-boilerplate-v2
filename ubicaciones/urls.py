from django.conf.urls import url
from . import _departamento as departamento
from . import _provincia as provincia
from . import _distrito as distrito

urlpatterns = [
  url(r'^/departamento/listar$', departamento.listar, name='listar'),
  url(r'^/departamento/guardar$', departamento.guardar, name='guardar'),
  url(r'^/provincia/listar/(?P<departamento_id>[0-9]+)$', provincia.listar, name='listar'),
  url(r'^/provincia/guardar$', provincia.guardar, name='guardar'),
  url(r'^/distrito/listar/(?P<provincia_id>[0-9]+)$', distrito.listar, name='listar'),
  url(r'^/distrito/guardar$', distrito.guardar, name='guardar'),
]
