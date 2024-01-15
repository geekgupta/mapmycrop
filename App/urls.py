from django.urls import path
from .views import WeatherAPIView

app_name = 'App'  # Add name of the app 
urlpatterns = [
    path('weather/', WeatherAPIView.as_view(), name='weather_api'),
]
