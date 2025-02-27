from django.test import TestCase
from blog.models import Post
from accounts.models.users import User
from accounts.models.profiles import Profile


class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com", password="a/@1234567"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test_first_name",
            last_name="test_last_name",
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            user=self.user,
            title="test",
            content="description",
            status=True,
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title, "test")
