from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog import views


class TestUrl(SimpleTestCase):

    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:post_list")
        self.assertEqual(resolve(url).func.view_class, views.PostListView)

    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post_detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.PostDetailView)

    def test_blog_post_create_url_resolve(self):
        url = reverse("blog:post_create")
        self.assertEqual(resolve(url).func.view_class, views.PostCreateView)

    def test_blog_post_update_url_resolve(self):
        url = reverse("blog:post_update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.PostUpdateView)

    def test_blog_post_delete_url_resolve(self):
        url = reverse("blog:post_delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.PostDeleteView)

    def test_blog_post_done_url_resolve(self):
        url = reverse("blog:post_done", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.PostDoneView)
