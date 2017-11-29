# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.forms import ModelForm
from rest_framework import serializers
import random



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
    image = models.CharField(max_length=255, blank=True, null=True)
    gifts = models.ManyToManyField(Gift)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image is None:
            pics = [
                'http://s1.1zoom.me/big0/449/345838-admin.jpg',
                'https://www.legarrick.co.uk/wp-content/uploads/2014/05/xmas-le-garrick-700x400.jpg',
                'http://www.goodwp.com/images/201211/goodwp.com_25947.jpg',
                'http://longwallpapers.com/Desktop-Wallpaper/gold-holiday-wallpapers-for-iphone-For-Desktop-Wallpaper.jpg',
                'http://starliteloungewinebar.com/wp-content/uploads/new-years-glassware-700x614.jpg',
                'http://www.crossfitbothell.com/wp-content/uploads/2016/12/eating-chocolate-daily-is-good-for-health980-1456212647_980x457.jpg',
                'http://www.goodwp.com/large/201103/15589.jpg',
                'https://i.pinimg.com/736x/a5/0a/96/a50a96b6f408404cc71a014652708d77--christmas-wedding-christmas-drinks.jpg',
                'https://i.pinimg.com/originals/63/c2/90/63c290f0666144c5662d5b374d3bf295.jpg'
            ]
            self.image = random.choice(pics)

        super(Wishlist, self).save(*args, **kwargs)



class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'date', 'gifts', 'image']


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('id', 'title', 'date', 'gifts', 'image')


