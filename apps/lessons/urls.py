from django.urls import path

from .views import LessonsListAPIView

urlpatterns = [
    path("all/", LessonsListAPIView.as_view()),
]