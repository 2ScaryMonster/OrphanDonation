from django.contrib import admin
from django.urls import path,include
from Basics import views

urlpatterns = [
    path('Calculator/', views.calculation,name="calculation"),
    path('student/',views.student,name="Student"),
    path('largest/',views.largest,name="largest"),
]