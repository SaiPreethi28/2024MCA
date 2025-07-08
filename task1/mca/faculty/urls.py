from django.urls import path
from .import views

urlpatterns=[

   path('murali/',views.murali,name='murali'),
   path('chandra/',views.chandra,name='chandra'),
   path('praveen/',views.praveen,name='praveen'),
]





