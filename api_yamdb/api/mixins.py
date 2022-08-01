from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import mixins, serializers, viewsets

User = get_user_model()


class ListCreateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class BaseUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value in settings.FORBIDDEN_NAMES:
            raise serializers.ValidationError('Выберете другое имя')
        return value
