from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
