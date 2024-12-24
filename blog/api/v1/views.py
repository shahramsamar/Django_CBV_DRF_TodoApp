from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from blog.api.v1.permission import IsOwnerOrReadOnly
from blog.api.v1.paginations import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


#  """"""""""""""""""""""""""(ModelViewSet in CBV)"""""""""""""""""""""""""""""""""""""""
class PostModelViewSet(viewsets.ModelViewSet):
    """ getting a CRUD for posts"""
    permission_classes =[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_fields = {'status':['exact']}
    # Search_fields =['title']
    ordering_fields = ['created_date']