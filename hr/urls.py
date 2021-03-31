from django.contrib import admin
from django.urls import path,include
from . import views
app_name='hr'

urlpatterns = [
    path('about/',views.hr_about,name='about'),
    path('login/',views.hr_login),
    path('register/',views.register,name='register'),
    path('studregister/',views.studRegister,name='studregister'),
    path('sendemail/',views.send_email,name='sendemail')

]