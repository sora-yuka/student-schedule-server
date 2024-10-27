from django.urls import path

from .views import FacultyListAPIView, SpecialtyListAPIView, GroupListAPIView


urlpatterns = [
    path("faculties/get/", FacultyListAPIView.as_view()),
    path("specialties/get/", SpecialtyListAPIView.as_view()),
    path("groups/get/", GroupListAPIView.as_view()),
]