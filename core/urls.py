from .views import UserLoginView,WeatherListApi,UserLogoutView
from django.urls import path  


urlpatterns=[
	path("",UserLoginView.as_view(),name="login"),
	path("weather-api/",WeatherListApi.as_view(),name="home"),
	path("logout/",UserLogoutView.as_view(),name="logout"),
]

