# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
  locals = {
    'title': 'Login',
    'saludo': 'hola mundo',
  }
  return render(request, 'login/index.html', locals)
