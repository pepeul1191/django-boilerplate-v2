# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from error.views import methodNotAllow
from .helpers import index_css, index_js
from main.constants import constants

def index(request):
  if request.method == 'GET':
    locals = {
      'title': 'Home',
      'mensaje': '',
      'csss': index_css(),
      'jss': index_js(),
    }
    return render(request, 'home/index.html', locals)
  else:
    return HttpResponse(methodNotAllow(), status = 500)
