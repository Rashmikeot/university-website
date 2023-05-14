from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api5.models import Company, ImageSlider, QuickLinks, Objectives_of_Sikkim_University, Upcoming_Events, Department, School
from api5.serializers import CompanySerializer, ImageSliderSerializer, QuickLinksSerializer, Objectives_of_Sikkim_University_Serializer, Upcoming_Events_Serializer, Department_Serializer, School_Serializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class=CompanySerializer

class ImageSliderViewSet(viewsets.ModelViewSet):
    queryset = ImageSlider.objects.all()
    serializer_class=ImageSliderSerializer

class QuickLinksViewSet(viewsets.ModelViewSet):
    queryset = QuickLinks.objects.all()
    serializer_class=QuickLinksSerializer

class Objectives_of_Sikkim_UniversityViewSet(viewsets.ModelViewSet):
    queryset = Objectives_of_Sikkim_University.objects.all()
    serializer_class=Objectives_of_Sikkim_University_Serializer

class Upcoming_Events_ViewSet(viewsets.ModelViewSet):
    queryset = Upcoming_Events.objects.all()
    serializer_class=Upcoming_Events_Serializer

class School_ViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class=School_Serializer
    @action(detail=True, methods=['get'])
    def departments(self, request, pk=None):
        print("get Employees of ",pk," company")
        try:
            school = School.objects.get(pk=pk)
            depts = Department.objects.filter(School_name=school)
            depts_serializer = Department_Serializer(depts, many=True, context={'request':request})
            return Response(depts_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': "Company or employee dowsnot exist"
            })

class Department_ViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class=Department_Serializer