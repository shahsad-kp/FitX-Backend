from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response

from Category.models import Category, CompletedCategory
from Exercises.models import Exercise, CompletedExercise
from Exercises.serializers import ExerciseSerializer, CompletedExerciseSerializer


class CreateExercise(CreateAPIView):
    queryset = Exercise.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ExerciseSerializer


class GetExercise(RetrieveAPIView):
    queryset = Exercise.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExerciseSerializer
    lookup_field = 'id'


class UpdateExercise(UpdateAPIView):
    queryset = Exercise.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ExerciseSerializer
    lookup_field = 'id'

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'count' in request.data and 'duration' in request.data:
            return Response(
                {"detail": "Both 'count' and 'duration' cannot be provided simultaneously."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if 'count' in request.data:
            serializer.save(duration=None)
        elif 'duration' in request.data:
            serializer.save(count=None)
        else:
            serializer.save()

        return Response(serializer.data)


class DeleteExercise(DestroyAPIView):
    queryset = Exercise.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ExerciseSerializer
    lookup_field = 'id'


class GetListAllExercise(ListAPIView):
    queryset = Exercise.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExerciseSerializer


class GetCategoryExercise(ListAPIView):
    queryset = Exercise.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        category_id = self.kwargs['id']
        category = Category.objects.filter(id=category_id).first()
        if category:
            queryset = self.queryset.filter(category=category)
        else:
            queryset = self.queryset.none()
        return queryset


class CompleteExercise(CreateAPIView, ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CompletedExercise.objects.all()
    serializer_class = CompletedExerciseSerializer

    def post(self, request, *args, **kwargs):
        data = request.POST
        exercise_id = request.data.get('exercise_id')
        category_id = request.data.get('category_id')
        if exercise_id.isdigit():
            exercise_id = int(exercise_id)
        else:
            return Response(
                {"detail": "Exercise ID must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if category_id.isdigit():
            category_id = int(category_id)
        else:
            return Response(
                {"detail": "Category ID must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )
        exercise = Exercise.objects.filter(id=exercise_id).first()
        category = Category.objects.filter(id=category_id).first()
        if not (exercise and category):
            return Response(
                {"detail": "Exercise or category not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        if CompletedExercise.objects.filter(user=request.user, exercise=exercise, category=category).exists():
            return Response(
                {"detail": "Exercise already completed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        completed_exercise = CompletedExercise.objects.create(
            user=request.user,
            exercise=exercise,
            category=category
        )
        for exercise in category.exercises.all():
            if not CompletedExercise.objects.filter(user=request.user, exercise=exercise, category=category).exists():
                return Response(
                    {"detail": "Exercise completed."},
                )
        CompletedExercise.objects.filter(user=request.user, category=category).delete()
        CompletedCategory.objects.create(
            user=request.user,
            category=category
        )
        return Response(
            {"detail": "Category completed."},
        )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset
