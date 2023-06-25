from rest_framework.serializers import ModelSerializer

from Goals.models import WeeklyCalorieGoal, WeeklyCategoryGoal, WeeklyExerciseGoal


class WeeklyCalorieGoalSerializer(ModelSerializer):
    class Meta:
        model = WeeklyCalorieGoal
        fields = ['calorie_goal', 'last_date', 'user']


class WeeklyCategoryGoalSerializer(ModelSerializer):
    class Meta:
        model = WeeklyCategoryGoal
        fields = ['category_goal', 'last_date', 'user']


class WeeklyExerciseGoalSerializer(ModelSerializer):
    class Meta:
        model = WeeklyExerciseGoal
        fields = ['exercise_goal', 'last_date', 'user']
