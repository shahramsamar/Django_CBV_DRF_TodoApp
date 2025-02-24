from django.urls import path
from accounts.api.v1 import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name='api-v1'

urlpatterns = [

        # registration
    path(
        "registration/",views.RegistrationApiView.as_view(), name="registrations"
    ),
      # login token
    path(
        "token/login/",views.CustomObtainAuthToken.as_view(), name="token-login"
    ),
      # logout token
    path(
        "token/logout/",views.CustomDiscardAuthToken.as_view(), name="token-logout"
    ),
        # change password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),





       # custom jwt token
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt_create",
    ),
        # refresh jwt token
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"
    ),
    # verify jwt token
    path("api/token/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
]
