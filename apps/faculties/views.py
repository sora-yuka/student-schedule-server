from rest_framework.generics import ListAPIView

from .models import FacultiesModel, SpecialtyModel, GroupsModel
from .serializers import FacultySerializer, SpecialtySerializer, GroupSerializer

# Create your views here.


class FacultyListAPIView(ListAPIView):
    serializer_class = FacultySerializer
    queryset = FacultiesModel.objects.all()
    
    
class SpecialtyListAPIView(ListAPIView):
    serializer_class = SpecialtySerializer
    queryset = SpecialtyModel.objects.all()
    
    
class GroupListAPIView(ListAPIView):
    serializer_class = GroupSerializer
    queryset = GroupsModel.objects.all()