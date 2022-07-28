import uuid

import django_filters
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (
    filters, mixins, response, status, views, viewsets, permissions, pagination
)
from rest_framework_simplejwt.tokens import RefreshToken

from reviews.models import Genre, Category, Title, Review
from .pagination import UserPagination
from .permissions import (
    IsAdminPermission, IsAuthorOrReadOnly, IsStaffOrReadOnly,
    IsAdminOrReadOnly,
)
from .serializers import (
    CategorySerializer, GenreSerializer, TitleGetSerializer,
    TitlePostSerializer, GetTokenSerializer, SignupSerializer,
    UserMeSerializer, UserSerializer, ReviewSerializer,
    CommentSerializer,
)

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
        email = request.data.get('email')
        username = request.data.get('username')

        if User.objects.filter(username=username).filter(email=email).exists():
            send_mail(username, confirmation_code, from_email, [email])
            user = User.objects.get(email=email)
            user.confirmation_code = confirmation_code
            user.save()
            return response.Response(
                {'email': str(email), 'username': str(username)},
                status=status.HTTP_200_OK)

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


class ListCreateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class TitleFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(
        field_name="genre__slug", lookup_expr='icontains'
    )
    category = django_filters.CharFilter(
        field_name="category__slug", lookup_expr='icontains'
    )
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Title
        fields = [
            'genre',
            'category',
            'year',
            'name',
        ]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleGetSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in {'list', 'retrieve'}:
            return TitleGetSerializer
        return TitlePostSerializer


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = "slug"


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = "slug"


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
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        review = self.get_review_obj()
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review_obj())
