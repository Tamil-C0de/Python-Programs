from django.http import HttpResponse
from django.shortcuts import render
import datetime

def get_time(request):
    time = datetime.datetime.now()
    time = time.strftime("%H:%M")
    return HttpResponse(time)

def home(request):
    return render(request, 'home.html')