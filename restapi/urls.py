from django.contrib import admin
from django.urls import path,include
from restapi import views

urlpatterns = [
    path('employee_list/', views.employee_list),
    path('employee_detail/<int:pk>', views.employee_detail),
]
