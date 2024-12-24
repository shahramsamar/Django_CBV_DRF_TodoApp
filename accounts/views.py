from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_message = " is login successfully!"

    def form_valid(self, form):
        # Add the success message
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_list')


class RegisterView(SuccessMessageMixin, FormView):
    template_name = "registration/register.html"  # Update with the path to your HTML file
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    success_message = "Account created successfully! You can now log in."

    def form_valid(self, form):
        # Save the user instance
        user = form.save()
        # Add the success message
        messages.success(self.request, self.success_message)
        # Additional processing can be done here
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle errors
         # Add an error message when form validation fails
        messages.error(self.request, 
                       "There was an error with your registration. Please check the form and try again.")
        return super().form_invalid(form)
