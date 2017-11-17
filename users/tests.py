from django.test import TestCase

from .models import User

# Create your tests here.

class UserModelTests(TestCase):

    def test_string_representation(self):
        user = User(first_name="TestName")
        self.assertEqual(str(user), user.first_name)
