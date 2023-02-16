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


class WeatherListApi(generics.ListAPIView):
	authentication_classes=[SessionAuthentication]
	permission_classes=[IsAuthenticated]
	queryset=Weather.objects.all()
	serializer_class = WeatherSerializer
	pagination_class = WeatherPagination


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



class UserLogoutView(APIView):
	authentication_classes=[SessionAuthentication]
	permission_classes=[IsAuthenticated]
	renderer_classes = [TemplateHTMLRenderer]
	def get(self,request,format=None):
		logout(request)
		return redirect("login")




# def home(request):
# 	data=dict(requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Siliguri&appid=7f09ced009234bc55b64960b5284ac6d").json())
# 	return render(request,"core/home.html",{"city":data})


# class WeatherApiView(APIView):
# 	def get(self,request,format=None):
# 		return HttpResponse("<h1>Get weather</h1>")
# 	def post(self,request,format=None):
# 		city=["Siliguri","Delhi","Mumbai","Pune","Bangalore","Hyderabad","Ahmedabad","Chennai","Kolkata","Surat","Vadodara","Pune","Jaipur",
# 		"Lucknow","Kanpur","Nagpur","Indore","Thane","Patna","Ghaziabad","Ludhiana","Agra","Nashik","Meerut","Srinagar","Gwalior","Jabalpur","Jodhpur","Dhanbad","Guwahati"]
# 		for city in city:
# 			data=dict(requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f09ced009234bc55b64960b5284ac6d").json())
# 			time=data.get("dt")
# 			date = datetime.date.fromtimestamp(int(time))

# 			data={
# 			"city":data.get("name"),
# 			"weather_date":str(date),
# 			"maximum_temperature":data.get("main")["temp_max"],
# 			"minimum_temperature":data.get("main")["temp_min"],
# 			"humidity":data.get("main")["humidity"],
# 			}

# 			serializer=WeatherSerializer(data=data)
# 			if serializer.is_valid():
# 				serializer.save()
# 			else:
# 				print(serializer.errors)
# 		return redirect("home")

