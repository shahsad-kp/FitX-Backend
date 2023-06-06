from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from Users.models import User
from Users.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class GetUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated | IsAdminUser]

    def get_object(self):
        user_id = self.kwargs.get('id')  # Assuming the URL pattern captures the user ID
        user = User.objects.get(id=int(user_id))
        if user.is_superuser or (user.id == self.request.user.id):
            return user
        else:
            self.permission_denied(self.request)


class GetSelfUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UpdateUserView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated | IsAdminUser]
    lookup_field = 'id'

    def get_object(self):
        user_id = self.kwargs.get('id')  # Assuming the URL pattern captures the user ID
        user = User.objects.get(id=int(user_id))
        if user.is_superuser or (user.id == self.request.user.id):
            return user
        else:
            self.permission_denied(self.request)


class UpdateSelfUserView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        return self.request.user


class DeleteUserView(DestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'



