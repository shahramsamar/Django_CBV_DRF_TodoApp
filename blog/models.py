from django.db import models


'''
    this is a class to define posts for blog app
'''
class Post(models.Model):
    image = models.ImageField(null=True, blank= True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    status = models.BooleanField()
    created_date  = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    
    def __str__(self) :
        return self.title