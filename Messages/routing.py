from django.urls import path

from Messages.consumers import MessageConsumer

websocket_urlpatterns = [
    path('ws/messages/', MessageConsumer.as_asgi(), name='messages'),
]
