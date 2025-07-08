from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def red(request):
    return render(request,'red.html')


def pink(request):
    return render(request,'pink.html')

def skyblue(request):
    return render(request,'skyblue.html')

