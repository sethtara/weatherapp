import requests
from django.shortcuts import render
# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid='
    city = 'las vegas'
    r = requests.get(url.format(city))
    print(r.text)

    return render(request,'weather/weather.html')