import requests
import json
import datetime

def valid(location):
    API = '08cccf809ef0d4a7ea3ed60b8744f222'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={API}")
    if weather_data.status_code == 200:
        return True
    return False

def get_json(location):
    while True:
        API = '08cccf809ef0d4a7ea3ed60b8744f222'
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={API}")
        if weather_data.status_code == 200:
            return weather_data

def retrive_data(location):
    weather_data = get_json(location)
    json_data = weather_data.json()

    weather_cond = json_data['weather'][0]['main']    # Variable for weather condition
    weather_disc = json_data['weather'][0]['description']  # Variable that describes the condition

    temp = json_data['main']['temp']
    temp_max = json_data['main']['temp_max']
    temp_min = json_data['main']['temp_min']
    humidity = json_data['main']['humidity']

    wind_speed = json_data['wind']['speed']
    wind_deg = json_data['wind']['deg']

    timestamp = json_data['dt']
    date = datetime.datetime.fromtimestamp(timestamp).date()
    time = datetime.datetime.fromtimestamp(timestamp).time()

    sunrise = datetime.datetime.fromtimestamp(json_data['sys']['sunrise'])
    sunrise_time = sunrise.strftime("%H:%M")
    sunrise_date = sunrise.date()

    sunset = datetime.datetime.fromtimestamp(json_data['sys']['sunset'])
    sunset_time = sunset.strftime("%H:%M")
    sunset_date = sunset.date()

    name = json_data['name']

    data_list = [
        [weather_cond, weather_disc],
        [temp, temp_max, temp_min, humidity],
        [wind_speed, wind_deg],
        [date,time],
        [sunrise_time, sunrise_date],
        [sunset_time, sunset_date],
        [name]
    ]
    return data_list



