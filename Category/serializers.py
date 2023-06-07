from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from Category.models import Category


class CategorySerializer(ModelSerializer):
    exercises = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image', 'music', 'exercises')
