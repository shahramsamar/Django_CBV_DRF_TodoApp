from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is required

    class Meta:
        model = User  # Use the custom user model
        fields = [ "email", "password1", "password2"]  # Adjust based on your fields

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
