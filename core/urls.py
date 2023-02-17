from .views import UserLoginView,WeatherListApi,UserLogoutView
from django.urls import path  



# THESE ARE ALL THE URLS FOR THE VIEWS DEFINED IN THE views.py FILE
urlpatterns=[
	path("",UserLoginView.as_view(),name="login"),
	path("weather-api/",WeatherListApi.as_view(),name="home"),
	path("logout/",UserLogoutView.as_view(),name="logout"),
]

