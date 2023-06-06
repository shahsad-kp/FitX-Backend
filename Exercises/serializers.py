from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from Exercises.models import Category, Exercise


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'demo', 'count', 'duration')


class CategorySerializer(ModelSerializer):
    exercises = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image', 'music', 'exercises')
