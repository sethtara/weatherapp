import requests
from django.shortcuts import render
# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='
    city = 'hyderabad'
    req = requests.get(url.format(city)).json()
    city_weather = {

        'city':req['name'],
        'country':req['sys']['country'],
        'actual_temp':req['main']['temp'],
        'max_temp':req['main']['temp_max'],
        'min_temp':req['main']['temp_min'],
        'humidity':req['main']['humidity'],
        'pressure':req['main']['pressure'],
        'wind_speed':req['wind']['speed'],
        'description':req['weather'][0]['description'],
        'icon':req['weather'][0]['icon'],
    }


    return render(request,'weather/weather.html',{'city_weather':city_weather})
