import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
import re

from ngoprofile.models import Ngo_Details
# Create your views here.


def extract_iframe_src_value(html):
    # Define regular expression to match the src attribute value of the first <iframe> tag
    iframe_src_regex = re.compile(r'<iframe.*?src="(.*?)".*?>', re.IGNORECASE)

    # Extract the src attribute value and return it as a string enclosed in double quotes
    match = re.search(iframe_src_regex, html)
    if match:
        return f'{match.group(1)}'

    return html


def profile(request):
    if request.method == 'POST':
        ngonam_value = request.POST['ngoname']
        results = ''
        if ngonam_value:
            results = Ngo_Details.objects.filter(
                Q(ngoname__contains=ngonam_value)).values()
        results = list(results)
    if request.method == 'GET':
        ngonam_value = request.GET['name']
        results = ''
        if ngonam_value:
            results = Ngo_Details.objects.filter(
                Q(ngoname__contains=ngonam_value)).values()
        results = list(results)
    return render(request, "profile.html", {'data': results[0]})


def register(request):
    return render(request, "register.html")


def upload(request):
    if request.method == 'POST':
        msg = "false"
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
            "stength": request.POST['stength'],
            "googleLocation": extract_iframe_src_value(request.POST['loc'])
        }
        # print(details)
        for i in details:
            r += i+"="+str(details[i])+"&"
            if i == "officialwebsite":
                if not checkurl(details[i]) :
                    error_ms = True
                    msg="The Url didn't Exists in the Internet or <br> Try after some time"
                if  searchUrl(details[i])  :
                    error_ms = True
                    msg="The Url For the Given NGO already Present."
        if error_ms:
            messages.add_message(request, messages.ERROR, msg)
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
        obj.googleLocation = details["googleLocation"]
        obj.save()
        return HttpResponseRedirect('/profile?name='+details["NgoName"])
        # return HttpResponse(details)
    # var1 = request.GET['abc']


def checkurl(url):
    try:
        requests.get(url)
        return True
    except:
        return False
def searchUrl(url):
    if Ngo_Details.objects.filter(url__exact=url).exists():
        # print("found")
        return True
    else:
        # print("Not-found")
        return False
