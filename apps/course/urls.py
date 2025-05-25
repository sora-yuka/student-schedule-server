from django.urls import path
from .views import CourseListAPIView, CourseContentRetrieveAPIView

urlpatterns = [
    path("", CourseListAPIView.as_view()),
    path("<int:pk>/", CourseContentRetrieveAPIView.as_view()),
]