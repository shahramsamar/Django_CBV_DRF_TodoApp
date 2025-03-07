"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from accounts import views
# from django.contrib.auth.views import LogoutView


app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # path('api/v1/', include('accounts.api.v1.urls')),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
    #     path('login/',views.CustomLoginView.as_view(), name='login'),
    #     path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #     path('register/', views.RegisterView.as_view(), name='register'),
    # path('send_email/',views.send_email,name='send_email'),
    path('fetch_weather/',views.fetch_weather,name='fetch_weather'),

]
