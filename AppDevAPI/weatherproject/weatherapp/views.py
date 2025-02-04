import requests
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'weatherapp/index.html') 

def get_weather(request):  
    city = request.GET.get('city', 'Manila')  
    api_key = 'ba6fffdb56dbc7f390f03c05f61b54d5'  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if response.status_code == 200 and 'main' in data and 'weather' in data:
            weather_data = {
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'city': data['name']
            }
        else:
            weather_data = {'error': 'City not found or API issue'}

    except Exception as e:
        weather_data = {'error': str(e)}

    return JsonResponse(weather_data)
