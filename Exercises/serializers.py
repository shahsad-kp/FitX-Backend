from rest_framework.serializers import ModelSerializer

from Exercises.models import Exercise


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            'id', 'name', 'description', 'demo', 'count', 'duration', 'burn_calorie', 'video_link', 'focused_area')
