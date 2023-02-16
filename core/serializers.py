from rest_framework import serializers 
from .models import User,Weather

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=User  
		fields=['name','password']



class WeatherSerializer(serializers.ModelSerializer):
	class Meta:
		model=Weather
		fields=['id','city','weather_date','maximum_temperature','minimum_temperature','humidity']

		