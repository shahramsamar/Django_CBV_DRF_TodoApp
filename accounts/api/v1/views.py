from rest_framework import generics, status
from rest_framework.response import Response
from accounts.api.v1.serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ActivationResendApiSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from ...models import User, Profile
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from accounts.api.v1.utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.conf import settings
import jwt


class RegistrationApiView(generics.GenericAPIView):
    """this view for simple register"""

    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation_email.tpl",
                {"token": token},
                "shahramsamar2010@gmail.com",
                to=[email],
            )
            EmailThread(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomObtainAuthToken(ObtainAuthToken):
    """this view for create token for user"""

    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "email": user.email}
        )


class CustomDiscardAuthToken(APIView):
    """this view for delete token user"""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    """this view for login with jwt token"""

    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        Serializer = self.get_serializer(data=request.data)
        if Serializer.is_valid():
            if not self.object.check_password(
                Serializer.data.get("old_password")
            ):
                return Response(
                    {"old_password": ["Warning password"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(Serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"detail": "change password successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class ActivationApiView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(
                token, settings.SECRET_KEY, algorithms=["HS256"]
            )
            user_id = token.get("user_id")
        except ExpiredSignatureError:
            return Response(
                {"details": "token has been expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except InvalidSignatureError:
            return Response(
                {"details": "token is not valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_obj = User.objects.get(pk=user_id)
        if user_obj.is_verified:
            return Response(
                {"details": "your account has already been verified"}
            )
        user_obj.is_verified = True
        user_obj.save()
        return Response(
            {
                "details": "your account have you been verified and activated successfully"
            }
        )
        # return Response (token)


class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = ActivationResendApiSerializer

    def post(self, request, *args, **kwargs):
        serializer = ActivationResendApiSerializer(data=request.data)
        if serializer.is_valid():
            user_obj = serializer.validated_data["user"]
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation_email.tpl",
                {"token": token},
                "shahramsamar2010@gmail.com",
                to=[user_obj.email],
            )
            EmailThread(email_obj).start()
            return Response(
                {"detail": "user activation resend successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"details": "invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
