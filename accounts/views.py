from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import CustomUserCreationForm  # Import your custom form

User = get_user_model()  # Ensure the correct user model is used


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_message = "Logged in successfully!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_list')


class RegisterView(SuccessMessageMixin, FormView):
    template_name = "registration/register.html"  
    form_class = CustomUserCreationForm  # Use the custom form
    success_url = reverse_lazy('login')  
    success_message = "Account created successfully! You can now log in."

    def form_valid(self, form):
        user = form.save(commit=False)  # Save without committing to set additional fields if needed
        user.save()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your registration. Please check the form and try again.")
        return super().form_invalid(form)
