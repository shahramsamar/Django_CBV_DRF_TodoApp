from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
# from accounts.models import User
from accounts.models.users import User


"""
Post:
    - This model defines the structure for blog posts in the blog app.
    - Fields:
        - `image`: Optional field to upload an image for the post (null and blank are allowed).
        - `title`: Title of the post, with a maximum length of 255 characters.
        - `content`: Main body of the post, limited to 255 characters (could be increased if needed).
        - `status`: Boolean field to represent whether the post is published or in draft (True for published, False for draft).
        - `created_date`: Automatically records the date and time when the post is first created.
        - `updated_date`: Automatically updates the date and time whenever the post is modified.
        - `published_date`: The date and time when the post is officially published.
    - Methods:
        - `__str__`: Returns the title of the post when the object is printed or displayed.
"""


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})
