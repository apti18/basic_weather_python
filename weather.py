from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather(city="Mumbai"):

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'


    get_details = requests.get(weather_url).json()

    return get_details

if __name__=="__main__":
    print("\n *** Weather Conditions ***")

    city = input("Enter a city name ")
    #check for empty city or spaces...
    if not bool(city.strip()):
        city = "Mumbai"
    get_details = get_weather(city)
    print("\n")
    pprint(get_details)
