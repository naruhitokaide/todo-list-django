from django.contrib.auth.models import User
from rest_framework import serializers

from lists.models import TodoList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login', 'date_joined',
                  'email', 'todolists')

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'created_at', 'creator')