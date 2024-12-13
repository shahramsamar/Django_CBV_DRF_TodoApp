
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
 


@api_view()
def post_list(request):
    posts = Post.objects.filter(status=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view()
def post_detail(request, id):
    # try:
    #     post = Post.objects.get(pk=id)
    #     # print(post.__dict__)
    #     serializer = PostSerializer(post)
    #     # print(serializer.__dict__)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     # return Response({'detail':'post dose not exist'},status=404)
    #     return Response({'detail':'post dose not exist'},status=status.HTTP_404_NOT_FOUND)
    post = get_object_or_404(Post, pk=id, status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)
