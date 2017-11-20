# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=30)
    price_cents = models.IntegerField()
    sku = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    gifts = models.ManyToManyField(Gift)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'price_cents', 'sku']

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'date', 'gifts']