import datetime
from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView

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
    
    def get_queryset(self) -> QuerySet:
        current_date = datetime.date.today()
        user_profile = self.request.user.studentprofilemodel
        schedules = SemesterScheduleModel.objects.all()
        current_schedule = []
        
        for schedule in schedules:
            if schedule.onset <= current_date <= schedule.end:
                current_schedule.append(schedule)
        
        return SemesterScheduleModel.objects.filter(id__in=[item.id for item in current_schedule])