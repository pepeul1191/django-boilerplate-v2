from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'access/(?P<numero>[0-9]+)$', views.access, name='access'),
]
