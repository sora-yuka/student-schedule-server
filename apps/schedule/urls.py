from django.urls import path

from .views import SemesterScheduleListAPIView, LessonListAPIView


urlpatterns = [
    path("", SemesterScheduleListAPIView.as_view()),
    path("lessons/", LessonListAPIView.as_view())
]