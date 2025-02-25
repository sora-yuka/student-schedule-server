import datetime
from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import LessonModel, ScheduleModel, SemesterScheduleModel
from .serializers import LessonSerializer, ScheduleSerializer, SemesterScheduleSerializer

# Create your views here.


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = LessonModel.objects.all()


class ScheduleListAPIView(ListAPIView):
    serializer_class = ScheduleSerializer
    
    def get_queryset(self) -> QuerySet:
        user_profile = self.request.user.studentprofilemodel
        queryset = ScheduleModel.objects.filter(group=user_profile.group)
        return queryset
    
    
class SemesterScheduleListAPIView(ListAPIView):
    queryset = SemesterScheduleModel.objects.all()
    serializer_class = SemesterScheduleSerializer
    
    def get_object(self) -> SemesterScheduleModel:
        current_date = timezone.now().date()
        user_profile = self.request.user.studentprofilemodel

        current_schedule = SemesterScheduleModel.objects.filter(
            onset__lte=current_date,
            end__gte=current_date,
            course=user_profile.course
        )

        if not current_schedule:
            print("No schedule found for this date")

        return current_schedule