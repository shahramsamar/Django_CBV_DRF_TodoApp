from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DeleteView

# Create your views here.



'''
this is for show list of post 
'''    
class PostListView(ListView):
    model = Post
    template_name = "blog/post-list.html"  
    context_object_name = "posts"
    ordering = ("-id")
    # paginate_by = 1

'''
this is for show detail of post 
'''  
class PostDetailView(DeleteView):
    model = Post
    template_name = "blog/post-detail.html"            
