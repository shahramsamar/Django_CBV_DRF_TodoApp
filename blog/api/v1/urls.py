from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'  


urlpatterns = [
    path('post/', views.PostList, name="post_list"),
]
