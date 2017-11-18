from django.test import TestCase
from .models import User, UserForm


class UserModelTests(TestCase):

    def setUp(self):
        self.user = User(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='test@testing.com',
            dob='1999-09-09',
        )
        self.user.set_password('testing')
        self.user.save()

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.first_name)

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)

    def test_username_uniqueness(self):
        user_form = UserForm({'username': 'johndoe'})
        self.assertEqual(user_form.errors['username'], ['A user with that username already exists.'])
    
    def test_password_should_not_be_plain_text(self):
        self.assertNotEqual(self.user.password, 'testing')

    def test_password_should_be_decodable(self):
        self.assertTrue('testing', self.user.password)
