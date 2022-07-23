from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GetTokenView, SignupView, UserMeViewSet, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path(
        'v1/users/me/',
        UserMeViewSet.as_view(
            {'get': 'retrieve', 'patch': 'partial_update'}),
        name='userme_view'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignupView.as_view(), name='signup_view'),
    path('v1/auth/token/', GetTokenView.as_view(), name='gettoken_view'),
]
