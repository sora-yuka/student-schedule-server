from django.urls import path

from .views import LessonsListAPIView


urlpatterns = [
    path("", LessonsListAPIView.as_view()),
]