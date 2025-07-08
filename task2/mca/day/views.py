from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import StudentModel  
from .forms import StudentForm
#display & save form data   
def insert_student(request):
    context ={}
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_student.html", context)  
