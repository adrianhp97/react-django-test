from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User
from .validators import validate_username


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_verified:
            raise serializers.ValidationError('User is not verified yet.')

        return {'user': user}



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'address',
            'birthday',
            'email',
            'name',
            'password',
            'phone',
        )
        read_only_fields = ['created_at']
        extra_kwargs = {
            'birthday': { 'required': True },
            'password': { 'required': True, 'write_only': True },
            'name': { 'required': True }
        }

    @staticmethod
    def validate_email(value):
        return validate_username(value)

    def create(self, validated_data):
        return User.objects.create_user(
                    validated_data.pop('email'),
                    validated_data.pop('password'),
                    **validated_data
                )
