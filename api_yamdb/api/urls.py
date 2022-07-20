from django.urls import include, path
from rest_framework import routers

from .views import TitleViewSet, GenreViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genres',)
router.register(r'titles', TitleViewSet, basename='titles',)
router.register(r'categories', CategoryViewSet, basename='categories',)


urlpatterns = [
    path('', include(router.urls)),
]
