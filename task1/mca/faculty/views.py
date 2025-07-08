from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def murali(request):
    return render(request,'murali.html')


def chandra(request):
    return render(request,'chandra.html')

def praveen(request):
    return render(request,'praveen.html')

