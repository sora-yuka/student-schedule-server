from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import CourseModel, CourseContentModel
from .serializers import CourseSerializer, CourseContentSerializer
from apps.profiles.models import StudentProfileModel

# Create your views here.


class CourseListAPIView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    
    def list(self, request: Request, *args, **kwargs) -> Response:
        profile = StudentProfileModel.objects.get(owner=self.request.user)
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(group=profile.group)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
class CourseContentRetrieveAPIView(ListAPIView):
    serializer_class = CourseContentSerializer
    queryset = CourseContentModel.objects.all()
    
    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(course=kwargs.get("pk"))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)