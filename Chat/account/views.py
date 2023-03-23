from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, View
from .forms import CustomSignUpForm

# Create your views here.


class SignUpView(CreateView):
    success_url = 'accounts/login/'
    template_name = 'allauth/account/signup.html'
    model = User
    form_class = CustomSignUpForm


class LoginView(View):
    model = User
    form_class = CustomSignUpForm
    success_url = '/'