from django.shortcuts import render
from django.http import HttpResponse
from werkzeug.utils import redirect
from django.http import HttpResponseRedirect
from Login.models import Item
# Create your views here.

  
def Login(request):
    data = {'key':'sdfsf'}
    return render(request,'login.html',{'data':data})

def loggedin(request):
    data = {'key':'error'}
    context = data
    if request.method == 'POST':
        email = request.POST['InputEmail']
        passw = request.POST['InputPassword']
        prod = Item()
        if len(request.FILES) != 0:
            prod.image = request.FILES['image']
            
        prod.save()
        if passw != " ":
            obj1={'pass':"empty password"}
            pass
        url = "/profile/"
        return HttpResponse("g=done ")
        # return HttpResponseRedirect(url)
    else:
        # return render(
        #     request,
        #     'login.html',
        #     context
        # )
        print("this else run")
        return render(request,'login.html',{'data':data})
