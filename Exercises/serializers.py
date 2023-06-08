from rest_framework.serializers import ModelSerializer, ValidationError

from Exercises.models import Exercise


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'demo', 'count', 'duration')
