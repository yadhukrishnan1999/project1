from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@csrf_exempt
def employee_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        employee1 = employee.objects.all()
        serializer = EmployeeSerializer(employee1, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        employee2 = employee.objects.get(pk=pk)
    except employee2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee2)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


