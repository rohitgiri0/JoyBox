import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

def get_models():
    from django.contrib.auth.models import User
    from .models import ChatRoom, Message
    return User, ChatRoom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("CONNECT called")
        try:
            self.room_id = self.scope['url_route']['kwargs']['room_id']
            print("Connecting to room:", self.room_id)
            self.room_group_name = f'chat_{self.room_id}'

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        except Exception as e:
            print("WebSocket connect error:", e)

    async def disconnect(self, close_code):
        print("DISCONNECT called")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print("RECEIVE called with:", text_data)
        data = json.loads(text_data)
        message = data['message']
        sender = self.scope["user"]

        User, ChatRoom, Message = get_models()

        try:
            room = await database_sync_to_async(ChatRoom.objects.get)(id=self.room_id)
            await database_sync_to_async(Message.objects.create)(
                chat_room=room,
                sender=sender,
                content=message
            )
        except ChatRoom.DoesNotExist:
            return

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': sender.username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
        }))