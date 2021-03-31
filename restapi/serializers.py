from rest_framework import serializers
from restapi.models import employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['name','age','salary']
