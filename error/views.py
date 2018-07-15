# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect
from login.helpers import index_css, index_js
from django.http import HttpResponse
from main.constants import constants

def handler404(request):
  if request.method == 'GET':
    return  redirect(constants['base_url'] + 'error/access/404')
  else:
    error = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Recurso no disponible',
        'Error 404'
      ],
    }
    return HttpResponse(json.dumps(error))


def access(request, numero):
  locals = {
    'title': 'error',
    'mensaje': '',
    'csss': index_css(),
    'jss': index_js(),
  }
  return render(request, 'error/access.html', locals)
