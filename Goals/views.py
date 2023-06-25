from datetime import date, timedelta

from django.http import HttpRequest, HttpResponse
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Goals.models import WeeklyExerciseGoal, WeeklyCategoryGoal, WeeklyCalorieGoal
from Goals.serializer import WeeklyCalorieGoalSerializer, WeeklyCategoryGoalSerializer, WeeklyExerciseGoalSerializer


class WeeklyCalorieGoalViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        calorie = request.data.get('calorie_goal')
        if not calorie:
            return HttpResponse(
                content="{'calorie_goal': 'This field may not be null.'}",
                status=status.HTTP_400_BAD_REQUEST
            )
        today = date.today()
        days_ahead = (6 - today.weekday() + 7) % 7
        next_sunday = today + timedelta(days=days_ahead)

        serializer = WeeklyCalorieGoalSerializer(data={
            'user': request.user.pk,
            'last_date': next_sunday,
            'calorie_goal': calorie
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=201)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        today = date.today()
        days_ahead = (6 - today.weekday() + 7) % 7
        next_sunday = today + timedelta(days=days_ahead)

        goal = request.user.weekly_calorie_goals.filter(last_date=next_sunday).first()
        if goal is None:
            return HttpResponse(status=404)
        return HttpResponse(goal.calorie_goal)


class WeeklyCategoryGoalViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        category = request.data.get('category_goal')
        if not category:
            return HttpResponse(
                content="{'category_goal': 'This field may not be null.'}",
                status=status.HTTP_400_BAD_REQUEST
            )
        today = date.today()
        days_ahead = (6 - today.weekday() + 7) % 7
        next_sunday = today + timedelta(days=days_ahead)

        serializer = WeeklyCategoryGoalSerializer(data={
            'user': request.user.pk,
            'last_date': next_sunday,
            'category_goal': category
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=201)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        today = date.today()
        days_ahead = (6 - today.weekday() + 7) % 7
        next_sunday = today + timedelta(days=days_ahead)

        goal = request.user.weekly_category_goals.filter(last_date=next_sunday).first()
        if goal is None:
            return HttpResponse(status=404)
        return HttpResponse(goal.category_goal)


class WeeklyExerciseGoalViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        exercise = request.data.get('exercise_goal')
        if not exercise:
            return HttpResponse(
                content="{'exercise_goal': 'This field may not be null.'}",
                status=status.HTTP_400_BAD_REQUEST
            )
        today = date.today()
        days_ahead = (6 - today.weekday() + 7) % 7
        next_sunday = today + timedelta(days=days_ahead)

        serializer = WeeklyExerciseGoalSerializer(data={
            'user': request.user.pk,
            'last_date': next_sunday,
            'exercise_goal': exercise
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=201)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        today = date.today()
        days_ahead = (6 - today.weekday() + 7) % 7
        next_sunday = today + timedelta(days=days_ahead)

        goal = request.user.weekly_exercise_goals.filter(last_date=next_sunday).first()
        if goal is None:
            return HttpResponse(status=404)
        return HttpResponse(goal.exercise_goal)


class GetAllExerciseGoals(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WeeklyExerciseGoalSerializer
    queryset = WeeklyExerciseGoal.objects.get_queryset()

    def get_queryset(self):
        return self.request.user.weekly_exercise_goals.all()


class GetAllCategoryGoals(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WeeklyCategoryGoalSerializer
    queryset = WeeklyCategoryGoal.objects.get_queryset()

    def get_queryset(self):
        return self.request.user.weekly_category_goals.all()


class GetAllCalorieGoals(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WeeklyCalorieGoalSerializer
    queryset = WeeklyCalorieGoal.objects.get_queryset()

    def get_queryset(self):
        return self.request.user.weekly_calorie_goals.all()
