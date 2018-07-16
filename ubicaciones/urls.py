from django.conf.urls import url
from . import _departamento as departamento

urlpatterns = [
  url(r'^/departamento/listar$', departamento.listar, name='listar'),
]
