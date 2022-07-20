from django.urls import path, include
from rest_framework import routers

from .views import ReviewViewSet

router = routers.DefaultRouter()

router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='review',
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
