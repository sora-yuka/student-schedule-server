from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView

from .models import ScheduleModel
from .serializers import ScheduleSerializer

# Create your views here.


class ScheduleListAPIView(ListAPIView):
    serializer_class = ScheduleSerializer
    
    def get_queryset(self) -> QuerySet:
        user_profile = self.request.user.studentprofilemodel
        queryset = ScheduleModel.objects.filter(group=user_profile.group)
        return queryset