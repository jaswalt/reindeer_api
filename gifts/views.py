# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from users.models import User

# Create your views here.
class GiftsView(View):
    """View to handle requests to /api/vX/users/X/gifts/"""

    def get(self, _request, user_id):
        """Method for GET /api/vX/users/X/gifts/"""
        gifts = User.objects.get(pk=user_id).gift_set.all()
        gifts = serializers.serialize('json', gifts)
        return JsonResponse(gifts, safe=False)

    def post(self, request, _user_id):
        """Method for POST /api/vX/users/X/gifts/"""
        print(json.loads(request.body))
        return HttpResponse()


def index(request):
    """GET /"""
    # TODO: Change to actual index page when ready
    return render(request, 'soon.html')
