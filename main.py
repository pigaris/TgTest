import requests
import datetime
from pprint import pprint
from config import open_weather_token 

def get_weather(city, open_weather_token):

    code_to_smile = {
    "Clear": "Clear \u2600",
    "Clouds": "Clouds \u2601",
    "Rain": "Rain \u2614",
    "Drizzle": "Drizzle \u2614",
    "Thunderstorm": "Thunderstorm \u26A1",
    "Snow": "Snow \u1F328",
    "Mist": "Mist \u1F32B"
    }


    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data['main']['temp']

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "See for yourself, I can't figure out what's going on"
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Wether in the city: {city}\nTemperature: {cur_weather}C° {wd}\n"
              f'Humidity: {humidity}%\nPressure: {pressure} mmHg of the column\nWind: {wind} m/s\n'
              f'Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of the day: {length_of_the_day}\n'
              f'Have a good day!'
              )
    except Exception as ex:
        print(ex)
        print('Check name of the city')


def main():
    city = input('Enter name of the city: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()