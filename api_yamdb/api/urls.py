from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserMeViewSet, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'users/me', UserMeViewSet, basename='me')

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'auth/token/', TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
]
