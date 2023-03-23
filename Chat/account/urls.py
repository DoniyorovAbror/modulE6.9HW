from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]
