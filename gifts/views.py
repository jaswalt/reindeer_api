# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, user_id):
    return HttpResponse(f"Hello, {user_id}")
