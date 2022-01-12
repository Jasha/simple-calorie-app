from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from calorie.core.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('name', 'password', 'email')
        extra_kwargs = {
            'name': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class InviteSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('name', 'email')
        extra_kwargs = {
            'name': {'required': True},
        }

    def create(self, validated_data):
        email = validated_data['email']

        user = User.objects.create(
            name=validated_data['name'],
            email=email,
        )

        user.set_password(email.split('@')[0])
        user.save()

        return user


class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    is_superuser = serializers.BooleanField()
    calories_threshold = serializers.IntegerField()
