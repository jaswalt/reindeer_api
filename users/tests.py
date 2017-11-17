from django.test import TestCase

from .models import User

# Create your tests here.

class UserModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username = 'johndoe', 
            password = 'testing',
            first_name = 'John', 
            last_name = 'Doe',
            email = 'test@testing.com',
            dob = '1999-09-09',
        )
    

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.first_name)
    
    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
