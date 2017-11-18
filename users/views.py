# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(_request):
    """GET /api/vX/users/"""
    return HttpResponse("Hello, world. You're at the users index.")

def show(_request, user_id):
    """GET api/vX/users/X"""
    return HttpResponse(f"Hello, {user_id}")
