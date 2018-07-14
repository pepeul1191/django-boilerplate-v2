# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
  context = {'saludo': 'hola mundo'}
  return render(request, 'login/index.html', context)
