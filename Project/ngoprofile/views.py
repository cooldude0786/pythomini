from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request):
    return render(request,"profile.html")
def register(request):
    return render(request,"register.html")

def upload(request):
    if request.method == 'POST':
        
        return HttpResponse("good")
    return HttpResponse("welldone")