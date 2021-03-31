from django.db import models


# Create your models here.

class Course(models.Model):
    h = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
