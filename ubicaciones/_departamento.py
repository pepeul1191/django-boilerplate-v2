# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sqlalchemy.sql import select
from main.databases import engine_ubicaciones, session_ubicaciones
from .models import Departamento
from main.decorators import check_csrf
from error.views import methodNotAllow

@csrf_exempt
@check_csrf
def listar(request):
  if request.method == 'GET':
    rpta = None
    status = 200
    try:
      conn = engine_ubicaciones.connect()
      stmt = select([Departamento])
      rs = conn.execute(stmt)
      rpta = [dict(r) for r in conn.execute(stmt)]
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error en listar los departamentos',
          str(e)
        ],
      }
      status = 500
    return HttpResponse(json.dumps(rpta), status = status,)
  else:
    return HttpResponse(methodNotAllow(), status = 500)

@csrf_exempt
@check_csrf
def guardar(request):
  if request.method == 'POST':
    status = 200
    data = json.loads(request.POST.get('data'))
    nuevos = data['nuevos']
    editados = data['editados']
    eliminados = data['eliminados']
    array_nuevos = []
    rpta = None
    session = session_ubicaciones()
    try:
      if len(nuevos) != 0:
        for nuevo in nuevos:
          temp_id = nuevo['id']
          s = Departamento(
            nombre = nuevo['nombre'],
          )
          session.add(s)
          session.flush()
          temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
          array_nuevos.append(temp)
      if len(editados) != 0:
        for editado in editados:
          session.query(Departamento).filter_by(id = editado['id']).update({
            'nombre': editado['nombre'],
          })
      if len(eliminados) != 0:
        for id in eliminados:
          session.query(Departamento).filter_by(id = id).delete()
      session.commit()
      rpta = {
        'tipo_mensaje' : 'success',
        'mensaje' : [
          'Se ha registrado los cambios en los departamentos',
          array_nuevos
        ]
      }
    except Exception as e:
      status = 500
      session.rollback()
      rpta = {
        'tipo_mensaje' : 'error',
        'mensaje' : [
          'Se ha producido un error en guardar los departamentos',
          str(e)
        ]
      }
    return HttpResponse(json.dumps(rpta), status = status,)
  else:
    return HttpResponse(methodNotAllow(), status = 500)
