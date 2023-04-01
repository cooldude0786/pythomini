from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name="home"),
    path('index/search/', views.search, name="search"),
]
