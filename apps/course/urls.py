from django.urls import path
from .views import CourseListAPIView, CourseContentListAPIView

urlpatterns = [
    path("", CourseListAPIView.as_view()),
    path("<int:pk>/", CourseContentListAPIView.as_view()),
]