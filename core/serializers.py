from rest_framework import serializers 
from .models import User,Weather


# HERE I AM SERIALIZING THE CUSTOM USER MODEL'S FIELD [name,password] DEFINED IN THE models.py FILE

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=User  
		fields=['name','password']



# I AM USING MODEL SERIALIZER TO SERIALIZER THE WEATHER DATA PRESENT IN THE DATABASE

class WeatherSerializer(serializers.ModelSerializer):
	class Meta:
		model=Weather
		fields=['id','city','weather_date','maximum_temperature','minimum_temperature','humidity']

		