# from django.shortcuts import redirect, render
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib import messages


# class CustomLoginView(LoginView):
#     redirect_authenticated_user = True
#     success_message = " is login successfully!"

#     def form_valid(self, form):
#         # Add the success message
#         messages.success(self.request, self.success_message)
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('blog:post_list')


# class RegisterView(SuccessMessageMixin, FormView):
#     template_name = "registration/register.html"  # Update with the path to your HTML file
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')  # Redirect to login page after successful registration
#     success_message = "Account created successfully! You can now log in."

#     def form_valid(self, form):
#         # Save the user instance
#         user = form.save()
#         # Add the success message
#         messages.success(self.request, self.success_message)
#         # Additional processing can be done here
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         # Handle errors
#          # Add an error message when form validation fails
#         messages.error(self.request,
#                        "There was an error with your registration. Please check the form and try again.")
#         return super().form_invalid(form)

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.cache import cache
import requests
from django.views.decorators.cache import cache_page
# import time
# from .tasks import send_email

# def send_email(request):
#     time.sleep(3)
#     # send_email.delay()
#     return HttpResponse("<h1>done sending </h1>")

# def test(request):
#     if cache.get("test_delay_api") is None:
#         response = requests.get("")
#         cache.set("test_delay_api",response.json())
#     return JsonResponse(cache.get("test_delay_api")) 

# @cache_page(60)
# def test(request):
#     response = requests.get("")
#     return JsonResponse(response.json())    

@cache_page(60*20)
def fetch_weather(request):
    # https://api.openweathermap.org/data/2.5/weather"?lat={lat}&lon={lon}&appid={API key}
    params = {"lat":35.69,"lon":51.42,"appid":"00e7ad1f702afa36c308e10a55cba3ef"}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    response = response.json()
    # print(response['weather'][0]['main'])
    # return JsonResponse(response['weather'][0]['main'])
    weather = response['weather'][0]['main']
    return HttpResponse(weather)
