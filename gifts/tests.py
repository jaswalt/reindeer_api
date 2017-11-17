# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Gift, GiftForm
from users.models import User

# Create your tests here.
class TestGiftModel(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username = 'johndoe', 
            password = 'testing',
            first_name = 'John', 
            last_name = 'Doe',
            email = 'test@testing.com',
            dob = '1999-09-09',
        )

        self.gift = self.user.gift_set.create(
            name = 'Book Book',
            price_cents = '7024',
            sku= '53434',
        )

    def test_string_representation(self):
        self.assertEqual(str(self.gift), self.gift.name)

    def test_gift(self):
        self.assertIsInstance(self.gift, Gift)

    def test_gift_name_length(self):
        gift_form = GiftForm({'name': 'Bob Dob'})
        self.assertFalse(gift_form.is_valid())