from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Meal


def meal_list(request):
    ob_meals = Meal.objects.all()
    return render(request, 'meal_list.html', {'meals': ob_meals})

def meal_detail(request, pk):
    ob_meal = get_object_or_404(Meal, pk=pk)
    return render(request, 'meal_detail.html', {'meal': ob_meal})

