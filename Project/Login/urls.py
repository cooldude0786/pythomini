from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name="LoginPage"),
    path('logged',views.loggedin,name='loggedin'),
]
