from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Room(models.Model):
    room = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.room
    

class Message(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, related_name="room_group")
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="sent_message")
    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="received_message")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.sender} to {self.receiver} at {self.timestamp}"