from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAuthenticated

from Messages.models import Message
from Messages.serializers import MessageSerializer
from Users.serializers import UserSerializer
from Users.models import User


class MessagePagination(CursorPagination):
    ordering = '-created_at'
    page_size = 20


class AllMessagesView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MessagePagination

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Message.objects.filter(
            Q(
                sender_id=user_id,
                receiver_id=self.request.user.id
            ) |
            Q(
                sender_id=self.request.user.id,
                receiver_id=user_id
            )
        )


class AllMessagedUsersView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            Q(
                sended_messages__receiver_id=self.request.user.id
            ) |
            Q(
                received_messages__sender_id=self.request.user.id
            )
        ).distinct()
