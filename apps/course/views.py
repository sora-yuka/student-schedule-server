from rest_framework.generics import ListAPIView

from .models import CourseModel
from .serializers import CourseSerializer

# Create your views here.


class CourseListAPIView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()