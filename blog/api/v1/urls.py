from blog.api.v1 import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = "api-v1"


router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")


urlpatterns = [
    path('', include(router.urls)),
   
]