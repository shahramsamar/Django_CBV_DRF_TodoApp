from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "name": "title",
                "placeholder": "enter the title",
            }
        ),
        label="",
    )
    
    class Meta:

        model = Post
        fields = ['title','content','status'] 
        # fields = ['author','title','content','status','category','published_date'] 