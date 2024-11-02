from rest_framework.generics import ListAPIView

from .models import StudentProfileModel
from .serializers import ProfileSerializer


class ProfileListAPIView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = StudentProfileModel.objects.all()