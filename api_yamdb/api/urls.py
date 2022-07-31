from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    SignupView,
    TitleViewSet,
    UserMeViewSet,
    UserViewSet,
)

app_name = 'api'

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='review',
)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comment',
)

urlpatterns = [
    path(
        'v1/users/me/',
        UserMeViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}),
        name='userme_view',
    ),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignupView.as_view(), name='signup_view'),
    path('v1/auth/token/', views.gettoken_view, name='gettoken_view'),
]
