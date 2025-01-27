from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView

from .models import LessonModel, ScheduleModel
from .serializers import LessonSerializer, ScheduleSerializer

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