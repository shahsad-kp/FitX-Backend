from rest_framework import serializers

from Trainer.models import TrainerData, Certificate
from Users.serializers import UserSerializer


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'title', 'description', 'file']


class TrainerSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=120)
    certificates = CertificateSerializer(many=True)
    experience = serializers.DurationField()

    class Meta:
        model = TrainerData
        fields = ['id', 'phone', 'certificates', 'experience']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)


class TrainerListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    certificates = CertificateSerializer(many=True)

    class Meta:
        model = TrainerData
        fields = ['id', 'user', 'phone', 'certificates', 'experience']
