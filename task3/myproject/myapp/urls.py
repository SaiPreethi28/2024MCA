from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]
