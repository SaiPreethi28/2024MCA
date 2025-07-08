from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def page1(request):
    return render(request,'page1.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def page4(request):
    return render(request,'page4.html')

def page5(request):
    return render(request,'page5.html')

def page6(request):
    return render(request,'page6.html')

