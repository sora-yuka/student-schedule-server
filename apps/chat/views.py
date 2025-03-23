from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Q

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

# Create your views here.


class DirectListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        lookup_field = self.kwargs["pk"]
        user_id = self.request.user.id

        queryset = queryset.filter(
            Q(receiver_id=lookup_field) & Q(sender_id=user_id) | Q(receiver_id=user_id) & Q(sender_id=lookup_field)
        )
        
        return queryset