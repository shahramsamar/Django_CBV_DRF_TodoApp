from django.shortcuts import render
from blog.forms import PostForm
from blog.models import Post
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView




"""
PostListView:
    - A class-based view to display a list of all blog posts.
    - Uses the 'blog/post-list.html' template to render the list.
    - The context variable for posts is 'posts'.
    - The posts are ordered by the 'id' field in descending order.
    - Pagination can be enabled by setting 'paginate_by'.
"""  
class PostListView(ListView):
    model = Post
    template_name = "blog/post-list.html"  
    context_object_name = "posts"
    ordering = ("-id")
    # paginate_by = 1

"""
PostDetailView:
    - A class-based view to display details of a specific blog post.
    - Uses the 'blog/post-detail.html' template for rendering.
    - Displays detailed information for a single post instance.
"""
class PostDetailView(DeleteView):
    model = Post
    template_name = "blog/post-detail.html"   
             
"""
PostCreateView:
    - A class-based view to handle the creation of new blog posts.
    - Renders a form to create a post with fields: 'title', 'content', 'status', and 'published_date'.
    - Upon successful creation, the user is redirected to the homepage ("/").
    - Uses the 'blog/post-form.html' template for the form rendering.
"""
class PostCreateView(CreateView):
    model = Post 
    fields = ['title','content','status','published_date']
    success_url = '/'
    template_name = "blog/post-form.html" 
    
    
class PostUpdateView( UpdateView):
    '''
    a class  based UpdateView to show post_form page
    '''  
    model = Post 
    form_class = PostForm
    success_url = '/'    
    template_name = "blog/post-form.html" 


class PostDeleteView(DeleteView):
    '''
    a class  based DeleteView to show post_form page
    '''  
    model = Post 
    success_url = '/'
    template_name = "blog/post-confirm-delete.html" 