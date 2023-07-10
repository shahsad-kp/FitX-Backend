from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer


def make_group_name(user_id):
    return f'chat_{user_id}'


@database_sync_to_async
def save_message(message: dict):
    from Users.models import User
    from Messages.serializers import MessageSerializer
    try:
        message['receiver_id'] = User.objects.get(id=message.pop('receiver_id')).id
    except User.DoesNotExist:
        raise ValueError('Receiver does not exist')

    serializer = MessageSerializer(data=message)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


class MessageConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None
        self.user = None

    async def connect(self):
        if self.scope['user'].is_anonymous:
            await self.close(code=1009)
            return
        self.user = self.scope['user']
        self.room_group_name = make_group_name(self.user.id)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive_json(self, content, **kwargs):
        if content['type'] == 'message':
            message_data = content['message']
            message_data['sender_id'] = self.user.id
            message = await save_message(message_data)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'message',
                    'message': message
                }
            )
            if message['receiver']['id'] != self.user.id:
                await self.channel_layer.group_send(
                    make_group_name(message['receiver']['id']),
                    {
                        'type': 'message',
                        'message': message
                    }
                )

    async def message(self, event):
        await self.send_json(event)

    async def disconnect(self, close_code):
        if self.room_group_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
        await self.close(code=close_code)
