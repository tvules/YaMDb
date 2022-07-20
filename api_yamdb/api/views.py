from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins

from reviews.models import Genre, Title, Category
from .permissions import CategoriesGenresPermission, TitlesPermission
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
)


class ListCreateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [TitlesPermission]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'genre__slug',
        'category__slug',
        'year',
        'name',
    )


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoriesGenresPermission]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [CategoriesGenresPermission]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
