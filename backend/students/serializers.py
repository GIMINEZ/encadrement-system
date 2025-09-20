from rest_framework import serializers
from .models import (
    Student, StudentContact, StudentHealth,
    StudentAcademic, StudentMilitary, StudentClothing,
    StudentHousing, StudentDocument
)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StudentContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentContact
        fields = "__all__"

class StudentHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHealth
        fields = "__all__"

class StudentAcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAcademic
        fields = "__all__"

class StudentMilitarySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMilitary
        fields = "__all__"

class StudentClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClothing
        fields = "__all__"

class StudentHousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHousing
        fields = "__all__"

class StudentDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDocument
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    contact = StudentContactSerializer(read_only=True)
    health = StudentHealthSerializer(read_only=True)
    academic = StudentAcademicSerializer(read_only=True)
    military = StudentMilitarySerializer(read_only=True)
    clothing = StudentClothingSerializer(read_only=True)
    housing = StudentHousingSerializer(read_only=True)
    documents = StudentDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = "__all__"