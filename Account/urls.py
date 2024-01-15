from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'Account' 

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_api'), 
    path('registration/', UserRegistrationView.as_view(), name='registration_api'),
]
