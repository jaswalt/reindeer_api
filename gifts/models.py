# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.forms import ModelForm
from rest_framework import serializers


# Create your models here.
class Gift(models.Model):
    """GIFT MODEL"""
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    sku = models.IntegerField(blank=True)
    description = models.TextField()
    photo = models.CharField(max_length=255)
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='holds',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'price', 'sku']


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = (
            'id',
            'name',
            'price',
            'sku',
            'description',
            'photo',
            'user',
            'holder'
        )


class Wishlist(models.Model):
    """WISHLIST MODEL"""
    title = models.CharField(max_length=255)
    date = models.DateField()
    gifts = models.ManyToManyField(Gift)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'date', 'gifts']


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('id', 'title', 'date', 'gifts')
