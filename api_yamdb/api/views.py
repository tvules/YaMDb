import uuid

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import (
    mixins, response, status, views, viewsets, permissions, pagination
)
from rest_framework_simplejwt.tokens import RefreshToken

from .pagination import UserPagination
from .permissions import (
    IsAdminPermission, IsAuthorOrReadOnly, IsStaffOrReadOnly
)
from .serializers import (
    GetTokenSerializer, SignupSerializer, UserMeSerializer, UserSerializer,
    ReviewSerializer, CommentSerializer
)
from reviews.models import Title

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminPermission,)
    pagination_class = UserPagination
    lookup_field = 'username'


class UserMeViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = UserMeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(User, username=self.request.user)


class SignupView(views.APIView):

    def post(self, request):
        from_email = None
        confirmation_code = str(uuid.uuid4())
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')
        send_mail(username, confirmation_code, from_email, [email])
        serializer.save(confirmation_code=confirmation_code)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class GetTokenView(views.APIView):

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        user = User.objects.get(username=username)
        token = str(RefreshToken.for_user(user).access_token)
        return response.Response(
            {'token': str(token)},
            status=status.HTTP_200_OK
        )


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet модели Review."""

    serializer_class = ReviewSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly | IsStaffOrReadOnly,
    )
    pagination_class = pagination.LimitOffsetPagination

    def get_title_obj(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        title = self.get_title_obj()
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title_obj())


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly | IsStaffOrReadOnly,
    )
    pagination_class = pagination.LimitOffsetPagination

    def get_review_obj(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        review = self.get_review_obj()
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review_obj())
