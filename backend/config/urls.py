"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from students.views import (
    StudentViewSet, StudentContactViewSet, StudentHealthViewSet,
    StudentAcademicViewSet, StudentMilitaryViewSet, StudentClothingViewSet,
    StudentHousingViewSet, StudentDocumentViewSet
)

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'student-contacts', StudentContactViewSet)
router.register(r'student-health', StudentHealthViewSet)
router.register(r'student-academics', StudentAcademicViewSet)
router.register(r'student-military', StudentMilitaryViewSet)
router.register(r'student-clothing', StudentClothingViewSet)
router.register(r'student-housing', StudentHousingViewSet)
router.register(r'student-documents', StudentDocumentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
