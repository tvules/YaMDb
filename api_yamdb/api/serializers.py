from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Title, Review, Comment


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
