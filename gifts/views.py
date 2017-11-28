# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .models import GiftSerializer, Gift, WishlistSerializer, Wishlist
from .upc_api import ProductInfo


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


class GiftHoldingsView(APIView):
    """View to handle requests to /api/vX/users/X/gifts/X/hold"""

    def patch(self, request, user_id, gift_id):
        """Method for PATCH /api/vX/users/X/gifts/X/hold"""
        gift = User.objects.get(pk=user_id).gift_set.get(pk=gift_id)
        if gift.holder is None:
            gift.holder = request.user
            gift.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, user_id, gift_id):
        """Method for DELETE /api/vX/users/X/gifts/X/hold"""
        gift = User.objects.get(pk=user_id).gift_set.get(pk=gift_id)
        if gift.holder is not None:
            gift.holder = None
            gift.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def search(request, query):
    gifts = ProductInfo.fetch_search_info(query)
    return Response(gifts)


@api_view(['GET'])
def getUserWishlists(request, userId):
    wishlists = Wishlist.objects.all().filter(user_id=userId)
    serialized_wishlists = WishlistSerializer(wishlists, many=True)
    return Response(serialized_wishlists.data)


@api_view(['GET'])
def getWishlistGifts(request, userId, wishlistId):
    wishlist = Wishlist.objects.get(pk=wishlistId)
    gifts = wishlist.gifts.all()
    serialized_gifts = GiftSerializer(gifts, many=True)
    return Response(serialized_gifts.data)


@api_view(['POST'])
def postSearchGiftToGifts(request, user_id):
    """Method for POST /api/vX/users/X/gifts/add"""
    gift = json.loads(request.body)['gift']
    print(gift)
    add_gift = Gift(
        name=gift['name'],
        price=gift['price'],
        sku=0,
        user_id=user_id,
        description=gift['description'],
        photo=gift['image']
    )
    add_gift.save()
    return Response(status=status.HTTP_201_CREATED)


def index(request):
    """GET /"""
    # TODO: Change to actual index page when ready
    return render(request, 'soon.html')
