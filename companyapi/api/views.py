from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompnyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=CompanySerializer   

    #companies/{compnyId}/employees
    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        try:
            compnay=company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=compnay)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'company not exiest'
            })

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer