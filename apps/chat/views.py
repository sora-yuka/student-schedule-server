from rest_framework.generics import ListAPIView
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

# Create your views here.


class MessageListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    # def get_object(self) -> Message:
    #     user = self.user.request
    #     messages = Message.objects.get()