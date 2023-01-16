from django.shortcuts import render
from .models import Location, WeatherData
# Create your views here.


def location_detail(request, location_id):
    location = Location.objects.get(id=location_id)
    weather_data = WeatherData.objects.filter(location=location)
    context = {'location': location, 'weather_data': weather_data}
    return render(request, 'index.html', context)
