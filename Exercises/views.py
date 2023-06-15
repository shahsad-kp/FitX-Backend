from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response

from Category.models import Category
from Exercises.models import Exercise
from Exercises.serializers import ExerciseSerializer


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
