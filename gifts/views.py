# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from users.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class GiftsView(View):

    def get(self, request, user_id):
        gifts = User.objects.get(pk=user_id).gift_set.all()
        gifts = serializers.serialize('json', gifts)
        return JsonResponse(gifts, safe=False)

    @csrf_exempt
    def post(self, request, user_id):
        print(request.POST)
        return HttpResponse()