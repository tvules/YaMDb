from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Title, Review, Comment
from users.models import ROLE_CHOICES

User = get_user_model()

forbidden_names = ('me', 'admin', 'moderator')


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=ROLE_CHOICES, required=False)

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "bio", "role"
        )

    def validate_username(self, value):
        if value in forbidden_names:
            raise serializers.ValidationError(
                'Выберете другое имя')
        return value


class UserMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "bio", "role"
        )
        read_only_fields = ("role",)

    def validate_username(self, value):
        if value in forbidden_names:
            raise serializers.ValidationError(
                'Выберете другое имя')
        return value


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email")

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


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор модели Review."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, attrs):
        if self.context.get('request').method != "POST":
            return attrs

        author = self.context.get('request').user
        title = get_object_or_404(
            Title,
            pk=self.context.get('view').kwargs.get('title_id'),
        )

        if title.reviews.filter(author=author).exists():
            return serializers.ValidationError(
                'Нельзя оставлять больше одного отзыва.'
            )

        return attrs


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
