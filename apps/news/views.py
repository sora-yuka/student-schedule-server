from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import NewsModel, ResourceModel
from .serializers import NewsSerializer, ResourceSerializer

# Create your views here.


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = NewsModel.objects.all()
    
    
class NewsRetrieveAPIView(RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = NewsModel.objects.all()