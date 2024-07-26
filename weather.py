import requests
import json

WEATHERBIT_API_KEY = "7fddca83cfd74504a3bd1d602ef9f972"

city = input("City Name: ")


def weather(city):
    url = f"https://api.weatherbit.io/v2.0/current?city={city}&key=7fddca83cfd74504a3bd1d602ef9f972"
    response = requests.get(url)
    data = response.json()

    temp = data["data"][0]["app_temp"]
    date = data["data"][0]["datetime"]
    desc = data["data"][0]["weather"]["description"]

    print(f"Date: {date}")
    print(f"Temparature: {temp}")
    print(f"Description: {desc}")


print(weather(city))