from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from Category.models import Category, CompletedCategory
from Category.serializers import CategorySerializer, CompletedCategorySerializer
from Exercises.models import Exercise
from Users.models import User
from Users.serializers import UserSerializer


class GetAllCategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class GetCategoryView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class UpdateCategoryView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'


class DeleteCategoryView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'


class AddExerciseIntoCategory(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request: Request, *args, **kwargs):
        category_id = kwargs.get('category_id', 0)
        exercise_id = kwargs.get('exercise_id', 0)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(
                {'detail': 'Category not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            exercise = Exercise.objects.get(id=exercise_id)
        except Exercise.DoesNotExist:
            return Response(
                {'detail': 'Exercise not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        if category.exercises.filter(id=exercise.id).exists():
            return Response(
                {'detail': 'Exercise is already added'},
                status=status.HTTP_409_CONFLICT
            )

        category.exercises.add(exercise)
        return Response({'detail': 'Exercise added to the category.'})


class RemoveExerciseFromCategory(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request: Request, *args, **kwargs):
        category_id = kwargs.get('category_id', 0)
        exercise_id = kwargs.get('exercise_id', 0)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(
                {'detail': 'Category not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            exercise = Exercise.objects.get(id=exercise_id)
        except Exercise.DoesNotExist:
            return Response(
                {'detail': 'Exercise not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        if not category.exercises.filter(id=exercise.id).exists():
            return Response(
                {'detail': 'Exercise is not in the category'},
                status=status.HTTP_409_CONFLICT
            )

        category.exercises.remove(exercise)
        return Response({'detail': 'Exercise removed from the category.'})


class GetCategoryLikes(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Category.objects.none()
        return category.liked_by.all()


class CompletedCategoryView(ListCreateAPIView):
    serializer_class = CompletedCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CompletedCategory.objects.filter(user=self.request.user)
