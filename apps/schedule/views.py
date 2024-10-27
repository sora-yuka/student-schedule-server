from rest_framework.generics import ListAPIView

from .models import ScheduleModel
from .serializers import ScheduleSerializer

# Create your views here.


class ScheduleListAPIView(ListAPIView):
    serializer_class = ScheduleSerializer
    queryset = ScheduleModel.objects.all()