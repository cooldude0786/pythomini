from django.shortcuts import render
from django.http import HttpResponse
from werkzeug.utils import redirect
from django.http import HttpResponseRedirect
# Create your views here.

  
def Login(request):
    data = {'key':'products'}
    # for p in products:
        # print(p.image.url)
        
    return render(request,'login.html',{'data':data})


def loggedin(request):
    data = {'key':'error'}
    context = data
    if request.method == 'POST':
        email = request.POST['InputEmail']
        passw = request.POST['InputPassword']
        # if passw != " ":
        #     obj1={'pass':"empty password"}
        #     pass
        url = "/login/"
        # return HttpResponse("gdone ")
        return HttpResponseRedirect(url)
    else:
 
        print("this else run")
        return render(request,'login.html',{'data':data})
