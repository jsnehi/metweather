from . import views
from django.urls import path
from .views import WeatherSummaryAPIView, WeatherListAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('api/summary', WeatherSummaryAPIView.as_view(), name='api-summary'),
    path('api/weather', WeatherListAPIView.as_view(), name='api-weather'),
]
