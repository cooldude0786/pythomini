from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('register', views.register, name="register"),
    path('uploadDetail', views.upload, name='upload')
]
