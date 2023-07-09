from rest_framework.serializers import ModelSerializer

from Transformation.models import TransformationImage


class TransformationImageSerializer(ModelSerializer):
    class Meta:
        model = TransformationImage
        fields = ('id', 'image', 'date')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
