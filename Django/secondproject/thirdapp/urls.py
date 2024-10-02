from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.get_time),
    path('welcome/', views.home),
]