from django.db import models

from Users.models import User


class Message(models.Model):
    MESSAGE_TYPE = [('text', 'text'), ('image', 'image'), ('video', 'video'), ('audio', 'audio'), ('file', 'file')]

    text = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=30, choices=MESSAGE_TYPE, default='text')
    media = models.ForeignKey(to='MessageMedia', on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sended_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver} at {self.created_at}'


class MessageMedia(models.Model):
    media = models.FileField(upload_to='media/', null=False, blank=False)
