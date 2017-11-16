# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Gift, Wishlist

# Register your models here.
admin.site.register(Gift)
admin.site.register(Wishlist)
