from django.urls import path
from . import views

urlpatterns = [
    path('green/',views.green,name='green'),
##    path('green1/', views.green1, name='green1'),
]
