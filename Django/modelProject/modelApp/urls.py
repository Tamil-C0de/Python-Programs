from django.urls import path
from . import views

urlpatterns = [
    path('add-book/', views.add_book)
]