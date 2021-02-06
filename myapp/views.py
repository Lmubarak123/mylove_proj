from django.shortcuts import render
from django.http import HttpResponse
from.models import Lovers
# Create your views here.
def input(request):
    return render(request,'input.html')
def insert(request):
    firstlv1=request.POST['t1']
    secondlv1=request.POST['t2']
    sweet=request.POST['t3']
    favcolor=request.POST['t4']
    oneword=request.POST['t5']
    f=Lovers(firstlv1=firstlv1,secondlv1=secondlv1,sweet=sweet,favcolor=favcolor,oneword=oneword,)
    f.save()
    return render(request,'lov.html')

