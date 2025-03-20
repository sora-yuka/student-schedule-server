import json
from typing import List, Dict, Any
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message
from .serializers import MessageSerializer

from apps.account.serializers import UserSerializer

User = get_user_model()


class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        request_user = self.scope["user"]
        
        if request_user.is_authenticated:
            try:
                chat_with_user = self.scope["url_route"]["kwargs"]["id"]
                user_ids = sorted([int(request_user.id), int(chat_with_user)])
                self.room_group_name = f"chat_{user_ids[0]}-{user_ids[1]}"
                
                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name,
                )
                
                await self.accept()
            
            except (KeyError, ValueError) as err:
                print("Error during connection: ", err)
                await self.close()
                
    async def receive(self, text_data=None, bytes_data=None) -> None:
        json_data = json.loads(text_data)
        
        message = await self.save_message(content=json_data["message"])
        
        serializer = MessageSerializer(message)
        serialized_message = serializer.data
        
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message",
                "message": serialized_message, # providing serialized message
            }
        )
    
    @database_sync_to_async
    def save_message(self, content: str) -> None:
        sender = self.scope["user"]
        receiver_id = self.scope["url_route"]["kwargs"]["id"]
        receiver = User.objects.get(id=receiver_id)
        
        try:
            room = Room.objects.get(room=self.room_group_name)
            
        except Room.DoesNotExist as err:
            room = Room.objects.create(room=self.room_group_name)
            
        new_message = Message.objects.create(
            room = room,
            sender = sender,
            receiver = receiver,
            content = content,
        )
        
        return new_message
                
    async def disconnect(self, close_code: int) -> None:
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
    
    async def chat_message(self, event: Dict[str, Any]) -> None:
        await self.send(text_data=json.dumps(event["message"]))