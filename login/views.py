# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from login.helpers import index_css, index_js

def index(request):
  locals = {
    'title': 'Login',
    'mensaje': '',
    'csss': index_css(),
    'jss': index_js(),
  }
  return render(request, 'login/index.html', locals)
