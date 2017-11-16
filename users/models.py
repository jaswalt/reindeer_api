from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    dob = models.DateField(null=True)
    friends = models.ManyToManyField("self")