from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm
from rest_framework import serializers


# Create your models here.
class User(AbstractUser):
    dob = models.DateField(null=True)
    friends = models.ManyToManyField("self", blank=True)

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'friends',
        )
        extra_kwargs = {'password': { 'write_only': True }}
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

