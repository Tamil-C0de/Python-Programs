from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('gm/', views.gm_view),
    path('gn/', views.gn_view),
]