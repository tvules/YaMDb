from rest_framework import serializers

from reviews.models import Categories, Titles, Genres


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = '__all__'


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Categories.objects.all(),
    )

    class Meta:
        model = Titles
        fields = '__all__'
