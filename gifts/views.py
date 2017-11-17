# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from users.models import User

# Create your views here.
def index(request, user_id):
    gifts = User.objects.get(pk=user_id).gift_set.all()
    gifts = serializers.serialize('json', gifts)
    return JsonResponse(gifts, safe=False)
