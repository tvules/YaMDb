from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "bio", "role",)

    def validate_username(self, value):
        if value == "me":
            raise serializers.ValidationError(
                'Недопустимое имя')
        return value


class UserMeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "bio", "role",)
        read_only_fields = ("role",)

    def validate_username(self, value):
        if value == "me":
            raise serializers.ValidationError(
                'Недопустимое имя')
        return value
