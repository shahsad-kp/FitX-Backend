from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from Category.models import Category
from Category.serializers import CategorySerializer
from Users.models import User
from Users.serializers import UserSerializer, GoalsSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            user = User.objects.get(username=serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }
            response.data = data
        return response


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
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class GetAllUsersListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUpdateUserGoals(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = GoalsSerializer
    lookup_field = 'id'

    def get_object(self):
        return self.request.user


class LikeACategory(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, *args, **kwargs):
        category_id = kwargs.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(
                data={
                    'detail': 'Category not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        print(category)
        request.user.liked_categories.add(category)
        return Response(
            {
                'detail': 'Category liked'
            },
            status=status.HTTP_202_ACCEPTED
        )


class DislikeACategory(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, *args, **kwargs):
        category_id = kwargs.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(
                data={
                    'detail': 'Category not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        request.user.liked_categories.remove(category)
        return Response(
            {
                'detail': 'Category dislike'
            },
            status=status.HTTP_202_ACCEPTED
        )


class GetAllLikedCategory(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()

    def get_queryset(self):
        queryset = Category.objects.filter(liked_by=self.request.user)
        return queryset
