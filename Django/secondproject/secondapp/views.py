from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page.")

def gm_view(request):
    return HttpResponse("Good Morning.")

def gn_view(request):
    return HttpResponse("Good Night!")