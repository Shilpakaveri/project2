from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def add(requet):
    x=requet.POST["t1"]
    y=requet.POST["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("The sum is:"+str(z))
    return res