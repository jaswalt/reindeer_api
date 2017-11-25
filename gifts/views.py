# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .models import GiftSerializer

# Create your views here.
class GiftsView(APIView):
    """View to handle requests to /api/vX/users/X/gifts/"""

    def get(self, request, user_id, gift_id):
        """Method for GET /api/vX/users/X/gifts/"""
        gifts = User.objects.get(pk=user_id).gift_set.all()
        serialized_gifts = GiftSerializer(gifts, many=True)
        return Response(serialized_gifts.data)

    def post(self, request, user_id, gift_id):
        """Method for POST /api/vX/users/X/gifts/"""
        print(json.loads(request.body))
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, user_id, gift_id):
        """Method for DELETE /api/vX/users/X/gifts/X"""
        User.objects.get(pk=user_id).gift_set.get(pk=gift_id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)


def index(request):
    """GET /"""
    # TODO: Change to actual index page when ready
    return render(request, 'soon.html')
