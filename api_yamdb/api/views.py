from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets

from .permissions import UserMePermission, UserPermission
from .serializers import UserMeSerializer, UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)


class UserMeViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = UserMeSerializer
    permission_classes = (UserMePermission,)

    def get_object(self):
        return self.request.user
