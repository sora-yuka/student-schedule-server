from rest_framework.generics import ListAPIView

from .models import LessonsModel
from .serializers import LessonsSerializer

# Create your views here.


class LessonsListAPIView(ListAPIView):
    serializer_class = LessonsSerializer
    queryset = LessonsModel.objects.all()