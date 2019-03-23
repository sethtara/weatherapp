import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    weather_data=[]

    for city in cities:

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
            'id': city.id,
        }
        weather_data.append(city_weather)

    return render(request,'weather/weather.html',{'weather_data':weather_data,'form':form})

def delete(request,city_id):
    item = City.objects.get(pk=city_id)
    item.delete()
    return redirect('index')
