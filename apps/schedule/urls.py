from django.urls import path

from .views import ScheduleListAPIView


urlpatterns = [
    path("get/", ScheduleListAPIView.as_view())
]