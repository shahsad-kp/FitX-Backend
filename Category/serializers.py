from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from Category.models import Category


class CategorySerializer(ModelSerializer):
    exercises_count = SerializerMethodField()
    likes = SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image', 'music', 'exercises_count', 'likes')

    def get_exercises_count(self, instance):
        return instance.exercises.count()

    def get_likes(self, instance):
        return instance.likes.count()
