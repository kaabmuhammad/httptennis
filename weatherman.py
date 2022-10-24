import requests
import json
import sys

api_key="b7ad380cbd3b89bd161a3aaf7f6797b5"

lat = sys.argv[1]
lon = sys.argv[2]

url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)
data = response.json()

print("The weather in ",data["name"]," is ",data["main"]["temp"]," degrees.")