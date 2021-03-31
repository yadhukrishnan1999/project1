from django.contrib import admin
from django.urls import path,include
from . import views
app_name='home'

urlpatterns = [
    path('',views.home ,name='home'),
    path('login/',views.login),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit')
] 