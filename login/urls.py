from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'acceder$', views.acceder, name='acceder'),
  url(r'ver$', views.ver, name='ver'),
  url(r'salir$', views.salir, name='salir'),
]
