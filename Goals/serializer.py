from datetime import timedelta, datetime

import pytz
from rest_framework.serializers import ModelSerializer

from Goals.models import WeeklyCalorieGoal, WeeklyCategoryGoal, WeeklyExerciseGoal


class WeeklyCalorieGoalSerializer(ModelSerializer):
    class Meta:
        model = WeeklyCalorieGoal
        fields = ['user', 'week', 'goal']
        read_only_fields = ['user', 'week']

    def to_representation(self, instance):
        return {"goal": instance.goal}

    def create(self, validated_data):
        user = self.context['request'].user
        goal = validated_data['goal']
        current_date = datetime.now(pytz.UTC).date()
        last_sunday = current_date - timedelta(days=current_date.weekday() + 1)

        obj, created = WeeklyCalorieGoal.objects.update_or_create(
            user=user,
            week=last_sunday,
            defaults={'goal': goal}
        )

        return obj


class WeeklyCategoryGoalSerializer(ModelSerializer):
    class Meta:
        model = WeeklyCategoryGoal
        fields = ['user', 'week', 'goal']
        read_only_fields = ['user', 'week']

    def to_representation(self, instance):
        return {"goal": instance.goal}

    def create(self, validated_data):
        user = self.context['request'].user
        goal = validated_data['goal']
        current_date = datetime.now(pytz.UTC).date()
        last_sunday = current_date - timedelta(days=current_date.weekday() + 1)

        obj, created = WeeklyCategoryGoal.objects.update_or_create(
            user=user,
            week=last_sunday,
            defaults={'goal': goal}
        )

        return obj


class WeeklyExerciseGoalSerializer(ModelSerializer):
    class Meta:
        model = WeeklyExerciseGoal
        fields = ['user', 'week', 'goal']
        read_only_fields = ['user', 'week']

    def to_representation(self, instance):
        return {"goal": instance.goal}

    def create(self, validated_data):
        user = self.context['request'].user
        goal = validated_data['goal']
        current_date = datetime.now(pytz.UTC).date()
        last_sunday = current_date - timedelta(days=current_date.weekday() + 1)

        obj, created = WeeklyExerciseGoal.objects.update_or_create(
            user=user,
            week=last_sunday,
            defaults={'goal': goal}
        )

        return obj
