from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '4cd0fee60a5d8c82002e6c25b134b28d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&metric&appid=' + appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm


    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
    all_cities.append(city_info)
    context = {
        'all_info': all_cities,
        'form': form
    }
    print(res)
    return render(request, 'weather/index.html', context)


def info(request):
    return render(request, 'weather/info.html')


def main(request):
    return render(request, 'weather/main.html')

