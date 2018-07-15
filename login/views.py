# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests.exceptions import ConnectionError
from django.views.decorators.csrf import csrf_exempt
from error.views import methodNotAllow
from .helpers import index_css, index_js
from main.constants import constants

def index(request):
  if request.method == 'GET':
    locals = {
      'title': 'Login',
      'mensaje': '',
      'csss': index_css(),
      'jss': index_js(),
    }
    return render(request, 'login/index.html', locals)
  else:
    return HttpResponse(methodNotAllow(), status = 500)

@csrf_exempt
def acceder(request):
  if request.method == 'POST':
    mensaje = ''
    continuar = True
    try:
      usuario = request.POST.get('usuario')
      # validar usuario/sistema
      r1 = requests.post(
        constants['servicios']['accesos']['url'] + 'sistema/usuario/validar',
        headers = {
          constants['servicios']['accesos']['key'] : constants['servicios']['accesos']['secret'],
        },
        params = {
          'usuario' : usuario,
          'sistema_id' : constants['sistema_id'],
        }
      )
      if r1.status_code == 200:
        if r1.text != '1':
          continuar = False
          mensaje = 'Usuario no se encuentra registrado en el sistema'
      else:
        continuar = False
        mensaje = 'Se ha producido un error no esperado al validar usuario/sistema'
    except ConnectionError as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'No se puede acceder al servicio de validación de usuario/sistema',
          str(e)
        ],
      }
      print(rpta)
      mensaje = rpta['mensaje'][0]
      continuar = False
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error no controlado al validar usuario/sistema',
          str(e)
        ],
      }
      print(rpta)
      mensaje = rpta['mensaje'][0]
      continuar = False
    # validar usuario/contrasenia
    if continuar == True:
      try:
        usuario = request.POST.get('usuario')
        contrasenia = request.POST.get('contrasenia')
        # validar usuario/sistema
        r2 = requests.post(
          constants['servicios']['accesos']['url'] + 'usuario/externo/validar',
          headers = {
            constants['servicios']['accesos']['key'] : constants['servicios']['accesos']['secret'],
          },
          params = {
            'usuario' : usuario,
            'contrasenia' : contrasenia,
          }
        )
        if r2.status_code == 200:
          if r2.text != '1':
            continuar = False
            mensaje = 'Usuario y/o contraseña no coincide'
          else:
            # TODO, habilitar la session
            return redirect(constants['base_url'])
        else:
          continuar = False
          mensaje = 'Se ha producido un error no esperado al validar usuario/contraseña'
      except ConnectionError as e:
        rpta = {
          'tipo_mensaje': 'error',
          'mensaje': [
            'No se puede acceder al servicio de validación de usuario/contrasenia',
            str(e)
          ],
        }
        print(rpta)
        mensaje = rpta['mensaje'][0]
        continuar = False
      except Exception as e:
        rpta = {
          'tipo_mensaje': 'error',
          'mensaje': [
            'Se ha producido un error no controlado al validar usuario/contrasenia',
            str(e)
          ],
        }
        print(rpta)
        mensaje = rpta['mensaje'][0]
        continuar = False
    locals = {
      'title': 'Login',
      'mensaje': mensaje,
      'csss': index_css(),
      'jss': index_js(),
    }
    return render(request, 'login/index.html', locals, status = 500)
  else:
    return HttpResponse(methodNotAllow(), status = 500)
