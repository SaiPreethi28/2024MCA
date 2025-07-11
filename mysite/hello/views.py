from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.http import HttpResponse
def demo(request):
    temp=loader.get_template('grid2.html')
    return HttpResponse(temp.render())