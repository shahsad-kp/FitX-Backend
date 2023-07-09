from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from Transformation.models import TransformationImage
from Transformation.serializers import TransformationImageSerializer


class TransformationImageView(ListCreateAPIView):
    serializer_class = TransformationImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: TransformationImageSerializer):
        serializer.initial_data['user'] = self.request.user
        return super().perform_create(serializer)

    def get_queryset(self):
        return TransformationImage.objects.all().filter(user=self.request.user)
