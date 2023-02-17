from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import LoginSerializer,WeatherSerializer
import requests
from .models import Weather
from .paginator import WeatherPagination
from rest_framework import generics



# I AM USING THE GENERIC LISTAPI VIEW PROVIDED BY THE DRF.THIS WILL LIST ALL THE OBJECTS IN THE QUERYSET.
class WeatherListApi(generics.ListAPIView):
	authentication_classes=[SessionAuthentication]
	permission_classes=[IsAuthenticated]
	queryset=Weather.objects.all()
	serializer_class = WeatherSerializer
	pagination_class = WeatherPagination



# HERE I AM USNIG THE APIView PROVIDED BY THE DRF. THIS VIEW BASICALLY TAKES THE DATA FROM THE LOGIN PAGE SERIALIZES IT 
# AND THEN AFTER AUTHENTICATING THE DATA IT LOGS THE USER IN USING THE login() provided by the django.contrib.auth
class UserLoginView(APIView):
	authentication_classes=[SessionAuthentication]
	permission_classes=[AllowAny]
	renderer_classes = [TemplateHTMLRenderer]

	def get(self, request, format=None):
		if not request.user.is_authenticated:
			return Response(template_name="core/login.html")
		else:
			return redirect('home')

	def post(self,request,format=None):

		serializer = LoginSerializer(request.data)

		name=serializer.data.get("name")
		password=serializer.data.get("password")

		user = authenticate(name=name,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")

		return redirect("login")



# THIS IS  THE LOGOUT VIEW, IT USES THE APIview PROVIDED BY THE DRF AND BASICALLY IT JUST LOGOUT THE USER.
class UserLogoutView(APIView):
	authentication_classes=[SessionAuthentication]
	permission_classes=[IsAuthenticated]
	renderer_classes = [TemplateHTMLRenderer]
	def get(self,request,format=None):
		logout(request)
		return redirect("login")
