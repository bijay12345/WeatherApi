import requests
import time
import datetime
from django.core.management.base import BaseCommand
from core.models import Weather


# HERE I HAVE DEFINED A CUSTOM DJANGO COMMAND IT FETCHES THE DATA AND SAVES THE DATA TO THE DATABASE

class Command(BaseCommand):
    help = 'Fetch weather data from OpenWeatherMap and store it in the database'

    def handle(self, *args, **options):
        cities=["Siliguri","Delhi","Mumbai","Pune","Bangalore","Hyderabad","Ahmedabad","Chennai","Kolkata","Surat","Vadodara","Noida","Jaipur",
        "Lucknow","Kanpur","Nagpur","Indore","Thane","Patna","Ghaziabad","Ludhiana","Agra","Nashik","Meerut","Srinagar","Gwalior","Jabalpur","Jodhpur","Dhanbad","Guwahati"]
 

        # HERE WE ARE RUNNING AN INFINITE LOOP THAT WILL SLEEP FOR 30 MINTES AND FETCH THE DATA FROM openweathermap.org,
        # SAVE THE DATA IF INSTANCE DOESN'T EXISTS OR UPDATE IT IF THE INSTANCE EXISTS.

        while True:
            for city in cities:
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f09ced009234bc55b64960b5284ac6d'
                response = requests.get(url)
                data = response.json()

                dtime=data.get("dt")
                date = datetime.date.fromtimestamp(int(dtime))

                weather_date=str(date),
                maximum_temperature=data.get("main")["temp_max"],
                minimum_temperature=data.get("main")["temp_min"],
                humidity=data.get("main")["humidity"],

            # SINCE THE DATA IS ALREADY IN THE JSON FORMAT WE WILL NOT BE SERIALIZING IT AND SAVING IT DIRECTLY TO THE DATABASE.

                weather,created=Weather.objects.update_or_create(
                    city=data.get("name"),
                    defaults={
                    "weather_date":str(date),
                    "maximum_temperature":data.get("main")["temp_max"],
                    "minimum_temperature":data.get("main")["temp_min"],
                    "humidity":data.get("main")["humidity"]
                    }
                )    

            
            time.sleep(1800) 