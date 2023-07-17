from rest_framework import serializers

from Messages.models import Message, MessageMedia
from Users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    sender_id = serializers.IntegerField(write_only=True)
    receiver_id = serializers.IntegerField(write_only=True)
    media_id = serializers.IntegerField(write_only=True)
    media = serializers.FileField(source='media.media', read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'text', 'type', 'media', 'media_id', 'sender', 'sender_id', 'receiver_id', 'receiver', 'created_at')


class MessageMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageMedia
        fields = ['media', 'id']
