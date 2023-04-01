from django.shortcuts import render
from django.http import HttpResponse
from werkzeug.utils import redirect
from django.http import HttpResponseRedirect
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
        if passw != " ":
            obj1={'pass':"empty password"}
            pass
        url = "/profile/"
        return HttpResponseRedirect(url)
    else:
        # return render(
        #     request,
        #     'login.html',
        #     context
        # )
        print("this else run")
        return render(request,'login.html',{'data':data})
