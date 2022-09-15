from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')


class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post 
        fields = ('author', 'title', 'iamge', 'description', 'created_at', 'updated_at',)