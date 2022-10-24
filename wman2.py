import json
import sys
import requests


location = sys.argv[1]

with open("UK.json") as file:
    data = json.load(file)

for i in range(0,13):
    if data["places"][i]["name"]==location:
        long=data["places"][i]["x"]
        lat=data["places"][i]["y"]
        break
else:
    print("Sorry location not found")

api_key="b7ad380cbd3b89bd161a3aaf7f6797b5"

url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, long, api_key)

response = requests.get(url)
data = response.json()
# print(data)

print("The weather in ",location," is ",data["main"]["temp"]," degrees.")

