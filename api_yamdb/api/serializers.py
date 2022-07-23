from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from users.models import ROLE_CHOICES

User = get_user_model()

forbidden_names = ('me', 'admin', 'moderator')


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "bio", "role",)

    def validate_username(self, value):
        if value in forbidden_names:
            raise serializers.ValidationError(
                'Выберете другое имя')
        return value


class UserMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "bio", "role",)
        read_only_fields = ("role",)

    def validate_username(self, value):
        if value in forbidden_names:
            raise serializers.ValidationError(
                'Выберете другое имя')
        return value


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        user = get_object_or_404(User, username=username)
        input_confirmation_code = data.get('confirmation_code')
        if input_confirmation_code != user.confirmation_code:
            raise serializers.ValidationError(
                'Введите действующий код подтверждения.')
        return data
