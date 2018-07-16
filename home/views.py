# -*- coding: utf-8 -*-
import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from error.views import methodNotAllow
from .helpers import index_css, index_js
from main.constants import constants
from main.decorators import session_true

@session_true
def index(request):
  if request.method == 'GET':
    locals = {
      'title': 'Home',
      'mensaje': '',
      'csss': index_css(),
      'jss': index_js(),
      'menu' : json.dumps([
		{'url' : 'accesos/', 'nombre' : 'Accesos'},
        {'url' : 'maestros/', 'nombre' : 'Maestros'},
    	{'url' : 'agricultores/', 'nombre' : 'Agricultores'},
    	{'url' : 'estaciones/', 'nombre' : 'Estaciones'},
      ]),
      'items' : json.dumps([
    	{"subtitulo":"Opciones", "items":
    	  [
    		{"item":"Gestión de Sistemas","url":"#/sistema"},
    		{"item":"Gestión de Usuarios","url":"#/usuario"}
    	  ]
    	},
      ]),
      'data' : json.dumps({
        'titulo_pagina' : 'Gestión Accesos',
        'modulo' : 'Accesos'
      }),
    }
    return render(request, 'home/index.html', locals)
  else:
    return HttpResponse(methodNotAllow(), status = 500)
