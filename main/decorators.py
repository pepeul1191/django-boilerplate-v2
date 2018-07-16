import json
from django.http import HttpResponse
from django.shortcuts import redirect
from main.constants import constants

def enable_cors(fn):
  def _enable_cors(*args, **kwargs):
    # set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    if bottle.request.method != 'OPTIONS':
      # actual request; reply with the actual response
      return fn(*args, **kwargs)
  return _enable_cors

def check_csrf(fn):
  def _check_csrf(request, *args, **kwargs):
    #si csrf en el header NO coincide
    if constants['ambiente_csrf'] == 'activo':
      continuar = True
      mensaje = []
      if request.META.get('HTTP_' + constants['csrf']['key'].upper()) != None:
        if request.META.get('HTTP_' + constants['csrf']['key'].upper()) != constants['csrf']['secret']:
          continuar = False
          mensaje = [
            'No se puede acceder al recurso',
            'CSRF Token key error'
          ]
      else:
        continuar = False
        mensaje = [
          'No se puede acceder al recurso',
          'CSRF Token error no encontrado'
        ]
      if continuar == True:
        return fn(request, *args, **kwargs)
      else:
        rpta = {
          'tipo_mensaje' : 'error',
          'mensaje' : mensaje
        }
        return HttpResponse(json.dumps(rpta), status = 500,)
      return fn(request, *args, **kwargs)
    else:
      return fn(request, *args, **kwargs)
  return _check_csrf

def session_false(fn):
  def _session_false(request, *args, **kwargs):
    #si la session es activaa, vamos a '/accesos/'
    if constants['ambiente_session'] == 'activo':
      s = request.session
      if s != None:
        if s.has_key('activo') == True:
          if s['activo'] == True:
            return redirect('/')
      return fn(request, *args, **kwargs)
    #else: contnuar
    else:
      return fn(request, *args, **kwargs)
  return _session_false

def session_true(fn):
  def _session_true(request, *args, **kwargs):
    #si la session es activaa, vamos a '/accesos/'
    if constants['ambiente_session'] == 'activo':
      s = request.session
      if s != None:
        if s.has_key('activo') == True:
          if s['activo'] == False:
            return redirect('/error/access/505')
        else:
          return redirect('/error/access/505')
      else:
        return redirect('/error/access/505')
    return fn(request, *args, **kwargs)
  return _session_true
