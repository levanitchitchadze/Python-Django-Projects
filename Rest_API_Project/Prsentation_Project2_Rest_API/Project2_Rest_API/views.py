from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Employees
from . serializers import EmployeesSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class EmployeeList(APIView):
    def get(self, request):
        employees1=Employees.objects.all()
        serializer=EmployeesSerializer(employees1, many=True)
        return Response(serializer.data)


@api_view(('GET',))  
def Details(request,pk):
    employees1=Employees.objects.get(id=pk)
    serializer=EmployeesSerializer(employees1, many=False)
    return Response(serializer.data)


@api_view(('POST',))  
def Create(request):
    serializer=EmployeesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


    

@api_view(('POST',))  
def Update(request,pk):
    employees1=Employees.objects.get(id=pk)
    serializer=EmployeesSerializer(instance=employees1, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(('DELETE',))  
def Delete(request,pk):
    employees1=Employees.objects.get(id=pk)
    employees1.delete()

    return Response('Item succesesfully delete!')