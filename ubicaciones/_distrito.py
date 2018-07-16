# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sqlalchemy.sql import select
from main.databases import engine_ubicaciones, session_ubicaciones
from .models import Distrito, VWDistritoProvinciaDepartamento as VW
from main.decorators import check_csrf
from error.views import methodNotAllow

@csrf_exempt
@check_csrf
def listar(request, provincia_id):
  if request.method == 'GET':
    rpta = None
    status = 200
    try:
      conn = engine_ubicaciones.connect()
      stmt = select([Distrito.id, Distrito.nombre]).where(Distrito.provincia_id == provincia_id)
      rs = conn.execute(stmt)
      rpta = [dict(r) for r in conn.execute(stmt)]
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error en listar los distritos de la provincia',
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
    provincia_id = data['extra']['provincia_id']
    array_nuevos = []
    rpta = None
    session = session_ubicaciones()
    try:
      if len(nuevos) != 0:
        for nuevo in nuevos:
          temp_id = nuevo['id']
          s = Distrito(
            nombre = nuevo['nombre'],
            provincia_id = provincia_id,
          )
          session.add(s)
          session.flush()
          temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
          array_nuevos.append(temp)
      if len(editados) != 0:
        for editado in editados:
          session.query(Distrito).filter_by(id = editado['id']).update({
            'nombre': editado['nombre'],
          })
      if len(eliminados) != 0:
        for id in eliminados:
          session.query(Distrito).filter_by(id = id).delete()
      session.commit()
      rpta = {
        'tipo_mensaje' : 'success',
        'mensaje' : [
          'Se ha registrado los cambios en los distritos',
          array_nuevos
        ]
      }
    except Exception as e:
      status = 500
      session.rollback()
      rpta = {
        'tipo_mensaje' : 'error',
        'mensaje' : [
          'Se ha producido un error en guardar las distritos de la provincia',
          str(e)
        ]
      }
    return HttpResponse(json.dumps(rpta), status = status,)
  else:
    return HttpResponse(methodNotAllow(), status = 500)

@csrf_exempt
@check_csrf
def buscar(request):
  if request.method == 'GET':
    rpta = None
    status = 200
    try:
      nombre = request.GET.get('nombre')
      conn = engine_ubicaciones.connect()
      stmt = select([VW]).where(VW.nombre.like(nombre + '%' )).limit(10)
      rs = conn.execute(stmt)
      rpta = [dict(r) for r in conn.execute(stmt)]
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error en buscar las coincidenciasd de los nombres de distritos',
          str(e)
        ],
      }
      status = 500
    return HttpResponse(json.dumps(rpta), status = status,)
  else:
    return HttpResponse(methodNotAllow(), status = 500)

@csrf_exempt
@check_csrf
def nombre(request, distrito_id):
  if request.method == 'GET':
    rpta = None
    status = 200
    try:
      session = session_ubicaciones()
      conn = engine_ubicaciones.connect()
      distrito = session.query(VW).filter_by(id = distrito_id).first()
      rpta = distrito.nombre
      session.commit()
    except Exception as e:
      rpta = {
        'tipo_mensaje': 'error',
        'mensaje': [
          'Se ha producido un error en buscar en nombre del distrito',
          str(e)
        ],
      }
      status = 500
    return HttpResponse(json.dumps(rpta), status = status,)
  else:
    return HttpResponse(methodNotAllow(), status = 500)
