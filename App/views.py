from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openmeteo_requests

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import validate_email
from retry_requests import retry
import requests_cache
import pandas as pd
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.authentication import TokenAuthentication


class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        start_date = request.data['start_date']
        end_date = request.data['end_date']

        if not all([latitude, longitude, start_date, end_date]):
            return Response({"error": "latitude, longitude, start_date, and end_date are required parameters."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            return Response({"error": "latitude and longitude must be valid floating-point numbers."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)


        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
            "hourly": "temperature_2m"
        }

        try:
            responses = openmeteo.weather_api(url, params=params)
            response = responses[0]

            coordinates = {"latitude": response.Latitude(), "longitude": response.Longitude()}
            elevation = response.Elevation()
            timezone_info = {"timezone": response.Timezone(), "timezone_abbreviation": response.TimezoneAbbreviation()}
            utc_offset_seconds = response.UtcOffsetSeconds()

            hourly = response.Hourly()
            hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

            hourly_data = {
                "date": pd.date_range(
                    start=pd.to_datetime(hourly.Time(), unit="s"),
                    end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
                    freq=pd.Timedelta(seconds=hourly.Interval()),
                    inclusive="left"
                ).tolist(),
                "temperature_2m": hourly_temperature_2m.tolist()
            }

            result = {
                "coordinates": coordinates,
                "elevation": elevation,
                "timezone_info": timezone_info,
                "utc_offset_seconds": utc_offset_seconds,
                "hourly_data": hourly_data
            }

            return Response(result)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
