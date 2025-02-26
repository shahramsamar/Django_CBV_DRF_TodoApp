from django.test import TestCase,Client
from django.urls import reverse
from accounts.models.users import User
from accounts.models.profiles import Profile
from blog.models import Post



class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@admin.com',
                                              password='a/@1234567',
                                              is_active=True)
        self.profile = Profile.objects.create(
            user = self.user, 
            first_name = 'test first_name',
            last_name = 'test last_name',
        )
        self.post = Post.objects.create(
            user = self.user ,
            title = "test",
            content = "post",
            status = True,  
            )
        
    def test_blog_list_url_successful_response(self):
        self.client.login(email='test@admin.com', password='a/@1234567')
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'post')
        self.assertTemplateUsed(response,'blog/post_list.html')

    def test_blog_post_detail_logged_in_response(self):
        #  self.client.force_login(self.user)
         self.client.login(email='test@admin.com', password='a/@1234567')
         url = reverse('blog:post_detail',kwargs={'pk': self.post.id})
         response= self.client.get(url)
         self.assertEqual(response.status_code,200)    
    
    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post_detail',kwargs={'pk':self.post.id})
        response= self.client.get(url)
        self.assertEqual(response.status_code,302)    