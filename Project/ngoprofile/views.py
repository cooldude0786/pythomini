import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

from ngoprofile.models import Ngo_Details
# Create your views here.


def profile(request):
    if request.method == 'POST':
        ngonam_value = request.POST['ngoname']
        results=''
        if ngonam_value:
            results = Ngo_Details.objects.filter(
                Q(ngoname__contains=ngonam_value)).values()
        results = list(results)
        return render(request, "profile.html", {'data': results[0]})


def register(request):
    return render(request, "register.html")


def upload(request):
    if request.method == 'POST':
        msg = ""
        r = ""
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
            messages.add_message(request, messages.ERROR, details)
            return HttpResponseRedirect('/profile/register?'+r)

        obj = Ngo_Details()
        obj.ngoname = details["NgoName"]
        obj.slogan = details["slogan"]
        obj.vision = details["Vision"]
        obj.founderstmt = details["founderstmt"]
        obj.startdate = details["StartDate"]
        obj.operatonal = details["type"]
        obj.fromstate = details["originState"]
        obj.url = details["officialwebsite"]
        obj.capacity = details["stength"]
        obj.save()
        messages.add_message(request, messages.ERROR, details)
        return HttpResponseRedirect('/profile/register?'+r)
    var1 = request.GET['abc']
    return HttpResponse("welldone")


def checkurl(url):
    try:
        requests.get(url)
        return True
    except:
        return False
