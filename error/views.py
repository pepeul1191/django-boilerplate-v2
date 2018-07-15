# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect
from .helpers import access_css, access_js
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
    return HttpResponse(json.dumps(error), status = 404)

def methodNotAllow():
  error = {
    'tipo_mensaje': 'error',
    'mensaje': [
      'Recurso no disponible',
      'methodNotAllow Error'
    ],
  }
  return json.dumps(error)


def access(request, numero):
  errores = {
    '404' : {
      'mensaje': 'Archivo no encontrado',
      'numero': '404',
      'descripcion': 'La página que busca no se encuentra en el servidor',
    },
    '505' : {
      'mensaje': 'Acceso restringido',
      'numero': '505',
      'descripcion': 'Necesita estar logueado',
    },
  }
  locals = {
    'title': 'Error',
    'mensaje': '',
    'csss': access_css(),
    'jss': access_js(),
    'error': errores[str(numero)]
  }
  return render(request, 'error/access.html', locals, status = 404)
