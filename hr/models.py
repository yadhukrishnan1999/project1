from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Student1(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()