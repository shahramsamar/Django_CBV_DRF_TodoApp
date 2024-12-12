
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.v1.serializer import PostSerializer
from ...models import Post

@api_view()
def post_list(request):
    return Response("ok")

@api_view()
def post_detail(request, id):
    post = Post.objects.get(pk=id)
    # print(post.__dict__)
    serializer = PostSerializer(post)
    # print(serializer.__dict__)
    return Response(serializer.data)
