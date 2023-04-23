from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from ngoprofile.models import Ngo_Details
# Create your views here.


def home(request):
    return render(request,'home.html')


def search(request):
    if request.method == 'POST':
        query = request.POST['Search']
        if query:
            results = Ngo_Details.objects.filter(
                Q(ngoname__icontains=query) |
                Q(slogan__icontains=query) |
                Q(vision__icontains=query) |
                Q(founderstmt__icontains=query) |
                Q(operatonal__icontains=query) |
                Q(fromstate__icontains=query) |
                Q(url__icontains=query) |
                Q(capacity__icontains=query)
            )
        else:
            results = Ngo_Details.objects.all()
        temp = []
        for r in results:
            if r.ngoname == "":
                continue
            temp.append({
             1:   r.ngoname,
             2:   r.slogan,
             3:   r.vision,
             4:   r.startdate,
            }
            )
        # print(temp)
        return render(request, 'ngoViewTem.html', {"data": temp})
    # return render(request, 'ngoViewTem.html')
    return HttpResponse("Internal server error")
