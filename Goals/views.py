from datetime import timedelta, datetime

import pytz
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from Goals.models import WeeklyExerciseGoal, WeeklyCategoryGoal, WeeklyCalorieGoal
from Goals.serializer import WeeklyCalorieGoalSerializer, WeeklyCategoryGoalSerializer, WeeklyExerciseGoalSerializer


class WeeklyCalorieGoalCreateUpdateRetrieveAPIView(CreateAPIView, RetrieveAPIView):
    serializer_class = WeeklyCalorieGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        current_date = datetime.now(pytz.UTC).date()
        last_sunday = current_date - timedelta(days=current_date.weekday() + 1)
        try:
            return WeeklyCalorieGoal.objects.get(user=user, week=last_sunday)
        except WeeklyCalorieGoal.DoesNotExist:
            return None

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method == 'GET':
            context['goal'] = None
        else:
            context['goal'] = self.request.data.get('goal')
        return context


class WeeklyCategoryGoalCreateUpdateRetrieveAPIView(CreateAPIView, RetrieveAPIView):
    serializer_class = WeeklyCategoryGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        current_date = datetime.now(pytz.UTC).date()
        last_sunday = current_date - timedelta(days=current_date.weekday() + 1)
        try:
            return WeeklyCategoryGoal.objects.get(user=user, week=last_sunday)
        except WeeklyCategoryGoal.DoesNotExist:
            return None

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method == 'GET':
            context['goal'] = None
        else:
            context['goal'] = self.request.data.get('goal')
        return context


class WeeklyExerciseGoalCreateUpdateRetrieveAPIView(CreateAPIView, RetrieveAPIView):
    serializer_class = WeeklyExerciseGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        current_date = datetime.now(pytz.UTC).date()
        last_sunday = current_date - timedelta(days=current_date.weekday() + 1)
        try:
            return WeeklyExerciseGoal.objects.get(user=user, week=last_sunday)
        except WeeklyExerciseGoal.DoesNotExist:
            return None

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method == 'GET':
            context['goal'] = None
        else:
            context['goal'] = self.request.data.get('goal')
        return context


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
