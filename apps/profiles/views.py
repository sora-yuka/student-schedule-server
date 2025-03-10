from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import StudentProfileModel
from .serializers import ProfileSerializer


class ProfilesListAPIView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = StudentProfileModel.objects.all()
    
    def get_queryset(self) -> StudentProfileModel:
        return StudentProfileModel.objects.exclude(owner=self.request.user.id)
    
    
class OwnProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = StudentProfileModel.objects.all()
    
    def get_object(self) -> StudentProfileModel:
        user = self.request.user
        profile = StudentProfileModel.objects.get(owner=user.id)
        return profile
    
    
class ProfileRetriveAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = StudentProfileModel.objects.all()
