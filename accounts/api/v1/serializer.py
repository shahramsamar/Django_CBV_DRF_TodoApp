# from rest_framework import serializers
# from ...models import User
# from  django.contrib.auth.password_validation import validate_password 


# class RegistrationSerializer(serializers.ModelSerializer):
#     password1 = serializers.CharField(write_only=True)
#     password2 = serializers.CharField(write_only=True)


#     class Meta:
#         model = User
#         fields =['username', 'email', 'password1', 'password2']

#     # def validate(self, attrs):
#     #     if attrs.get('password1') != attrs.get('password2'):
#     #         raise serializers.ValidationError({"password2": "Passwords must match."})
#     #     try:
#     #         validate_password(attrs.get('password'))
#     #     except  exceptions.validationError as e:
#     #         raise serializers.ValidationError({'password':list(e.messages)})
#     #     return super().validate(attrs)    
#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError({"password2": "Passwords must match."})
#         return data
#     # def create(self, validated_data):
#     #     # user = User.objects.create(
#     #     #     email=validated_data['email'],
#     #     #     password=validated_data['password']
#     #     # )
#     #     # return user
#     #     validated_data.pop('password1', None)
#     #     return  User.objects.create_user(**validated_data)
#     def create(self, validated_data):
#         validated_data.pop('password2')  # Remove password2
#         validated_data['password'] = validated_data.pop('password1')  # Rename password1 to password
#         if 'username' not in validated_data:
#             raise serializers.ValidationError({"username": "This field is required."})
#         return User.objects.create_user(**validated_data)

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from accounts.models import User  # Ensure correct import
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _




class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def validate_email(self, value):
        """Check if email is already registered."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        errors = {}

        # Check if passwords match
        if data['password1'] != data['password2']:
            errors["password2"] = "Passwords must match."

        # Validate password strength
        try:
            validate_password(data['password1'])
        except DjangoValidationError as e:
            errors["password"] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2
        password = validated_data.pop('password1')  # Rename password1 to password

        # Explicitly pass email and password to avoid `username` issues
        user = User.objects.create_user(**validated_data)
        return user


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        username = attrs.get("email")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
            if not user.is_verified:
                msg = _("user is not verifying.")
                raise serializers.ValidationError(msg, code="verifying")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
