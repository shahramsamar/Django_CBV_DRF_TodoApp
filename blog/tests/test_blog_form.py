from django.test import SimpleTestCase
from blog.forms import PostForm

class TestPostForm(SimpleTestCase):
    
    def test_post_form_with_valid_data(self):
        form = PostForm(
            data={
            "title":"test",
            "content":"test",
            "status":True,                
            })
        self.assertTrue(form.is_valid())
        
    def test_post_form_with_no_data(self):        
        form = PostForm(data={})
        self.assertFalse(form.is_valid())