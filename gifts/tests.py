# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import unittest

from models import Gift
from models import Wishlist

# Create your tests here.

class TestGiftModel(TestCase)

def setUp(self):
    gift = Gift(name="Bob Dob")
    wishlist = Wishlist(title="BEST LIST EVER", date="09022018")

def test_gift(self):
    self.assertInstance()

 