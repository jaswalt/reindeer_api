# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=30)
    price_cents = models.IntegerField()
    sku = models.IntegerField()

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    gifts = models.ManyToManyField(Gift)

    def __str__(self):
        return self.title

class User(AbstractUser):
    dob = models.DateField(null=True)
    friends = models.ManyToManyField("self")