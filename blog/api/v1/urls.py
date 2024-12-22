from django.urls import path
from blog.api.v1 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostModelViewSet,basename='post')
# router.register('category', views.CategoryModelViewSet,basename='category')
app_name = 'api-v1'  

urlpatterns = router.urls


