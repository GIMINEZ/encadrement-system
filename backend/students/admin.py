# from django.contrib import admin
from django.contrib import admin
from .models import (
    Student, StudentContact, StudentHealth,
    StudentAcademic, StudentMilitary, StudentClothing,
    StudentHousing, StudentDocument
)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("matricule", "prenom", "nom", "sexe", "date_naissance", "nationalite")
    search_fields = ("matricule", "prenom", "nom")
    list_filter = ("sexe", "nationalite")

admin.site.register(StudentContact)
admin.site.register(StudentHealth)
admin.site.register(StudentAcademic)
admin.site.register(StudentMilitary)
admin.site.register(StudentClothing)
admin.site.register(StudentHousing)
admin.site.register(StudentDocument)