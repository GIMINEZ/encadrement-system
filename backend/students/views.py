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
from .permissions import IsAdminOrOwner


# --- Student principal ---
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return Student.objects.all()   # Admin → voit tout
        return Student.objects.filter(user=user)  # Élève → seulement lui-même

    def perform_create(self, serializer):
        if self.request.user.role == "student":
            serializer.save(user=self.request.user)
        else:
            serializer.save()


# --- Contacts ---
class StudentContactViewSet(viewsets.ModelViewSet):
    queryset = StudentContact.objects.all()
    serializer_class = StudentContactSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return StudentContact.objects.all()
        return StudentContact.objects.filter(student__user=user)


# --- Santé ---
class StudentHealthViewSet(viewsets.ModelViewSet):
    queryset = StudentHealth.objects.all()
    serializer_class = StudentHealthSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return StudentHealth.objects.all()
        return StudentHealth.objects.filter(student__user=user)


# --- Académique ---
class StudentAcademicViewSet(viewsets.ModelViewSet):
    queryset = StudentAcademic.objects.all()
    serializer_class = StudentAcademicSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return StudentAcademic.objects.all()
        return StudentAcademic.objects.filter(student__user=user)


# --- Militaire ---
class StudentMilitaryViewSet(viewsets.ModelViewSet):
    queryset = StudentMilitary.objects.all()
    serializer_class = StudentMilitarySerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return StudentMilitary.objects.all()
        return StudentMilitary.objects.filter(student__user=user)


# --- Habillement ---
class StudentClothingViewSet(viewsets.ModelViewSet):
    queryset = StudentClothing.objects.all()
    serializer_class = StudentClothingSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return StudentClothing.objects.all()
        return StudentClothing.objects.filter(student__user=user)


# --- Hébergement ---
class StudentHousingViewSet(viewsets.ModelViewSet):
    queryset = StudentHousing.objects.all()
    serializer_class = StudentHousingSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return StudentHousing.objects.all()
        return StudentHousing.objects.filter(student__user=user)


# --- Documents ---
class StudentDocumentViewSet(viewsets.ModelViewSet):
    queryset = StudentDocument.objects.all()
    serializer_class = StudentDocumentSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return StudentDocument.objects.all()
        return StudentDocument.objects.filter(student__user=user)
# Create your views here.
