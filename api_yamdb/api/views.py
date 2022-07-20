from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from reviews.models import Title
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet модели Review."""

    serializer_class = ReviewSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly | IsStaffOrReadOnly,
    )

    def get_title_obj(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        title = self.get_title_obj()
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title_obj())
