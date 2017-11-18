from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm

# Create your models here.
class User(AbstractUser):
    dob = models.DateField(null=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        return self.first_name

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'dob'
        ]
