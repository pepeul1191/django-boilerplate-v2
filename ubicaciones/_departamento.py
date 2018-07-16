# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from sqlalchemy.sql import select
from main.databases import engine_ubicaciones
from .models import Departamento

def listar(request):
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
