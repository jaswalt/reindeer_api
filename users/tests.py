from django.test import TestCase

from .models import User, UserForm


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

    def test_username_uniqueness(self):
        user_form = UserForm({'username': 'johndoe'})
        self.assertEqual(user_form.errors['username'], ['A user with that username already exists.'])