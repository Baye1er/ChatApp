import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Message, Space


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.space_name = self.scope['url_route']['kwargs']['space_name']
        self.space_group_name = 'chat_%s' % self.space_name

        await self.channel_layer.group_add(
            self.space_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.space_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        space = data['room']

        await self.save_message(space, username, message)

        await self.channel_layer.group_send(
            self.space_group_name,
            {
                'type': 'chat_message',
                'message' : message,
                'username' : username,
                'space' : space,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        space = event['space']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'space': space,
        }))

    @sync_to_async
    def save_message(self, space, username, message):
        user = User.objects.get(username=username).id
        space = Space.objects.get(slug=space).id

        Message.objects.create(space=space, user=user, content=message)

