from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    
    
    class Meta:
        model = Post
        fields = ['title','content','status','published_date'] 
        # fields = ['author','title','content','status','category','published_date'] 