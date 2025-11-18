from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, validators = [validate_password], write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        models = User
        fields = ('username', 'email', 'password', 'password2')
    
    def validate(serlf, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password" : "password fields didn't match"}
            )
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.save()
        token = Token.objects.create(user=user)
        return user
    
    