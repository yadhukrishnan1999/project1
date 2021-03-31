from django.contrib import admin
from .models import employee


# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'salary')
admin.site.register(employee)
