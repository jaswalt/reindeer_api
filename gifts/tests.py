# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Gift
from users.models import User

# Create your tests here.
class TestGiftModel(TestCase)

def setUp(self):
    self.gift = Gift.objects.create(
        name='Bob Dob',
        price_cents='7024',
    )

def test_string_representation(self):
    self.assertEqual(str(self.gift), self.gift.name)

def test_gift(self):
    self.assertIsInstance(self.gift, gift)

def test_gift_name_length(self):
    gift_form = GiftForm({'name': 'Bob Dob'})
    self.assertFalse(gift_form.is_valid())