import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm
from decouple import config
from geotext import GeoText
# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+config('API_KEY')
    citie = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        data_recieved = request.POST
        city_name = data_recieved['name']
        city_name = city_name.title()
        places = GeoText(city_name)
        city_check = places.cities

        #for checking the city name and if already exsist
        if(city_name in city_check):
            form.save()            
        else:
            return redirect('index')


    form = CityForm()
    weather_data=[]

    for city in citie:

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
