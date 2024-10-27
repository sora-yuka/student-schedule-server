from django.urls import path

from .views import LessonsListAPIView

urlpatterns = [
    path("get/", LessonsListAPIView.as_view()),
]