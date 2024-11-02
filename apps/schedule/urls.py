from django.urls import path

from .views import ScheduleListAPIView


urlpatterns = [
    path("", ScheduleListAPIView.as_view())
]