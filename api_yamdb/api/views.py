import uuid

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import UserMePermission
from .serializers import GetTokenSerializer, UserMeSerializer, UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'username'


class UserMeViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = UserMeSerializer
    permission_classes = (UserMePermission,)

    def get_object(self):
        return get_object_or_404(User, username=self.request.user)


class SignupView(APIView):

    def post(self, request):
        from_email = None
        confirmation_code = str(uuid.uuid4())
        serializer = UserMeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')
        if User.objects.filter(email=email).exists():
            send_mail(username, confirmation_code, from_email, [email])
            user = get_object_or_404(User, email=email)
            user.confirmation_code = confirmation_code
            user.save()
            return Response(
                {'username': str(username),
                 'email': str(email)},
                status=status.HTTP_200_OK)
        send_mail(username, confirmation_code, from_email, [email])
        serializer.save(confirmation_code=confirmation_code)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTokenView(APIView):

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        user = User.objects.get(username=username)
        token = str(RefreshToken.for_user(user).access_token)
        return Response(
            {'token': str(token)},
            status=status.HTTP_200_OK)
