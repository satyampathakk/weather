from django.shortcuts import render,redirect
from django.http import HttpResponse 
import json
import urllib.request



def index(request):
    return render(request,'index.html')

def search(request):
    api_key = 'adb81a9664f84bc6a9da6a3aea16df3a'

    if request.method == 'POST':
        loc = request.POST.get('loc')  

        if loc:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={loc}&appid={api_key}'

            try:
                response = urllib.request.urlopen(url)
                json_data = json.loads(response.read())
                data = {
                    "country": json_data['sys']['country'],
                    "temp": float(json_data['main']['temp'])-273 ,
                    "pressure": json_data['main']['pressure'],
                    "humidity": json_data['main']['humidity'],
                }
            except Exception as e:
                data = {
                    'error_message': str(e),
                }
            return render(request, 'index.html', data)
        else:
            data = {
                'error_message': 'Please enter a location.',
            }
    else:
        data = {}

    return render(request, 'index.html', data)


