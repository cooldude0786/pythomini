import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import urllib3
# Create your views here.


def profile(request):
    return render(request, "profile.html")


def register(request):
    return render(request, "register.html")


def upload(request):
    if request.method == 'POST':
        msg = ""
        r=""
        error_ms = False
        details = {
            "NgoName": request.POST['NgoName'],
            "slogan": request.POST['slogan'],
            "Vision": request.POST['Vision'],
            "founderstmt": request.POST['founderstmt'],
            "StartDate": request.POST['StartDate'],
            "type": request.POST['type'],
            "originState": request.POST['originState'],
            "officialwebsite": request.POST['officialwebsite'],
            "stength": request.POST['stength']
        }
        for i in details:
            r += i+"="+details[i]+"&"
            if i == "officialwebsite":
                if not checkurl(details[i]):
                    error_ms = True
        if error_ms:
            messages.add_message(request, messages.ERROR,details)
            return HttpResponseRedirect('/profile/register?'+r)
        return HttpResponseRedirect('/profile/register')
    var1 = request.GET['abc']
    return HttpResponse("welldone")


def checkurl(url):
    try:
        requests.get(url)
        return True
    except:
        return False
