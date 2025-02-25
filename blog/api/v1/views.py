from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import viewsets
from blog.api.v1.permission import IsOwnerOrReadOnly
from blog.api.v1.paginations import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class PostModelViewSet(viewsets.ModelViewSet):
    """getting a CRUD for posts(ModelViewSet in CBV)"""
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"status": ["exact"]}
    # Search_fields =['title']
    ordering_fields = ["created_date"]
