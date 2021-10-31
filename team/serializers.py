from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Team

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "username",
      "first_name",
      "last_name",
    )

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team