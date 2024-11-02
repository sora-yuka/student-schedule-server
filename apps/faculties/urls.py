from django.urls import path

from .views import FacultyListAPIView, SpecialtyListAPIView, GroupListAPIView


urlpatterns = [
    path("faculties/", FacultyListAPIView.as_view()),
    path("specialties/", SpecialtyListAPIView.as_view()),
    path("groups/", GroupListAPIView.as_view()),
]