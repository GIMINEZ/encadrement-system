from django.shortcuts import render

from rest_framework import viewsets
from .models import (
    Student, StudentContact, StudentHealth,
    StudentAcademic, StudentMilitary, StudentClothing,
    StudentHousing, StudentDocument
)
from .serializers import (
    StudentSerializer, StudentContactSerializer, StudentHealthSerializer,
    StudentAcademicSerializer, StudentMilitarySerializer, StudentClothingSerializer,
    StudentHousingSerializer, StudentDocumentSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentContactViewSet(viewsets.ModelViewSet):
    queryset = StudentContact.objects.all()
    serializer_class = StudentContactSerializer


class StudentHealthViewSet(viewsets.ModelViewSet):
    queryset = StudentHealth.objects.all()
    serializer_class = StudentHealthSerializer


class StudentAcademicViewSet(viewsets.ModelViewSet):
    queryset = StudentAcademic.objects.all()
    serializer_class = StudentAcademicSerializer


class StudentMilitaryViewSet(viewsets.ModelViewSet):
    queryset = StudentMilitary.objects.all()
    serializer_class = StudentMilitarySerializer


class StudentClothingViewSet(viewsets.ModelViewSet):
    queryset = StudentClothing.objects.all()
    serializer_class = StudentClothingSerializer


class StudentHousingViewSet(viewsets.ModelViewSet):
    queryset = StudentHousing.objects.all()
    serializer_class = StudentHousingSerializer


class StudentDocumentViewSet(viewsets.ModelViewSet):
    queryset = StudentDocument.objects.all()
    serializer_class = StudentDocumentSerializer

# Create your views here.
